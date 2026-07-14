"""
=========================================================
KAI Smart Money AI

Market Structure Engine

statistics.py

Structure Analytics & Reporting

Author: Vincent Chimezirim
=========================================================
"""

from __future__ import annotations



from .constants import (

    BOS,

    CHOCH,

    BULLISH,

    BEARISH,

)



# ==========================================================
# TOTAL EVENTS
# ==========================================================

def total_events(
    events,
):
    """
    Count structure events.
    """

    return len(events)



# ==========================================================
# BOS COUNT
# ==========================================================

def bos_count(
    events,
):
    """
    Count BOS events.
    """

    return len(

        [

            e

            for e in events

            if e.event_type == BOS

        ]

    )



# ==========================================================
# CHOCH COUNT
# ==========================================================

def choch_count(
    events,
):
    """
    Count CHoCH events.
    """

    return len(

        [

            e

            for e in events

            if e.event_type == CHOCH

        ]

    )



# ==========================================================
# BULLISH EVENTS
# ==========================================================

def bullish_events(
    events,
):
    """
    Count bullish structure.
    """

    return len(

        [

            e

            for e in events

            if e.direction == BULLISH

        ]

    )



# ==========================================================
# BEARISH EVENTS
# ==========================================================

def bearish_events(
    events,
):
    """
    Count bearish structure.
    """

    return len(

        [

            e

            for e in events

            if e.direction == BEARISH

        ]

    )



# ==========================================================
# ACTIVE COUNT
# ==========================================================

def active_events(
    events,
):
    """
    Count active events.
    """

    return len(

        [

            e

            for e in events

            if e.active

            and not e.invalidated

        ]

    )



# ==========================================================
# INVALID COUNT
# ==========================================================

def invalid_events(
    events,
):
    """
    Count invalidated events.
    """

    return len(

        [

            e

            for e in events

            if e.invalidated

        ]

    )



# ==========================================================
# AVERAGE SCORE
# ==========================================================

def average_structure_score(
    events,
):
    """
    Average event score.
    """

    if not events:

        return 0



    return round(

        sum(

            e.score

            for e in events

        )

        /

        len(events),

        2

    )



# ==========================================================
# STRONGEST EVENT
# ==========================================================

def strongest_event(
    events,
):
    """
    Return strongest structure event.
    """

    if not events:

        return None



    return max(

        events,

        key=lambda x: x.score

    )



# ==========================================================
# STRUCTURE REPORT
# ==========================================================

def structure_summary(
    state,
):
    """
    Generate market structure report.
    """

    events = state.events



    return {


        "trend":

            state.trend,



        "total_events":

            total_events(

                events

            ),



        "bos":

            bos_count(

                events

            ),



        "choch":

            choch_count(

                events

            ),



        "bullish_events":

            bullish_events(

                events

            ),



        "bearish_events":

            bearish_events(

                events

            ),



        "active":

            active_events(

                events

            ),



        "invalid":

            invalid_events(

                events

            ),



        "score":

            state.score,



        "grade":

            state.grade,



        "strongest":

            strongest_event(

                events

            ),

    }



# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "total_events",

    "bos_count",

    "choch_count",

    "bullish_events",

    "bearish_events",

    "active_events",

    "invalid_events",

    "average_structure_score",

    "strongest_event",

    "structure_summary",

]