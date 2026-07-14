"""
=========================================================
KAI Smart Money AI

Liquidity Engine

detector.py

Liquidity Pool Detection

Author: Vincent Chimezirim
=========================================================
"""

from __future__ import annotations



from .models import (

    LiquidityZone,

    LiquidityState,

)



from .constants import (

    BUY_SIDE,

    SELL_SIDE,

    EQUAL_HIGH,

    EQUAL_LOW,

)



from .utils import (

    find_equal_highs,

    find_equal_lows,

)



# ==========================================================
# DETECT BUY SIDE LIQUIDITY
# ==========================================================

def detect_buy_side_liquidity(
    swing_highs,
):
    """
    Detect liquidity above swing highs.

    BSL = stops above highs.
    """

    zones = []



    for swing in swing_highs:


        zone = LiquidityZone(

            index=swing.index,

            timestamp=swing.timestamp,

            price=swing.price,

            high=swing.price,

            low=swing.price,

            liquidity_type=BUY_SIDE,

            touches=1,

        )


        zone.add_reason(

            "Liquidity above swing high"

        )


        zones.append(

            zone

        )



    return zones



# ==========================================================
# DETECT SELL SIDE LIQUIDITY
# ==========================================================

def detect_sell_side_liquidity(
    swing_lows,
):
    """
    Detect liquidity below swing lows.

    SSL = stops below lows.
    """

    zones = []



    for swing in swing_lows:


        zone = LiquidityZone(

            index=swing.index,

            timestamp=swing.timestamp,

            price=swing.price,

            high=swing.price,

            low=swing.price,

            liquidity_type=SELL_SIDE,

            touches=1,

        )


        zone.add_reason(

            "Liquidity below swing low"

        )


        zones.append(

            zone

        )



    return zones



# ==========================================================
# ADD EQUAL HIGH LIQUIDITY
# ==========================================================

def detect_equal_high_liquidity(
    swing_highs,
):
    """
    Detect equal high pools.
    """

    zones = []



    pools = find_equal_highs(

        swing_highs

    )



    for first, second in pools:


        zone = LiquidityZone(

            index=second.index,

            timestamp=second.timestamp,

            price=second.price,

            high=second.price,

            low=second.price,

            liquidity_type=BUY_SIDE,

            touches=2,

            equal=True,

        )


        zone.add_reason(

            "Equal highs liquidity pool"

        )


        zones.append(

            zone

        )



    return zones



# ==========================================================
# ADD EQUAL LOW LIQUIDITY
# ==========================================================

def detect_equal_low_liquidity(
    swing_lows,
):
    """
    Detect equal low pools.
    """

    zones = []



    pools = find_equal_lows(

        swing_lows

    )



    for first, second in pools:


        zone = LiquidityZone(

            index=second.index,

            timestamp=second.timestamp,

            price=second.price,

            high=second.price,

            low=second.price,

            liquidity_type=SELL_SIDE,

            touches=2,

            equal=True,

        )


        zone.add_reason(

            "Equal lows liquidity pool"

        )


        zones.append(

            zone

        )



    return zones



# ==========================================================
# MASTER DETECTOR
# ==========================================================

def detect_liquidity(
    swing_data,
):
    """
    Complete liquidity detection.
    """

    state = LiquidityState()



    highs = swing_data.highs


    lows = swing_data.lows



    state.buy_side.extend(

        detect_buy_side_liquidity(

            highs

        )

    )


    state.sell_side.extend(

        detect_sell_side_liquidity(

            lows

        )

    )



    state.buy_side.extend(

        detect_equal_high_liquidity(

            highs

        )

    )


    state.sell_side.extend(

        detect_equal_low_liquidity(

            lows

        )

    )



    return state



# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "detect_liquidity",

    "detect_buy_side_liquidity",

    "detect_sell_side_liquidity",

    "detect_equal_high_liquidity",

    "detect_equal_low_liquidity",

]