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

from programy.config.base import BaseConfigurationData
from programy.storage.stores.file.engine import FileStorageEngine
from programy.storage.stores.file.store.config import FileStoreConfiguration
from programy.storage.stores.file.store.filestore import FileStore


class FileStorageConfiguration(BaseConfigurationData):

    def __init__(self, name="files"):
        BaseConfigurationData.__init__(self, name=name)

        self._categories_storage        = FileStoreConfiguration(dirs=["./storage/categories"], extension="aiml", subdirs=True, format="xml", encoding="utf-8", delete_on_start=False)
        self._errors_storage            = FileStoreConfiguration(file="./storage/debug/errors.txt", format="text", encoding="utf-8", delete_on_start=False)
        self._duplicates_storage        = FileStoreConfiguration(file="./storage/debug/duplicates.txt", format="text", encoding="utf-8", delete_on_start=False)
        self._learnf_storage            = FileStoreConfiguration(dirs=["./storage/categories/learnf"], extension="aiml", subdirs=False, format="xml", encoding="utf-8", delete_on_start=False)

        self._conversation_storage      = FileStoreConfiguration(dirs=["./storage/conversations"], extension="txt", subdirs=False, format="text", encoding="utf-8", delete_on_start=False)
        
        self._sets_storage = FileStoreConfiguration(dirs=["./storage/sets"], extension="txt", subdirs=False, format="text", encoding="utf-8", delete_on_start=False)
        self._maps_storage = FileStoreConfiguration(dirs=["./storage/maps"], extension="txt", subdirs=False, format="text", encoding="utf-8", delete_on_start=False)
        self._rdf_storage = FileStoreConfiguration(dirs=["./storage/rdfs"], extension="txt", subdirs=True, format="text", encoding="utf-8", delete_on_start=False)

        self._denormal_storage = FileStoreConfiguration(file="./storage/lookups/denormal.txt", format="text", encoding="utf-8", delete_on_start=False)
        self._normal_storage = FileStoreConfiguration(file="./storage/lookups/normal.txt", format="text", encoding="utf-8", delete_on_start=False)
        self._gender_storage = FileStoreConfiguration(file="./storage/lookups/gender.txt", format="text", encoding="utf-8", delete_on_start=False)
        self._person_storage = FileStoreConfiguration(file="./storage/lookups/person.txt", format="text", encoding="utf-8", delete_on_start=False)
        self._person2_storage = FileStoreConfiguration(file="./storage/lookups/person2.txt", format="text", encoding="utf-8", delete_on_start=False)
        self._regex_storage = FileStoreConfiguration(file="./storage/lookups/regex.txt", format="text", encoding="utf-8", delete_on_start=False)

        self._properties_storage = FileStoreConfiguration(file="./storage/properties.txt", format="text", encoding="utf-8", delete_on_start=False)
        self._defaults_storage = FileStoreConfiguration(file="./storage/defaults.txt", format="text", encoding="utf-8", delete_on_start=False)
        self._variables_storage = FileStoreConfiguration(dirs=["./storage/variables"], extension="txt", subdirs=False, format="text", encoding="utf-8", delete_on_start=False)

        self._twitter_storage = FileStoreConfiguration(dirs=["./storage/twitter"], extension="txt", subdirs=False, format="text", encoding="utf-8", delete_on_start=False)

        self._spelling_storage = FileStoreConfiguration(file="./storage/spelling/corpus.txt", format="text", encoding="utf-8", delete_on_start=False)

        self._license_storage = FileStoreConfiguration(file="./storage/licenses/license.keys", format="text", encoding="utf-8", delete_on_start=False)

        self._pattern_nodes_storage = FileStoreConfiguration(file="./storage/nodes/pattern_nodes.txt", format="text", encoding="utf-8", delete_on_start=False)
        self._template_nodes_storage = FileStoreConfiguration(file="./storage/nodes/template_nodes.txt", format="text", encoding="utf-8", delete_on_start=False)

        self._binaries_storage = FileStoreConfiguration(file="./storage/braintree/braintree.bin", format="binary", encoding="utf-8", delete_on_start=False)
        self._braintree_storage = FileStoreConfiguration(file="./storage/braintree/braintree.xml", format="xml", encoding="utf-8", delete_on_start=False)

        self._preprocessors_storage = FileStoreConfiguration(file="./storage/processing/preprocessors.txt", format="text", encoding="utf-8", delete_on_start=False)
        self._postprocessors_storage = FileStoreConfiguration(file="./storage/processing/postprocessors.txt", format="text", encoding="utf-8", delete_on_start=False)

        self._usergroups_storage = FileStoreConfiguration(file="./storage/security/usergroups.yaml", format="yaml", encoding="utf-8", delete_on_start=False)

    @property
    def categories_storage(self):
        return self._categories_storage

    @property
    def errors_storage(self):
        return self._errors_storage

    @property
    def duplicates_storage(self):
        return self._duplicates_storage

    @property
    def learnf_storage(self):
        return self._learnf_storage

    @property
    def conversation_storage(self):
        return self._conversation_storage

    @property
    def sets_storage(self):
        return self._sets_storage

    @property
    def maps_storage(self):
        return self._maps_storage

    @property
    def rdf_storage(self):
        return self._rdf_storage

    @property
    def regex_storage(self):
        return self._regex_storage

    @property
    def denormal_storage(self):
        return self._denormal_storage

    @property
    def normal_storage(self):
        return self._normal_storage

    @property
    def gender_storage(self):
        return self._gender_storage

    @property
    def person_storage(self):
        return self._person_storage

    @property
    def person2_storage(self):
        return self._person2_storage

    @property
    def properties_storage(self):
        return self._properties_storage
    
    @property
    def variables_storage(self):
        return self._variables_storage

    @property
    def defaults_storage(self):
        return self._defaults_storage

    @property
    def twitter_storage(self):
        return self._twitter_storage

    @property
    def spelling_storage(self):
        return self._spelling_storage

    @property
    def license_storage(self):
        return self._license_storage

    @property
    def pattern_nodes_storage(self):
        return self._pattern_nodes_storage

    @property
    def template_nodes_storage(self):
        return self._template_nodes_storage

    @property
    def binaries_storage(self):
        return self._binaries_storage

    @property
    def braintree_storage(self):
        return self._braintree_storage

    @property
    def preprocessors_storage(self):
        return self._preprocessors_storage

    @property
    def postprocessors_storage(self):
        return self._postprocessors_storage

    @property
    def usergroups_storage(self):
        return self._usergroups_storage

    def load_storage_config(self, storage_config, name, configuration_file, storage, bot_root):
        config_section = configuration_file.get_option(storage, 'config')
        storage_config_section = configuration_file.get_option(config_section, name)
        if storage_config_section is not None:
            storage_config.extract_configuration(configuration_file, storage_config_section, bot_root)

    def load_config_section(self, configuration_file, storage, bot_root):
        if storage is not None:
            self.load_storage_config(self._categories_storage, FileStore.CATEGORIES_STORAGE, configuration_file, storage, bot_root)
            self.load_storage_config(self._errors_storage, FileStore.ERRORS_STORAGE, configuration_file, storage, bot_root)
            self.load_storage_config(self._duplicates_storage, FileStore.DUPLICATES_STORAGE, configuration_file, storage, bot_root)
            self.load_storage_config(self._learnf_storage, FileStore.LEARNF_STORAGE, configuration_file, storage, bot_root)

            self.load_storage_config(self._conversation_storage, FileStore.CONVERSATION_STORAGE, configuration_file, storage, bot_root)

            self.load_storage_config(self._sets_storage, FileStore.SETS_STORAGE, configuration_file, storage, bot_root)
            self.load_storage_config(self._maps_storage, FileStore.MAPS_STORAGE, configuration_file, storage, bot_root)
            self.load_storage_config(self._rdf_storage, FileStore.RDF_STORAGE, configuration_file, storage, bot_root)

            self.load_storage_config(self._denormal_storage, FileStore.DENORMAL_STORAGE, configuration_file, storage, bot_root)
            self.load_storage_config(self._normal_storage, FileStore.NORMAL_STORAGE, configuration_file, storage, bot_root)
            self.load_storage_config(self._gender_storage, FileStore.GENDER_STORAGE, configuration_file, storage, bot_root)
            self.load_storage_config(self._person_storage, FileStore.PERSON_STORAGE, configuration_file, storage, bot_root)
            self.load_storage_config(self._person2_storage, FileStore.PERSON2_STORAGE, configuration_file, storage, bot_root)
            self.load_storage_config(self._regex_storage, FileStore.REGEX_STORAGE, configuration_file, storage, bot_root)

            self.load_storage_config(self._properties_storage, FileStore.PROPERTIES_STORAGE, configuration_file, storage, bot_root)
            self.load_storage_config(self._variables_storage, FileStore.VARIABLES_STORAGE, configuration_file, storage, bot_root)
            self.load_storage_config(self._defaults_storage, FileStore.DEFAULTS_STORAGE, configuration_file, storage, bot_root)

            self.load_storage_config(self._twitter_storage, FileStore.TWITTER_STORAGE, configuration_file, storage, bot_root)

            self.load_storage_config(self._spelling_storage, FileStore.SPELLING_STORAGE, configuration_file, storage, bot_root)

            self.load_storage_config(self._license_storage, FileStore.LICENSE_STORAGE, configuration_file, storage, bot_root)

            self.load_storage_config(self._pattern_nodes_storage, FileStore.PATTERN_NODES_STORAGE, configuration_file, storage, bot_root)
            self.load_storage_config(self._template_nodes_storage, FileStore.TEMPLATE_NODES_STORAGE, configuration_file, storage, bot_root)

            self.load_storage_config(self._binaries_storage, FileStore.BINARIES_STORAGE, configuration_file, storage, bot_root)
            self.load_storage_config(self._braintree_storage, FileStore.BRAINTREE_STORAGE, configuration_file, storage, bot_root)

            self.load_storage_config(self._preprocessors_storage, FileStore.PREPROCESSORS_STORAGE, configuration_file, storage, bot_root)
            self.load_storage_config(self._postprocessors_storage, FileStore.POSTPROCESSORS_STORAGE, configuration_file, storage, bot_root)

            self.load_storage_config(self._usergroups_storage, FileStore.USERGROUPS_STORAGE, configuration_file, storage, bot_root)

    def create_filestorage_config(self):
        config = {}
        self._create_storage_map(config)

        if len(config.keys()) > 0:
            return config

        return None

    def to_yaml(self, data, defaults=True):
        if defaults is True:
            self._create_storage_defaults(data)
        else:
            self._create_storage_map(data)

    def create_engine(self):
        engine = FileStorageEngine(self)
        engine.initialise()
        return engine

    def _create_storage_map(self, amap):
        
        amap[FileStore.CATEGORIES_STORAGE] = self._categories_storage
        amap[FileStore.ERRORS_STORAGE] = self._errors_storage
        amap[FileStore.DUPLICATES_STORAGE] = self._duplicates_storage
        amap[FileStore.LEARNF_STORAGE] = self._learnf_storage

        amap[FileStore.CONVERSATION_STORAGE] = self._conversation_storage

        amap[FileStore.SETS_STORAGE] = self._sets_storage
        amap[FileStore.MAPS_STORAGE] = self._maps_storage
        amap[FileStore.RDF_STORAGE] = self._rdf_storage

        amap[FileStore.DENORMAL_STORAGE] = self._denormal_storage
        amap[FileStore.NORMAL_STORAGE] = self._normal_storage
        amap[FileStore.GENDER_STORAGE] = self._gender_storage
        amap[FileStore.PERSON_STORAGE] = self._person_storage
        amap[FileStore.PERSON2_STORAGE] = self._person2_storage
        amap[FileStore.REGEX_STORAGE] = self._regex_storage

        amap[FileStore.PROPERTIES_STORAGE] = self._properties_storage
        amap[FileStore.VARIABLES_STORAGE] = self._variables_storage
        amap[FileStore.DEFAULTS_STORAGE] = self._defaults_storage

        amap[FileStore.TWITTER_STORAGE] = self._twitter_storage

        amap[FileStore.SPELLING_STORAGE] = self._spelling_storage

        amap[FileStore.LICENSE_STORAGE] = self._license_storage

        amap[FileStore.PATTERN_NODES_STORAGE] = self._pattern_nodes_storage
        amap[FileStore.TEMPLATE_NODES_STORAGE] = self._template_nodes_storage

        amap[FileStore.BINARIES_STORAGE] = self._binaries_storage
        amap[FileStore.BRAINTREE_STORAGE] = self._braintree_storage

        amap[FileStore.PREPROCESSORS_STORAGE] = self._preprocessors_storage
        amap[FileStore.POSTPROCESSORS_STORAGE] = self._postprocessors_storage

        amap[FileStore.USERGROUPS_STORAGE] = self._usergroups_storage

    def _create_storage_defaults(self, amap):

        amap[FileStore.CATEGORIES_STORAGE] = FileStoreConfiguration(dirs=["./storage/categories"], extension="aiml", subdirs=True,
                                                        format="xml", encoding="utf-8", delete_on_start=False)
        amap[FileStore.ERRORS_STORAGE] = FileStoreConfiguration(file="./storage/debug/errors.txt", format="text",
                                                        encoding="utf-8", delete_on_start=False)
        amap[FileStore.DUPLICATES_STORAGE] = FileStoreConfiguration(file="./storage/debug/duplicates.txt", format="text",
                                                        encoding="utf-8", delete_on_start=False)
        amap[FileStore.LEARNF_STORAGE] = FileStoreConfiguration(dirs=["./storage/categories/learnf"], extension="aiml", subdirs=False,
                                                      format="xml", encoding="utf-8", delete_on_start=False)

        amap[FileStore.CONVERSATION_STORAGE] = FileStoreConfiguration(dirs=["./storage/conversations"], extension="txt",
                                                            subdirs=False, format="text", encoding="utf-8",
                                                            delete_on_start=False)

        amap[FileStore.SETS_STORAGE] = FileStoreConfiguration(dirs=["./storage/sets"], extension="txt", subdirs=False,
                                                    format="text", encoding="utf-8", delete_on_start=False)
        amap[FileStore.MAPS_STORAGE] = FileStoreConfiguration(dirs=["./storage/maps"], extension="txt", subdirs=False,
                                                    format="text", encoding="utf-8", delete_on_start=False)
        amap[FileStore.RDF_STORAGE] = FileStoreConfiguration(dirs=["./storage/rdfs"], extension="txt", subdirs=True,
                                                   format="text", encoding="utf-8", delete_on_start=False)

        amap[FileStore.DENORMAL_STORAGE] = FileStoreConfiguration(file="./storage/lookups/denormal.txt", format="text",
                                                        encoding="utf-8", delete_on_start=False)
        amap[FileStore.NORMAL_STORAGE] = FileStoreConfiguration(file="./storage/lookups/normal.txt", format="text",
                                                      encoding="utf-8", delete_on_start=False)
        amap[FileStore.GENDER_STORAGE] = FileStoreConfiguration(file="./storage/lookups/gender.txt", format="text",
                                                      encoding="utf-8", delete_on_start=False)
        amap[FileStore.PERSON_STORAGE] = FileStoreConfiguration(file="./storage/lookups/person.txt", format="text",
                                                      encoding="utf-8", delete_on_start=False)
        amap[FileStore.PERSON2_STORAGE] = FileStoreConfiguration(file="./storage/lookups/person2.txt", format="text",
                                                       encoding="utf-8", delete_on_start=False)
        amap[FileStore.REGEX_STORAGE] = FileStoreConfiguration(file="./storage/lookups/regex.txt", format="text",
                                                     encoding="utf-8", delete_on_start=False)

        amap[FileStore.PROPERTIES_STORAGE] = FileStoreConfiguration(file="./storage/properties.txt", format="text",
                                                          encoding="utf-8", delete_on_start=False)
        amap[FileStore.DEFAULTS_STORAGE] = FileStoreConfiguration(file="./storage/defaults.txt", format="text",
                                                          encoding="utf-8", delete_on_start=False)
        amap[FileStore.VARIABLES_STORAGE] = FileStoreConfiguration(dirs=["./storage/variables"], extension="txt", subdirs=False,
                                                         format="text", encoding="utf-8", delete_on_start=False)

        amap[FileStore.TWITTER_STORAGE] = FileStoreConfiguration(dirs=["./storage/twitter"], extension="txt", subdirs=False,
                                                       format="text", encoding="utf-8", delete_on_start=False)

        amap[FileStore.SPELLING_STORAGE] = FileStoreConfiguration(file="./storage/spelling/corpus.txt", format="text",
                                                        encoding="utf-8", delete_on_start=False)

        amap[FileStore.LICENSE_STORAGE] = FileStoreConfiguration(file="./storage/licenses/license.keys", format="text",
                                                       encoding="utf-8", delete_on_start=False)

        amap[FileStore.PATTERN_NODES_STORAGE] = FileStoreConfiguration(file="./storage/nodes/pattern_nodes.txt", format="text",
                                                             encoding="utf-8", delete_on_start=False)
        amap[FileStore.TEMPLATE_NODES_STORAGE] = FileStoreConfiguration(file="./storage/nodes/template_nodes.txt", format="text",
                                                              encoding="utf-8", delete_on_start=False)

        amap[FileStore.BINARIES_STORAGE] = FileStoreConfiguration(file="./storage/braintree/braintree.bin", format="binary",
                                                        encoding="utf-8", delete_on_start=False)
        amap[FileStore.BRAINTREE_STORAGE] = FileStoreConfiguration(file="./storage/braintree/braintree.xml", format="xml",
                                                         encoding="utf-8", delete_on_start=False)

        amap[FileStore.PREPROCESSORS_STORAGE] = FileStoreConfiguration(file="./storage/processing/preprocessors.txt",
                                                             format="text", encoding="utf-8", delete_on_start=False)
        amap[FileStore.POSTPROCESSORS_STORAGE] = FileStoreConfiguration(file="./storage/processing/postprocessors.txt",
                                                              format="text", encoding="utf-8", delete_on_start=False)

        amap[FileStore.USERGROUPS_STORAGE] = FileStoreConfiguration(file="./storage/security/usergroups.txt", format="text",
                                                          encoding="utf-8", delete_on_start=False)
