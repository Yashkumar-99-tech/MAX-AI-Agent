import time

from core.logger import logger

from config import OWNER
from config import VERSION
from config import LOADING_MODULES
from config import AI_NAME


class Startup:

    def __init__(self):

        self.owner = OWNER

        self.version = VERSION

        self.ai_name = AI_NAME

    def banner(self):

        print("\n" + "=" * 60)

        print(f"               🤖 {self.ai_name} AI ASSISTANT")

        print("=" * 60)

        print(f"Owner   : {self.owner}")

        print(f"Version : {self.version}")

        print("Status  : Initializing...")

        print("=" * 60)

    def loading(self):

        for module in LOADING_MODULES:

            print(module + "...")

            logger.info(module)

            time.sleep(0.3)

        print(f"\n✅ {self.ai_name} AI Ready!\n")

        logger.info(f"{self.ai_name} AI Started Successfully")


startup = Startup()