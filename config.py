# ==================================
# TradingBot Configuration File
# ==================================
import MetaTrader5 as mt5

BOT_NAME = "KAI_Bot"
VERSION = "1.0"
AUTHOR = "Vincent Chimezirim"

SYMBOLS = ["XAUUSDm", "EURUSDm", "GBPUSDm"]
TIMEFRAMES = ["M1", "M5", "M15", "H1", "H4", "D1"]
RISK_PER_TRADE = 0.07

LINE_WIDTH = 100
LABEL_WIDTH = 18

TIMEFRAME = mt5.TIMEFRAME_H1
HIGHER_TIMEFRAME = mt5.TIMEFRAME_H4
CANDLE_COUNT = 500

FAST_MA = 50
SLOW_MA = 200

