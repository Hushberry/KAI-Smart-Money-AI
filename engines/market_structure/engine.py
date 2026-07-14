"""
=========================================================
KAI Smart Money AI

Market Structure Engine

engine.py

Main Structure Analysis Interface

Author: Vincent Chimezirim
=========================================================
"""

from __future__ import annotations



from .detector import (

    detect_structure,

)



from .validator import (

    validate_structure_state,

)



from .scorer import (

    calculate_structure_score,

    score_structure_events,

)



from .lifecycle import (

    update_structure_state,

    active_structure_events,

)



from .statistics import (

    structure_summary,

)



# ==========================================================
# MARKET STRUCTURE ENGINE
# ==========================================================

class MarketStructureEngine:
    """
    Professional Market Structure Engine.

    Responsibilities:

    - HH / HL / LH / LL detection
    - BOS detection
    - CHoCH detection
    - Trend analysis
    - Structure confidence
    - Lifecycle tracking
    """



    def __init__(self):

        self.name = (

            "KAI Institutional "

            "Market Structure Engine"

        )


        self.version = "1.0"



    # ======================================================
    # DETECT
    # ======================================================

    def detect(
        self,
        candles,
        swing_data,
    ):
        """
        Detect market structure.
        """

        return detect_structure(

            candles,

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
        Validate structure events.
        """

        validate_structure_state(

            state

        )


        return state



    # ======================================================
    # SCORE
    # ======================================================

    def score(
        self,
        state,
    ):
        """
        Calculate structure confidence.
        """

        score_structure_events(

            state.events

        )


        calculate_structure_score(

            state

        )


        return state



    # ======================================================
    # UPDATE
    # ======================================================

    def update(
        self,
        state,
        candles,
    ):
        """
        Update structure lifecycle.
        """

        return update_structure_state(

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
        Return active structure.
        """

        return active_structure_events(

            state.events

        )



    # ======================================================
    # SUMMARY
    # ======================================================

    def summary(
        self,
        state,
    ):
        """
        Generate structure report.
        """

        return structure_summary(

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
        Complete market structure pipeline.
        """


        if swing_data is None:

            raise ValueError(

                "Swing data required "

                "for market structure analysis"

            )



        state = self.detect(

            candles,

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



            "trend":

                state.trend,



            "events":

                state.events,



            "summary":

                self.summary(

                    state

                ),

        }



# ==========================================================
# EXPORT
# ==========================================================

__all__ = [

    "MarketStructureEngine",

]