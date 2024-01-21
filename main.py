from logging import config, getLogger
from json import load
import log_test

with open("./config/logging.json", "r", encoding="utf-8") as f:
    config.dictConfig(load(f))


logger = getLogger(__name__)
logger.info("This is a info message.")
logger.debug("test")


#別ファイルlog_test.pyのログを確認
log_test.do_something()



