from ids import logger
from ids.exception import CustomException
import sys
from ids.pipeline.etl_pipeline import etl_pipeline


if __name__ == "__main__":
    try:
        logger.info("Starting pipeline")
        etl_pipeline()
        logger.info("Pipeline completed successfully")
    except CustomException as e:
        logger.error(f"Pipeline failed with error: {e}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Pipeline failed with error: {e}")
        sys.exit(1)