import logging

import numpy as np

from fancymath.fancy_math import fact
from fancymath.fancy_trig import fancy_sin
from fancymath.utils import configure_logging


if __name__ == '__main__':
    configure_logging()
    logger = logging.getLogger(__name__)
    logger.info("Welcome to Fancy Math!")
    logger.info(f'The factorial of 4 is {fact(4)}')
    logger.info(f'The sine of 1/2 pi is {fancy_sin(np.pi / 2)}')
    logger.info("Thanks for spending time with us today.")