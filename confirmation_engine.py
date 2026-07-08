"""
confirmation_engine.py

Confirms trade setups using multiple indicators.
"""

import numpy as np

def calculate_trade_score(
        trend,
        pattern,
        market_structure,
        mtf_confirmation,
        signal,
):
    """
    Calculates a simple confirmation score.
    """
    score = 0

    if trend == ["📈Uptrend", "📉 Downtrend"]:
        score += 1

    if market_structure in [
        "Higher Highs",
        "Lower Highs",
    ]:
        score += 1

    bullish = [
        "Hammer",
        "Bullish Engulfing",
    ]

    bearish = [
        "Shooting Star",
        "Bearish Engulfing",
    ]

    if pattern in bullish + bearish:
        score += 1

    if mtf_confirmation == "✅ Confirmed":
        score += 1

    if signal in [
        "📈 BUY",
        "📉 SELL",
    ]:
        score += 1
    

    stars =  "⭐" * score + "☆" * (5 - score)

    rating = f"{stars} ({score}/5)"
    
    return score, rating