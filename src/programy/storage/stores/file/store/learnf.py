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
from programy.utils.logging.ylogger import YLogger
import os
import os.path
import xml.etree.ElementTree as ET

from programy.storage.stores.file.store.filestore import FileStore
from programy.storage.entities.learnf import LearnfStore

from programy.utils.logging.ylogger import YLogger



class FileLearnfStore(FileStore, LearnfStore):

    def __init__(self, storage_engine):
        FileStore.__init__(self, storage_engine)

    @staticmethod
    def create_learnf_path(client_context, learnf_dir):
        return "%s%s%s.aiml"%(learnf_dir, os.sep, client_context.userid)

    @staticmethod
    def create_learnf_file_if_missing(learnf_path):

        if os.path.isfile(learnf_path) is False:
            try:
                with open(learnf_path, "w+", encoding="utf-8") as file:
                    file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
                    file.write('<aiml>\n')
                    file.write('</aiml>\n')
                    file.close()
            except Exception as excep:
                YLogger.exception(None, "Error Writing learnf to %s", excep, learnf_path)

    @staticmethod
    def write_node_to_learnf_file(client_context, node, learnf_path):

        YLogger.debug(client_context, "Writing learnf to %s", learnf_path)

        tree = ET.parse(learnf_path)
        root = tree.getroot()
        root.append(node)
        tree.write(learnf_path, method="xml")

    def _get_storage_path(self):
        if len(self.storage_engine.configuration.learnf_storage.dirs) > 1:
            YLogger.warning(self, "Learnf Storage has multiple folders specified, using first only")

        return self.storage_engine.configuration.learnf_storage.dirs[0]

    def create_category_xml_node(self, client_context, category)   :
        # Add our new element
        child = ET.Element("category")
        child.append(ET.Element(category.pattern))
        child.append(ET.Element(category.topic))
        child.append(ET.Element(category.that))
        child.append(category.template.xml_tree(client_context))
        return child

    def save_learnf(self, client_context, category):
        try:
            xml_node = self.create_category_xml_node(client_context, category)

            learnf_path = self._get_storage_path()
            self._ensure_dir_exists(learnf_path)

            learnf_fullpath = self.create_learnf_path(client_context, learnf_path)

            self.create_learnf_file_if_missing(learnf_fullpath)

            self.write_node_to_learnf_file(client_context, xml_node, learnf_fullpath)

        except Exception as exc:
            YLogger.exception(client_context, "Failed to save learnf", exc)
