import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5951049324:AAFNx8hkTDyO3G1JgxiNv5gVPXOQHf4l4q0")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1AZWarzYBu6na632lfTbaKcYVJkGvJWJc6Ggn-UxNJ939UpFMWXzcHaGqzdqYquGZMjv_6fYz0U5999-gxnzcOTcIqhKVlmwFYwmaBMXIw-xiYIvfolI7nSGIyB56Le21MA6YtRxpEgOy7qMlWsKIlKd0WR7w4gc74hOr_IviDUOK-tAQV7GZWAvvJWQ9W_HU83uVRmxx9V_C3whrWNqhxftrFbzMHRTTpPaFPH0px8S89aBPI_fCPgbU4NzlSUd0BiSuPvIDLZEKF6qaY3mzF66A_kdcQ7Tv2MmjSsrw4cRQp_P_uCp5bcGlLm2Ffmt3mcKXCkxuOhwZwWkmQn8aQlpPMaJylfw=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "TheKillProMusicBot")
    SUPPORT = os.environ.get("SUPPORT", "TheKillPro_Chat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "ThekillPro") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://te.legra.ph/file/791941c4db0ba8d00e10d.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://te.legra.ph/file/791941c4db0ba8d00e10d.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5840309156")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
