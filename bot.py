import config
import logger
import mt5_connector

print("=" * 50)
print(f"Welcome to {config.BOT_NAME}")
print(f"Version: {config.VERSION}")
print(f"Author: {config.AUTHOR}")
print("=" * 50)

logger.log("KAI_Bot has started.")

mt5_connector.connect_to_mt5()
mt5_connector.get_account_info()