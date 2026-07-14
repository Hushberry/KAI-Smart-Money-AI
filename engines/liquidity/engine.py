"""
=========================================================
KAI Smart Money AI

Liquidity Engine

engine.py

Main Liquidity Analysis Interface

Author: Vincent Chimezirim
=========================================================
"""

from __future__ import annotations



from .detector import (

    detect_liquidity,

)



from .validator import (

    validate_liquidity_state,

)



from .scorer import (

    score_liquidity_state,

)



from .lifecycle import (

    update_liquidity_state,

    active_liquidity,

)



from .statistics import (

    liquidity_summary,

)



# ==========================================================
# LIQUIDITY ENGINE
# ==========================================================

class LiquidityEngine:
    """
    Professional Liquidity Engine.

    Responsibilities:

    - Buy Side Liquidity
    - Sell Side Liquidity
    - Equal Highs
    - Equal Lows
    - Liquidity Pools
    - Liquidity Sweeps
    - Liquidity Strength
    """



    def __init__(self):

        self.name = (

            "KAI Institutional "

            "Liquidity Engine"

        )


        self.version = "1.0"



    # ======================================================
    # DETECT
    # ======================================================

    def detect(
        self,
        swing_data,
    ):
        """
        Detect liquidity pools.
        """

        return detect_liquidity(

            swing_data

        )



    # ======================================================
    # VALIDATE
    # ======================================================

    def validate(
        self,
        state,
    ):
        """
        Validate liquidity zones.
        """

        return validate_liquidity_state(

            state

        )



    # ======================================================
    # SCORE
    # ======================================================

    def score(
        self,
        state,
    ):
        """
        Score liquidity strength.
        """

        return score_liquidity_state(

            state

        )



    # ======================================================
    # UPDATE
    # ======================================================

    def update(
        self,
        state,
        candles,
    ):
        """
        Update liquidity lifecycle.
        """

        return update_liquidity_state(

            state,

            candles

        )



    # ======================================================
    # ACTIVE
    # ======================================================

    def active(
        self,
        state,
    ):
        """
        Return active liquidity.
        """

        return active_liquidity(

            state

        )



    # ======================================================
    # SUMMARY
    # ======================================================

    def summary(
        self,
        state,
    ):
        """
        Generate liquidity report.
        """

        return liquidity_summary(

            state

        )



    # ======================================================
    # COMPLETE ANALYSIS
    # ======================================================

    def analyze(
        self,
        candles,
        swing_data=None,
    ):
        """
        Complete liquidity pipeline.
        """


        if swing_data is None:

            raise ValueError(

                "Swing data required "

                "for liquidity analysis"

            )



        state = self.detect(

            swing_data

        )


        state = self.validate(

            state

        )


        state = self.score(

            state

        )


        state = self.update(

            state,

            candles

        )


        return {


            "state":

                state,



            "zones":

                state.all_zones(),



            "sweeps":

                state.sweeps,



            "summary":

                self.summary(

                    state

                ),

        }



# ==========================================================
# EXPORT
# ==========================================================

__all__ = [

    "LiquidityEngine",

]