"""
=========================================================
KAI Smart Money AI

Market Structure Engine

detector.py

BOS / CHoCH Detection

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



from .utils import (

    classify_high,

    classify_low,

    valid_structure_break,

)



# ==========================================================
# DETECT HIGH/LOW STRUCTURE
# ==========================================================

def detect_swing_relationships(
    swings,
):
    """
    Classify swing points into:

    HH
    HL
    LH
    LL
    """

    classifications = []



    previous_high = None

    previous_low = None



    for swing in sorted(

        swings,

        key=lambda x: x.index

    ):


        if swing.swing_type == "swing_high":


            if previous_high is not None:


                result = classify_high(

                    swing.price,

                    previous_high,

                )


                if result:

                    classifications.append(

                        result

                    )


            previous_high = swing.price



        elif swing.swing_type == "swing_low":


            if previous_low is not None:


                result = classify_low(

                    swing.price,

                    previous_low,

                )


                if result:

                    classifications.append(

                        result

                    )


            previous_low = swing.price



    return classifications



# ==========================================================
# BOS DETECTION
# ==========================================================

def detect_bos(
    candles,
    state: MarketStructureState,
):
    """
    Detect Break Of Structure.
    """

    events = []



    if not state.last_high and not state.last_low:

        return events



    current_price = float(

        candles.iloc[-1]["close"]

    )



    # Bullish BOS

    if valid_structure_break(

        current_price,

        state.last_high,

        BULLISH,

    ):


        event = StructureEvent(

            index=len(candles)-1,

            event_type=BOS,

            direction=BULLISH,

            broken_price=current_price,

            previous_price=state.last_high,

            confirmed=True,

        )


        event.add_reason(

            "Bullish break of structure"

        )


        events.append(

            event

        )



    # Bearish BOS

    if valid_structure_break(

        current_price,

        state.last_low,

        BEARISH,

    ):


        event = StructureEvent(

            index=len(candles)-1,

            event_type=BOS,

            direction=BEARISH,

            broken_price=current_price,

            previous_price=state.last_low,

            confirmed=True,

        )


        event.add_reason(

            "Bearish break of structure"

        )


        events.append(

            event

        )



    return events



# ==========================================================
# CHoCH DETECTION
# ==========================================================

def detect_choch(
    previous_trend,
    current_trend,
    index,
    price,
):
    """
    Detect Change Of Character.
    """

    if previous_trend == current_trend:

        return None



    if current_trend not in (

        BULLISH,

        BEARISH,

    ):

        return None



    event = StructureEvent(

        index=index,

        event_type=CHOCH,

        direction=current_trend,

        broken_price=price,

        confirmed=True,

    )


    event.add_reason(

        "Market structure trend changed"

    )


    return event



# ==========================================================
# MASTER DETECTOR
# ==========================================================

def detect_structure(
    candles,
    swing_data,
):
    """
    Complete structure detection.
    """


    state = MarketStructureState()



    swings = swing_data.all_swings()



    classifications = detect_swing_relationships(

        swings

    )



    # Basic trend

    bullish = classifications.count(

        "higher_high"

    ) + classifications.count(

        "higher_low"

    )


    bearish = classifications.count(

        "lower_high"

    ) + classifications.count(

        "lower_low"

    )



    if bullish > bearish:

        state.trend = BULLISH


    elif bearish > bullish:

        state.trend = BEARISH



    # Last swing references

    highs = swing_data.highs

    lows = swing_data.lows



    if highs:

        state.last_high = highs[-1].price



    if lows:

        state.last_low = lows[-1].price



    events = detect_bos(

        candles,

        state,

    )



    for event in events:

        state.add_event(

            event

        )



    return state



# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "detect_structure",

    "detect_bos",

    "detect_choch",

    "detect_swing_relationships",

]