"""
=========================================================
KAI Smart Money AI

Market Structure Engine

scorer.py

Structure Confidence Scoring

Author: Vincent Chimezirim
=========================================================
"""

from __future__ import annotations



from .models import (

    StructureEvent,

    MarketStructureState,

)



from .constants import (

    BOS,

    CHOCH,

    BULLISH,

    BEARISH,

)



# ==========================================================
# EVENT TYPE SCORE
# ==========================================================

def score_event_type(
    event: StructureEvent,
):
    """
    Score BOS and CHoCH importance.
    """

    if event.event_type == CHOCH:

        return 40



    if event.event_type == BOS:

        return 30



    return 0



# ==========================================================
# CONFIRMATION SCORE
# ==========================================================

def score_confirmation(
    event: StructureEvent,
):
    """
    Confirmed event bonus.
    """

    if event.confirmed:

        return 20



    return 0



# ==========================================================
# DIRECTION SCORE
# ==========================================================

def score_direction(
    event: StructureEvent,
):
    """
    Direction confidence.
    """

    if event.direction in (

        BULLISH,

        BEARISH,

    ):

        return 20



    return 0



# ==========================================================
# EVENT SCORE
# ==========================================================

def calculate_event_score(
    event: StructureEvent,
):
    """
    Calculate structure event quality.
    """

    score = (

        score_event_type(

            event

        )

        +

        score_confirmation(

            event

        )

        +

        score_direction(

            event

        )

    )


    event.score = min(

        score,

        100

    )


    event.grade = structure_grade(

        event.score

    )


    return event.score



# ==========================================================
# GRADE
# ==========================================================

def structure_grade(
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
# STATE SCORE
# ==========================================================

def calculate_structure_score(
    state: MarketStructureState,
):
    """
    Calculate market structure confidence.
    """

    if not state.events:

        state.score = 0

        state.grade = "D"

        return 0



    scores = []



    for event in state.events:


        scores.append(

            calculate_event_score(

                event

            )

        )



    state.score = round(

        sum(scores)

        /

        len(scores),

        2

    )


    state.grade = structure_grade(

        state.score

    )



    return state.score



# ==========================================================
# SCORE ALL EVENTS
# ==========================================================

def score_structure_events(
    events,
):
    """
    Score structure events.
    """

    for event in events:

        calculate_event_score(

            event

        )



    return sorted(

        events,

        key=lambda x: x.score,

        reverse=True

    )



# ==========================================================
# BREAKDOWN
# ==========================================================

def structure_score_breakdown(
    state: MarketStructureState,
):
    """
    Explain structure score.
    """

    return {

        "trend":

            state.trend,


        "events":

            len(

                state.events

            ),


        "score":

            state.score,


        "grade":

            state.grade,

    }



# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "calculate_event_score",

    "calculate_structure_score",

    "score_structure_events",

    "structure_grade",

    "structure_score_breakdown",

]