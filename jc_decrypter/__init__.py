import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from jc_decrypter.utils import logger


# SET LOGGER
logger.configure_logger()
