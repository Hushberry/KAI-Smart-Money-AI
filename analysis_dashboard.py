import config
from datetime import datetime
from terminal_colors import Color

LABEL = config.LABEL_WIDTH


def show_analysis(
    symbol,
    timeframe,
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
):
    
    LINE = config.LINE_WIDTH

    print("=" * LINE)
    print(f"{'KAI BOT ANALYSIS':^{LINE}}")
    print("=" * LINE)
    print()

    # -------------------------------------------------
    # SYMBOL
    # -------------------------------------------------

    print("\nSymbol")
    print("-" * LINE)

    print(f"{'Symbol':<{LABEL}} : {symbol}")
    print(f"{'Timeframe':<{LABEL}} : {timeframe}")
    print(f"{'Time':<{LABEL}} : {datetime.fromtimestamp(latest_candle['time'])}")

    
    # -------------------------------------------------
    # PRICE
    # -------------------------------------------------

    print("\n" + "=" * LINE)
    print("Price Information")
    print("-" * LINE)

    print(f"{'Open':<{LABEL}} : {latest_candle['open']:.5f}")
    print(f"{'High':<{LABEL}} : {latest_candle['high']:.5f}")
    print(f"{'Low':<{LABEL}} : {latest_candle['low']:.5f}")
    print(f"{'Close':<{LABEL}} : {latest_candle['close']:.5f}")
    print(f"{'Volume':<{LABEL}} : {latest_candle['tick_volume']:.0f}")
    
    
    # -------------------------------------------------
    # TREND
    # -------------------------------------------------

    print("\n" + "=" * LINE)
    print("Trend Analysis")
    print("-" * LINE)

    print(f"{'MA 50':<{LABEL}} : {ma50:.5f}")
    print(f"{'MA 200':<{LABEL}} : {ma200:.5f}")
    print(f"{'Trend':<{LABEL}} : {trend}")
    print(f"{'Structure':<{LABEL}} : {market_structure}")
    print(f"{'Pattern':<{LABEL}} : {pattern}")
    

    # -------------------------------------------------
    # SUPPORT / RESISTANCE
    # -------------------------------------------------

    print("\n" + "=" * LINE)
    print("Support / Resistance")
    print("-" * LINE)

    print(f"{'Support':<{LABEL}} : {support:.5f}")
    print(f"{'Resistance':<{LABEL}} : {resistance:.5f}")


    # -------------------------------------------------
    # MTF
    # -------------------------------------------------

    print("\n" + "=" * LINE)
    print("Multi-Timeframe")
    print("-" * LINE)

    print(f"{'H1 Trend':<{LABEL}} : {h1_trend}")
    print(f"{'H4 Trend':<{LABEL}} : {h4_trend}")
    print(f"{'Confirmation':<{LABEL}} : {mtf_confirmation}")


    # -------------------------------------------------
    # AI CONFIDENCE
    # -------------------------------------------------

    print("\n" + "=" * LINE)
    print("Ai Confidence")
    print("-" * LINE)

    print(f"{'Confidence':<{LABEL}} : {rating}")
    print()

    if "BUY" in signal:
        decision = Color.GREEN + signal + Color.RESET

    elif "SELL" in signal:
        decision = Color.RED + signal + Color.RESET

    else:
        decision = Color.YELLOW + signal + Color.RESET

        print(f"{'Decision':<18}: {decision}")
        print("=" * LINE)
        print()

    print("Reason")
    print("-" * config.LINE_WIDTH)

    if signal == "📈 BUY":

       print("✓ Trend is bullish")
       print("✓ Higher timeframe agrees")
       print("✓ Confidence above threshold")

    elif signal == "📉 SELL":

        print("✓ Trend is bearish")
        print("✓ Higher timeframe agrees")
        print("✓ Confidence above threshold")

    else:

        print("• Market not aligned")
        print("• Waiting for confirmation")