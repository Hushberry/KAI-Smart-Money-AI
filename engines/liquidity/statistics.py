"""
=========================================================
KAI Smart Money AI

Liquidity Engine

statistics.py

Liquidity Analytics & Reporting

Author: Vincent Chimezirim
=========================================================
"""

from __future__ import annotations



from .constants import (

    BUY_SIDE,

    SELL_SIDE,

)



# ==========================================================
# TOTAL ZONES
# ==========================================================

def total_liquidity(
    state,
):
    """
    Count liquidity zones.
    """

    return len(

        state.all_zones()

    )



# ==========================================================
# BUY SIDE COUNT
# ==========================================================

def buy_side_count(
    state,
):
    """
    Count BSL zones.
    """

    return len(

        [

            z

            for z in state.buy_side

        ]

    )



# ==========================================================
# SELL SIDE COUNT
# ==========================================================

def sell_side_count(
    state,
):
    """
    Count SSL zones.
    """

    return len(

        [

            z

            for z in state.sell_side

        ]

    )



# ==========================================================
# EQUAL LIQUIDITY COUNT
# ==========================================================

def equal_liquidity_count(
    state,
):
    """
    Count equal highs/lows.
    """

    return len(

        [

            z

            for z in state.all_zones()

            if z.equal

        ]

    )



# ==========================================================
# SWEEP COUNT
# ==========================================================

def sweep_count(
    state,
):
    """
    Count liquidity raids.
    """

    return len(

        state.sweeps

    )



# ==========================================================
# ACTIVE COUNT
# ==========================================================

def active_liquidity_count(
    state,
):
    """
    Count active liquidity.
    """

    return len(

        [

            z

            for z in state.all_zones()

            if z.active

        ]

    )



# ==========================================================
# SWEPT COUNT
# ==========================================================

def swept_liquidity_count(
    state,
):
    """
    Count consumed liquidity.
    """

    return len(

        [

            z

            for z in state.all_zones()

            if z.swept

        ]

    )



# ==========================================================
# AVERAGE SCORE
# ==========================================================

def average_liquidity_score(
    state,
):
    """
    Calculate average liquidity strength.
    """

    zones = state.all_zones()



    if not zones:

        return 0



    return round(

        sum(

            z.score

            for z in zones

        )

        /

        len(zones),

        2

    )



# ==========================================================
# STRONGEST ZONE
# ==========================================================

def strongest_liquidity(
    state,
):
    """
    Return strongest liquidity pool.
    """

    zones = state.all_zones()



    if not zones:

        return None



    return max(

        zones,

        key=lambda x: x.score

    )



# ==========================================================
# LIQUIDITY REPORT
# ==========================================================

def liquidity_summary(
    state,
):
    """
    Generate liquidity report.
    """

    return {


        "total":

            total_liquidity(

                state

            ),



        "buy_side":

            buy_side_count(

                state

            ),



        "sell_side":

            sell_side_count(

                state

            ),



        "equal_levels":

            equal_liquidity_count(

                state

            ),



        "sweeps":

            sweep_count(

                state

            ),



        "active":

            active_liquidity_count(

                state

            ),



        "swept":

            swept_liquidity_count(

                state

            ),



        "average_score":

            average_liquidity_score(

                state

            ),



        "grade":

            state.grade,



        "strongest":

            strongest_liquidity(

                state

            ),

    }



# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "total_liquidity",

    "buy_side_count",

    "sell_side_count",

    "equal_liquidity_count",

    "sweep_count",

    "active_liquidity_count",

    "swept_liquidity_count",

    "average_liquidity_score",

    "strongest_liquidity",

    "liquidity_summary",

]