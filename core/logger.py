import logging
import logging.handlers


class LoggerSetup:
    def __init__(self) -> None:
        self.logger = logging.getLogger("")
        self.setup_logging()

    def setup_logging(self):
        LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

        # Конфигурация форматирования логера
        formatter = logging.Formatter(LOG_FORMAT)

        # Конфигурация обработчика логера
        console = logging.StreamHandler()
        console.setFormatter(formatter)

        # Конфигурация TimeRotatingFileHandler
        log_file = f"core/logs/fastapi-efk.log"
        file = logging.handlers.TimedRotatingFileHandler(filename=log_file, when="midnight", backupCount=5)
        file.setFormatter(formatter)

        # Добавление обработчика
        self.logger.addHandler(console)
        self.logger.addHandler(file)
