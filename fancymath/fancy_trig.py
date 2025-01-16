import logging
import numpy as np

logger = logging.getLogger(__name__)


def fancy_sin(x):
    logger.debug(f"sin({x})")
    return np.sin(x)

def gauss_sum(n):
    return ((n + 1) * n) / 2