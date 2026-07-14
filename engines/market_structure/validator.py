"""
=========================================================
KAI Smart Money AI

Market Structure Engine

validator.py

Structure Validation Layer

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
# PRICE VALIDATION
# ==========================================================

def validate_price(
    event: StructureEvent,
):
    """
    Validate broken price.
    """

    return (

        event.broken_price > 0

    )



# ==========================================================
# EVENT TYPE VALIDATION
# ==========================================================

def validate_event_type(
    event: StructureEvent,
):
    """
    Check valid structure event.
    """

    return event.event_type in (

        BOS,

        CHOCH,

    )



# ==========================================================
# DIRECTION VALIDATION
# ==========================================================

def validate_direction(
    event: StructureEvent,
):
    """
    Check direction.
    """

    return event.direction in (

        BULLISH,

        BEARISH,

    )



# ==========================================================
# BREAK VALIDATION
# ==========================================================

def validate_break(
    event: StructureEvent,
):
    """
    Ensure real structure break.
    """

    if event.previous_price == 0:

        return False



    if event.direction == BULLISH:

        return (

            event.broken_price

            >

            event.previous_price

        )



    if event.direction == BEARISH:

        return (

            event.broken_price

            <

            event.previous_price

        )



    return False



# ==========================================================
# SINGLE EVENT VALIDATION
# ==========================================================

def validate_structure_event(
    event: StructureEvent,
):
    """
    Validate one structure event.
    """

    checks = [

        validate_price(

            event

        ),


        validate_event_type(

            event

        ),


        validate_direction(

            event

        ),


        validate_break(

            event

        ),

    ]



    if all(checks):

        event.confirmed = True


        event.add_reason(

            "Structure validation passed"

        )


        return True



    event.add_reason(

        "Structure validation failed"

    )


    return False



# ==========================================================
# EVENT CLEANING
# ==========================================================

def remove_invalid_events(
    events,
):
    """
    Remove invalid structure events.
    """

    valid = []



    for event in events:


        if validate_structure_event(

            event

        ):

            valid.append(

                event

            )



    return valid



# ==========================================================
# STATE VALIDATION
# ==========================================================

def validate_structure_state(
    state: MarketStructureState,
):
    """
    Validate complete structure.
    """


    state.events = remove_invalid_events(

        state.events

    )


    if state.events:

        return True



    return False



# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "validate_structure_event",

    "remove_invalid_events",

    "validate_structure_state",

]