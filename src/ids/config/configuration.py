from ids.constants import *
from ids.utils.common import read_yaml, create_directories
from ids.entity.config_entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(
        self,
        config_path = CONFIG_FILE_PATH,
        params_path = PARAMS_FILE_PATH,
        schema_path = SCHEMA_FILE_PATH):
        self.config = read_yaml(config_path)
        print(self.config)
        self.params = read_yaml(params_path)
        print(self.params)
        self.schema = read_yaml(schema_path)
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self):
        config = self.config.data_ingestion

        create_directories([config.data_ingest_root])

        data_ingestion_config = DataIngestionConfig(
            data_source = Path(config.data_source),
            train_data_path = Path(config.train_data_path),
            test_data_path = Path(config.test_data_path),
        )
        return data_ingestion_config