import logging


def setup_logger():
    logger = logging.getLogger("my_app_logger")
    logger.setLevel(logging.DEBUG)  


    fh = logging.FileHandler("error.log")  
    fh.setLevel(logging.ERROR) 

    
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)


    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger


logger = setup_logger()
logger.error("This is an error message")