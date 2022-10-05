import logging
import inspect


def CustomLogger(LogLevel=logging.DEBUG):
    loggerName = inspect.stack()[1][3]  # inspect.stack helps to get method/class name from where the loggerName is called

    logger = logging.getLogger(loggerName)  # LoggerName will get class/method name, so it can be used in logs
    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler('automate.log', mode='a') # ("{0}.log".format(loggerName), mode='w')
    fileHandler.setLevel(LogLevel)  # LogLevel will be given by user / setLevel of Handler overwrites setLevel of logger

    formatter = logging.Formatter("%(asctime)s: %(name)s: %(levelname)s: %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")

    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger