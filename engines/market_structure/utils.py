"""
=========================================================
KAI Smart Money AI

Market Structure Engine

utils.py

Structure Detection Utilities

Author: Vincent Chimezirim
=========================================================
"""

from __future__ import annotations



from .constants import (

    HIGHER_HIGH,

    HIGHER_LOW,

    LOWER_HIGH,

    LOWER_LOW,

)



# ==========================================================
# PRICE COMPARISON
# ==========================================================

def compare_price(
    current: float,
    previous: float,
):
    """
    Compare two prices.
    """

    if current > previous:

        return "higher"



    if current < previous:

        return "lower"



    return "equal"



# ==========================================================
# HIGH CLASSIFICATION
# ==========================================================

def classify_high(
    current_high: float,
    previous_high: float,
):
    """
    Classify swing high.

    HH or LH
    """

    comparison = compare_price(

        current_high,

        previous_high,

    )


    if comparison == "higher":

        return HIGHER_HIGH



    if comparison == "lower":

        return LOWER_HIGH



    return None



# ==========================================================
# LOW CLASSIFICATION
# ==========================================================

def classify_low(
    current_low: float,
    previous_low: float,
):
    """
    Classify swing low.

    HL or LL
    """

    comparison = compare_price(

        current_low,

        previous_low,

    )


    if comparison == "higher":

        return HIGHER_LOW



    if comparison == "lower":

        return LOWER_LOW



    return None



# ==========================================================
# BREAK CHECK
# ==========================================================

def broke_high(
    price: float,
    swing_high: float,
):
    """
    Check bullish break.
    """

    return price > swing_high



def broke_low(
    price: float,
    swing_low: float,
):
    """
    Check bearish break.
    """

    return price < swing_low



# ==========================================================
# TREND DETECTION
# ==========================================================

def determine_trend(
    classifications,
):
    """
    Determine market bias.
    """

    bullish = 0

    bearish = 0



    for item in classifications:


        if item in (

            HIGHER_HIGH,

            HIGHER_LOW,

        ):

            bullish += 1



        elif item in (

            LOWER_HIGH,

            LOWER_LOW,

        ):

            bearish += 1



    if bullish > bearish:

        return "bullish"



    if bearish > bullish:

        return "bearish"



    return "neutral"



# ==========================================================
# EVENT VALIDATION
# ==========================================================

def valid_structure_break(
    current_price,
    reference_price,
    direction,
):
    """
    Validate BOS direction.
    """

    if direction == "bullish":

        return current_price > reference_price



    if direction == "bearish":

        return current_price < reference_price



    return False



# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "compare_price",

    "classify_high",

    "classify_low",

    "broke_high",

    "broke_low",

    "determine_trend",

    "valid_structure_break",

]