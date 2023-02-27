import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6298975511:AAFoxoJ7v2FSndA9WYPD5TJWbUvBqsskk-A")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOH8Bu3Fjwji0fU4GpMsheHZryPkJNNyBuiooQbHjJE07rbo3k9pTXq4aQYx0qXMkv8qGbbamquTX7o02gLv3xKocqHLg-sEsLLu4JSr_WwbfknpjCOW92QVdAnBj3Iwlh-vhkNq7-_qKJq2meQPqcPsjRQ6gMAbXzsmek9_aHt9boPi3u2mUW3CU2j80K1EN26qnG8oRWp5R59kpK7L2RgQMAkviC31_xbIWfIr-BFvNyN9z2Gz5E7emczJ9kbAEafuYctpBQ5jm_ICb3IjIqJWHIPvaDLpCcpsvsZy5achcmAygMnv2rAgeYre2sHo7Jg-vun4XdQKnFdhzcRx5KAtHS40=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
