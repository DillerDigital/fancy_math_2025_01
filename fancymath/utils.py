import logging


def configure_logging():
    root_logger = logging.getLogger()
    fmt = '%(asctime)s %(levelname)8s:%(name)s: %(funcName)s(): %(message)s'
    formatter = logging.Formatter(fmt)
    sh = logging.StreamHandler()
    sh.setFormatter(formatter)
    sh.setLevel(logging.INFO)
    
    fh = logging.FileHandler('fancy_math.log')
    fh.setFormatter(formatter)
    fh.setLevel(logging.DEBUG)
    
    root_logger.addHandler(sh)
    root_logger.addHandler(fh)
    root_logger.setLevel(logging.DEBUG)