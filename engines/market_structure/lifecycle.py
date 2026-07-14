"""
=========================================================
KAI Smart Money AI

Market Structure Engine

lifecycle.py

Structure Lifecycle Management

Author: Vincent Chimezirim
=========================================================
"""

from __future__ import annotations



from .models import (

    StructureEvent,

    MarketStructureState,

)



from .constants import (

    BULLISH,

    BEARISH,

)



# ==========================================================
# UPDATE EVENT AGE
# ==========================================================

def update_event_age(
    event: StructureEvent,
    current_index: int,
):
    """
    Track structure event age.
    """

    event.age = (

        current_index

        -

        event.index

    ) if hasattr(event, "age") else 0



    return event



# ==========================================================
# CHECK STRUCTURE INVALIDATION
# ==========================================================

def check_event_invalidation(
    event: StructureEvent,
    candles,
):
    """
    Check if BOS/CHoCH failed.
    """

    if event.invalidated:

        return True



    for i in range(

        event.index + 1,

        len(candles)

    ):


        candle = candles.iloc[i]



        high = float(

            candle["high"]

        )


        low = float(

            candle["low"]

        )



        # Bullish structure failure

        if event.direction == BULLISH:


            if low < event.previous_price:


                event.invalidate()


                event.add_reason(

                    "Bullish structure invalidated"

                )


                return True



        # Bearish structure failure

        if event.direction == BEARISH:


            if high > event.previous_price:


                event.invalidate()


                event.add_reason(

                    "Bearish structure invalidated"

                )


                return True



    return False



# ==========================================================
# UPDATE EVENT
# ==========================================================

def update_structure_event(
    event: StructureEvent,
    candles,
):
    """
    Update one structure event.
    """

    check_event_invalidation(

        event,

        candles

    )


    return event



# ==========================================================
# UPDATE EVENTS
# ==========================================================

def update_structure_events(
    events,
    candles,
):
    """
    Update all structure events.
    """

    updated = []



    for event in events:


        updated.append(

            update_structure_event(

                event,

                candles

            )

        )



    return updated



# ==========================================================
# ACTIVE EVENTS
# ==========================================================

def active_structure_events(
    events,
):
    """
    Return valid structure events.
    """

    return [

        event

        for event in events

        if event.active

        and not event.invalidated

    ]



# ==========================================================
# INVALID EVENTS
# ==========================================================

def invalid_structure_events(
    events,
):
    """
    Return invalid events.
    """

    return [

        event

        for event in events

        if event.invalidated

    ]



# ==========================================================
# UPDATE STATE
# ==========================================================

def update_structure_state(
    state: MarketStructureState,
    candles,
):
    """
    Update market structure lifecycle.
    """

    state.events = update_structure_events(

        state.events,

        candles

    )


    return state



# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "update_structure_event",

    "update_structure_events",

    "active_structure_events",

    "invalid_structure_events",

    "update_structure_state",

]