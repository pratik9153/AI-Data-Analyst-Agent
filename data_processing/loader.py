import pandas as pd

from utils.exceptions import EmptyDataError
from utils.logger import logger


def load_data(file_path):

    logger.info("Loading dataset")

    df = pd.read_csv(file_path)

    if df.empty:
        raise EmptyDataError(
            "The uploaded dataset is empty."
        )

    logger.info("Dataset loaded successfully")

    return df