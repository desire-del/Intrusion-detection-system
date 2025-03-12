from ids.config.configuration import DataIngestionConfig
from ids.exception import CustomException
from ids import logger
from sklearn.model_selection import train_test_split
import pandas as pd
import sys
from zenml import step

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config 

    def load_data(self):
        try:
            logger.info(f"Loading data from {self.config.data_source}")
            data = pd.read_csv(self.config.data_source, low_memory=False)
            logger.info(f"Data loaded successfully")
            return data
        except Exception as e:
            raise CustomException(e, sys)     
    
    def split_data(self, data, seed: int = 42):
        try:
            logger.info(f"Splitting data into train and test datasets")

            train, test = train_test_split(data, test_size=0.2, random_state=seed)
            train.to_csv(self.config.train_data_path, index=False, header=True)
            test.to_csv(self.config.test_data_path, index=False, header=True)
            logger.info(f"Data split successfully")
            return (self.config.train_data_path, self.config.test_data_path)
        except Exception as e:
            raise CustomException(e, sys)

@step
def load_data_step(config: DataIngestionConfig):
    data_ingestion = DataIngestion(config)
    return data_ingestion.load_data()

@step
def split_data_step(data, config: DataIngestionConfig):
    data_ingestion = DataIngestion(config)
    return data_ingestion.split_data(data)