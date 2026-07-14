"""
=========================================================
KAI Smart Money AI

Liquidity Engine

scorer.py

Liquidity Strength Scoring

Author: Vincent Chimezirim
=========================================================
"""

from __future__ import annotations



from .models import (

    LiquidityZone,

    LiquidityState,

)



from .constants import (

    EQUAL_HIGH,

    EQUAL_LOW,

)



# ==========================================================
# TOUCH SCORE
# ==========================================================

def score_touches(
    zone: LiquidityZone,
):
    """
    More touches = stronger liquidity.
    """

    if zone.touches >= 3:

        return 30



    if zone.touches == 2:

        return 20



    return 10



# ==========================================================
# EQUAL LEVEL SCORE
# ==========================================================

def score_equal(
    zone: LiquidityZone,
):
    """
    Equal highs/lows bonus.
    """

    if zone.equal:

        return 30



    return 0



# ==========================================================
# AGE SCORE
# ==========================================================

def score_age(
    zone: LiquidityZone,
):
    """
    Older untouched liquidity is valuable.
    """

    if zone.swept:

        return 0



    return 20



# ==========================================================
# ACTIVE SCORE
# ==========================================================

def score_active(
    zone: LiquidityZone,
):
    """
    Active liquidity bonus.
    """

    if zone.active:

        return 20



    return 0



# ==========================================================
# CALCULATE SCORE
# ==========================================================

def calculate_liquidity_score(
    zone: LiquidityZone,
):
    """
    Calculate liquidity quality.
    """

    score = (

        score_touches(

            zone

        )

        +

        score_equal(

            zone

        )

        +

        score_age(

            zone

        )

        +

        score_active(

            zone

        )

    )


    zone.score = min(

        score,

        100

    )


    zone.grade = liquidity_grade(

        zone.score

    )


    return zone.score



# ==========================================================
# GRADE
# ==========================================================

def liquidity_grade(
    score,
):
    """
    Convert score to grade.
    """

    if score >= 90:

        return "A+"



    if score >= 80:

        return "A"



    if score >= 70:

        return "B"



    if score >= 60:

        return "C"



    return "D"



# ==========================================================
# SCORE ZONES
# ==========================================================

def score_liquidity_zones(
    zones,
):
    """
    Score multiple zones.
    """

    for zone in zones:

        calculate_liquidity_score(

            zone

        )



    return sorted(

        zones,

        key=lambda x: x.score,

        reverse=True

    )



# ==========================================================
# SCORE STATE
# ==========================================================

def score_liquidity_state(
    state: LiquidityState,
):
    """
    Score complete liquidity.
    """

    all_zones = state.all_zones()



    score_liquidity_zones(

        all_zones

    )



    if all_zones:


        state.total_score = round(

            sum(

                z.score

                for z in all_zones

            )

            /

            len(all_zones),

            2

        )


    state.grade = liquidity_grade(

        state.total_score

    )



    return state



# ==========================================================
# BREAKDOWN
# ==========================================================

def liquidity_score_breakdown(
    zone: LiquidityZone,
):
    """
    Explain liquidity score.
    """

    return {

        "price":

            zone.price,


        "type":

            zone.liquidity_type,


        "touches":

            zone.touches,


        "equal":

            zone.equal,


        "score":

            zone.score,


        "grade":

            zone.grade,

    }



# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "calculate_liquidity_score",

    "score_liquidity_zones",

    "score_liquidity_state",

    "liquidity_grade",

    "liquidity_score_breakdown",

]