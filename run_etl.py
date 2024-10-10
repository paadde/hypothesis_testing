import sys
from src.main import main
import logging

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.info(f'An error occurred: {e}')
        sys.exit(1)
