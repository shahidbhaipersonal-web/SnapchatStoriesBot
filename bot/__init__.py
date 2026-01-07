import logging
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class ENV_VARS(object):
    API_ID = int(os.environ.get("API_ID", "39699422"))
    API_HASH = os.environ.get("API_HASH", "c51ebf3a2e32beeb7d68605f155056a8")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8547247234:AAH1_eh2ooTRihCAYDCD62mWI8cH_tUck0I")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "snap122bot")
    #AUTH_USER = int(os.environ.get("AUTH_USER", 5071059420))


Config = ENV_VARS

handler = Config.BOT_USERNAME


class CMD(object):
    START = ["start", f"start@{handler}"]
