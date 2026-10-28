#Task 1

import logging

logger = logging.getLogger(__name__+"_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        logger.log(logging.INFO, f"Function: {func.__name__}")
        logger.log(logging.INFO, f"Positional Parameters: {args if args else 'none'}")
        logger.log(logging.INFO, f"Keyword Parameters: {kwargs if kwargs else 'none'}")
        logger.log(logging.INFO, f"Return: {value}")
        return value
    return wrapper


@logger_decorator
def something():
    print("hi")

@logger_decorator
def anyNum(*args):
    return True

@logger_decorator
def anyAny(**kwargs):
    return logger_decorator

something()
anyNum(2, "done")
anyAny(color="red")