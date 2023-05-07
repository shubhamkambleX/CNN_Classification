from cnnClassifier.pipline.stage_01_data_ingestion import DataIngestionTrainingPipline
from cnnClassifier.pipline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipline
from cnnClassifier import logger


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} Started <<<<<<")
    data_ingestion = DataIngestionTrainingPipline()
    data_ingestion.main()
    logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\n================x")
except Exception as e:
    logger.exception(e)
    raise e 


STAGE_NAME = "Prepare Base Model Stage"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} Started <<<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipline()
    prepare_base_model.main()
    logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\n================x")
except Exception as e:
    logger.exception(e)
    raise e 