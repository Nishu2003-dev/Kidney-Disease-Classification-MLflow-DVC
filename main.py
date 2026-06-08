from Kidney_Disease_cnn_Classification import logger 
from Kidney_Disease_cnn_Classification.pipeline.stage_01_data_ingestion import DataIngestionTrainPipeline


STAGE_NAME="Data Ingestion Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = DataIngestionTrainPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<< \n\nX=======X")
except Exception as e:
    logger.exception(e)
    raise e


    