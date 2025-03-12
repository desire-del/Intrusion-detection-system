from ids.config.configuration import ConfigurationManager
from ids.steps.data_ingestion import load_data_step, split_data_step
from zenml import pipeline

@pipeline
def etl_pipeline():
        
    try:
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        
        data = load_data_step(data_ingestion_config)
        return split_data_step(data, data_ingestion_config)

    except Exception as e:
        raise e