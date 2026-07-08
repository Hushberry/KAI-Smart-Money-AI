import config
import logger
import mt5_connector
import dashboard
import MetaTrader5 as mt5
import candle_engine
import trend_engine
import pattern_engine
import support_engine
import signal_engine
import analysis_dashboard
import confirmation_engine
import mtf_engine


# ==========================================
# START BOT
# ==========================================

logger.log("KAI_Bot has started.")

mt5_connector.connect_to_mt5()

account = mt5.account_info()

dashboard.show_header(account)


# ==========================================
# SETTINGS
# ==========================================

SYMBOLS = [
    "XAUUSDm",
    "EURUSDm",
    "GBPUSDm",
    "USDJPYm",
    "USDCHFm",
    "USDCADm",
    "UKOILm",
    "USOILm",
    "BTCUSDm",
    "ETHUSDm",
]

TIMEFRAME = mt5.TIMEFRAME_H1
CANDLE_COUNT = 500


# ==========================================
# MARKET WATCH
# ==========================================

market_data = []

for symbol in SYMBOLS:

    info = mt5.symbol_info(symbol)
    tick = mt5.symbol_info_tick(symbol)

    if info is None or tick is None:
        continue

    # Download candles
    rates = candle_engine.get_historical_candles(
        symbol,
        TIMEFRAME,
        CANDLE_COUNT
    )

    if rates is None:
        continue

    # Latest price
    latest_price = rates[-1]["close"]

    # Calculate moving averages
    ma50 = trend_engine.calculate_ma(rates, 50)
    ma200 = trend_engine.calculate_ma(rates, 200)

    # Detect trend
    trend = trend_engine.analyze_trend(
        latest_price,
        ma50,
        ma200
    )

    # Spread
    spread = (tick.ask - tick.bid) / info.point

    # Save row
    market_data.append({
        "symbol": symbol,
        "bid": tick.bid,
        "ask": tick.ask,
        "spread": spread,
        "trend": trend
    })

# Show Market Watch
dashboard.show_market_watch(market_data)

print()


# ==========================================
# AI ANALYSIS
# ==========================================

for symbol in SYMBOLS:

    rates = candle_engine.get_historical_candles(
        symbol,
        TIMEFRAME,
        CANDLE_COUNT
    )

    if rates is None:
        continue

    latest_candle = rates[-1]
    latest_price = latest_candle["close"]

    # -------------------------
    # Trend Analysis
    # -------------------------

    ma50 = trend_engine.calculate_ma(rates, 50)
    ma200 = trend_engine.calculate_ma(rates, 200)

    trend = trend_engine.analyze_trend(
        latest_price,
        ma50,
        ma200
    )

    market_structure = trend_engine.get_market_structure(rates)

    pattern = pattern_engine.analyze_patterns(rates)

    support = support_engine.find_support(rates)
    resistance = support_engine.find_resistance(rates)

    # -------------------------
    # Trade Signal
    # -------------------------

    signal = signal_engine.get_trade_bias(trend)

    # -------------------------
    # Multi-Timeframe
    # -------------------------

    h1_trend = mtf_engine.get_timeframe_trend(
        symbol,
        config.TIMEFRAME
    )

    h4_trend = mtf_engine.get_timeframe_trend(
        symbol,
        config.HIGHER_TIMEFRAME
    )

    mtf_confirmation = mtf_engine.compare_trends(
        h4_trend,
        h1_trend
    )

    # -------------------------
    # AI Confidence
    # -------------------------

    score, rating = confirmation_engine.calculate_trade_score(
        trend,
        pattern,
        market_structure,
        mtf_confirmation,
        signal
    )

    # -------------------------
    # Display Analysis
    # -------------------------

    analysis_dashboard.show_analysis(
        symbol,
        candle_engine.get_timeframe_name(TIMEFRAME),
        latest_candle,
        ma50,
        ma200,
        trend,
        market_structure,
        pattern,
        support,
        resistance,
        h1_trend,
        h4_trend,
        mtf_confirmation,
        score,
        rating,
        signal,
    )