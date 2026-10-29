import os
import logging


class Logger:

    def __init__(self):

        os.makedirs("logs", exist_ok=True)

        self.logger = logging.getLogger("MAX_AI")

        self.logger.setLevel(logging.INFO)

        if not self.logger.handlers:

            formatter = logging.Formatter(

                "%(asctime)s | %(levelname)s | %(message)s",

                "%d-%m-%Y %H:%M:%S"

            )

            file_handler = logging.FileHandler(

                "logs/app.log",

                encoding="utf-8"

            )

            file_handler.setFormatter(formatter)

            console_handler = logging.StreamHandler()

            console_handler.setFormatter(formatter)

            self.logger.addHandler(file_handler)

            self.logger.addHandler(console_handler)

    # ------------------------

    def info(self, message):

        self.logger.info(message)

    # ------------------------

    def warning(self, message):

        self.logger.warning(message)

    # ------------------------

    def error(self, message):

        self.logger.error(message)

    # ------------------------

    def user(self, message):

        self.logger.info(f"USER : {message}")

    # ------------------------

    def ai(self, message):

        self.logger.info(f"MAX  : {message}")


logger = Logger()