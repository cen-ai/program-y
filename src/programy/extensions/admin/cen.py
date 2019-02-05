"""
Copyright (c) 2016-2018 Keith Sterling http://www.keithsterling.com

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions
of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""
from programy.utils.logging.ylogger import YLogger

from programy.extensions.base import Extension
from programy.storage.factory import StorageFactory

class CenAdminExtension(Extension):


    def update_aiml(self, client_context):
        YLogger.debug(client_context, "Updating all AIML ")
        client_context.brain.update_aiml()
        return 'CENADMIN OK'

    def delete_aiml(self, client_context):
        YLogger.debug(client_context, "Deleting Unwanted AIML")
        client_context.brain.delete_aiml()
        return 'CENADMIN OK'

    # execute() is the interface that is called from the <extension> tag in the AIML
    def execute(self, client_context, data):
        YLogger.debug(client_context, "Cen Admin - [%s]", data)
        try:
            commands = CenAdminExtension.split_into_commands(data)
            if commands[0] == 'UPDATE':
                entity = commands[1]
                if entity in ['AIML']:
                    if entity == 'AIML':
                            return self.update_aiml(client_context)
                else:
                    raise Exception ("Unknown reload entity [%s]"%entity)
            elif commands[0] == 'DELETE':
                entity = commands[1]
                if entity in ['AIML']:
                    if entity == 'AIML':
                            return self.delete_aiml(client_context)
                else:
                    raise Exception ("Unknown reload entity [%s]"%entity)

            elif commands[0] == 'COMMANDS':
                return "UPDATE [AIML]"

            else:
                raise Exception ("Unknown reload command [%s]"%commands[0])

        except Exception as e:
            YLogger.exception(client_context, "Failed to execute cen extension", e)

        return "Cen Admin Error"
