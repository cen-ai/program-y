"""
Copyright (c) 2016-17 Keith Sterling http://www.keithsterling.com

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
import logging
from programy.services.service import Service
from programy.config.sections.brain.service import BrainServiceConfiguration
from programy.services.requestsapi import RequestsAPI
import json

class WeatherAPI(object):

    def __init__(self, request_api=None):
        if request_api is None:
            self._requests_api = RequestsAPI()
        else:
            self._requests_api = request_api
    def ask_question(self,url, question, botid):
        payload = {'apikey': botid, 'q': question}
        locresponse = self._requests_api.get(url+'/locations/v1/cities/autocomplete', params=payload)

        if locresponse is None:
            raise Exception("No Such Location from weather service")
        receive_payload = json.loads(locresponse.text, encoding="utf-8")
        weresponse = self._requests_api.get(url+'/currentconditions/v1/'+receive_payload[0]['Key'],payload)
        weatherinfo=json.loads(weresponse.text, encoding="utf-8")
        return "Current Weather Conditions in "+receive_payload[0]['LocalizedName']+", "+receive_payload[0]['Country']['ID']+" is "+weatherinfo[0]['WeatherText']+" and temperature is "+str(weatherinfo[0]['Temperature']['Imperial']['Value'])+weatherinfo[0]['Temperature']['Imperial']['Unit']


class WeatherService(Service):

    def __init__(self, config: BrainServiceConfiguration, api=None):
        Service.__init__(self, config)

        if api is None:
            self.api = WeatherAPI()
        else:
            self.api = api

        if config is None:
            raise Exception("Undefined url parameter")
        else:
            self.config=config

    def ask_question(self, bot, clientid: str, question: str):
        try:
            if bot.license_keys.has_key('WEATHER_KEYS'):
                botid = bot.license_keys.get_key('WEATHER_KEYS')
            else:
                if logging.getLogger().isEnabledFor(logging.ERROR):
                    logging.error("No variable WEATHER_KEYS found in license key file")
                return ""

            return self.api.ask_question(self.config.url,question, botid)

        except Exception as excep:
            if logging.getLogger().isEnabledFor(logging.ERROR):
                logging.error(str(excep))
            return ""
