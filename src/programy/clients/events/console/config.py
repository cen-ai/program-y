"""
Copyright (c) 2016-2018 Keith Sterling http://www.keithsterling.com

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
from programy.config.client.config import ClientConfigurationData


class ConsoleConfiguration(ClientConfigurationData):

    def __init__(self):
        ClientConfigurationData.__init__(self, "console")
        self._default_userid = "console"
        self._prompt = ">>>"

    @property
    def default_userid(self):
        return self._default_userid

    @property
    def prompt(self):
        return self._prompt

    def load_configuration(self, configuration_file, bot_root):
        console = configuration_file.get_section(self.section_name)
        if console is not None:
            self._default_userid = configuration_file.get_option(console, "default_userid", missing_value="Console")
            self._prompt = configuration_file.get_option(console, "prompt", missing_value=">>>")
        super(ConsoleConfiguration, self).load_configuration(configuration_file, console, bot_root)

    def to_yaml(self, data, defaults=True):
        if defaults is True:
            data['default_userid'] = "console"
            data['prompt'] = ">>>"
        else:
            data['default_userid'] = self._default_userid
            data['prompt'] = self._prompt
        super(ConsoleConfiguration, self).to_yaml(data, defaults)