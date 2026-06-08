from Kidney_Disease_cnn_Classification import logger 
from Kidney_Disease_cnn_Classification.pipeline.stage_01_data_ingestion import DataIngestionTrainPipeline
from Kidney_Disease_cnn_Classification.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline


#STAGE_NAME="Data Ingestion Stage"

'''try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = DataIngestionTrainPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<< \n\nX=======X")
except Exception as e:
    logger.exception(e)
    raise e '''


STAGE_NAME = "Prepare base Model"

try:
    logger.info(f"************")
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<\n\n")
        
except Exception as e:
    logger.exception(e)
    raise e
        
    