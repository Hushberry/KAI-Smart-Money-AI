"""
=========================================================
KAI Smart Money AI

Liquidity Engine

utils.py

Liquidity Detection Utilities

Author: Vincent Chimezirim
=========================================================
"""

from __future__ import annotations



from .constants import (

    EQUAL_TOLERANCE,

)



# ==========================================================
# PRICE DISTANCE
# ==========================================================

def price_distance(
    first: float,
    second: float,
):
    """
    Calculate price difference.
    """

    return abs(

        first - second

    )



# ==========================================================
# EQUAL PRICE CHECK
# ==========================================================

def is_equal_price(
    first: float,
    second: float,
    tolerance: float = EQUAL_TOLERANCE,
):
    """
    Check if two prices are equal within tolerance.
    """

    return (

        price_distance(

            first,

            second,

        )

        <=

        tolerance

    )



# ==========================================================
# GET HIGH PRICE
# ==========================================================

def get_high(
    swing,
):
    """
    Return swing high price.
    """

    return float(

        swing.price

    )



# ==========================================================
# GET LOW PRICE
# ==========================================================

def get_low(
    swing,
):
    """
    Return swing low price.
    """

    return float(

        swing.price

    )



# ==========================================================
# FIND EQUAL HIGHS
# ==========================================================

def find_equal_highs(
    swing_highs,
):
    """
    Detect equal high liquidity pools.

    Example:

    High
    |
    |____
         |
         |____

    """

    pools = []



    for i in range(

        len(swing_highs)

    ):


        current = swing_highs[i]



        for j in range(

            i + 1,

            len(swing_highs)

        ):


            target = swing_highs[j]



            if is_equal_price(

                current.price,

                target.price,

            ):


                pools.append(

                    (

                        current,

                        target,

                    )

                )



    return pools



# ==========================================================
# FIND EQUAL LOWS
# ==========================================================

def find_equal_lows(
    swing_lows,
):
    """
    Detect equal low liquidity pools.
    """

    pools = []



    for i in range(

        len(swing_lows)

    ):


        current = swing_lows[i]



        for j in range(

            i + 1,

            len(swing_lows)

        ):


            target = swing_lows[j]



            if is_equal_price(

                current.price,

                target.price,

            ):


                pools.append(

                    (

                        current,

                        target,

                    )

                )



    return pools



# ==========================================================
# LIQUIDITY DIRECTION
# ==========================================================

def liquidity_direction(
    swing_type,
):
    """
    Convert swing type into liquidity side.
    """

    if swing_type == "swing_high":

        return "buy_side_liquidity"



    if swing_type == "swing_low":

        return "sell_side_liquidity"



    return None



# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "price_distance",

    "is_equal_price",

    "get_high",

    "get_low",

    "find_equal_highs",

    "find_equal_lows",

    "liquidity_direction",

]