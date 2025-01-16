import logging
logger = logging.getLogger(__name__)


def fact(i):
    logger.debug(f"fact({i})")
    if i < 0:
        raise ValueError("i must be greater than 0")
    if i <= 1:
        return 1
    else:
        return i * fact(i - 1)

def is_even(number):
    return number % 2 == 0


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logger.info("Starting tests.")
    assert fact(1) == 1
    assert fact(4) == 24
    assert fact(0) == 1
    logger.info("Tests passed.")