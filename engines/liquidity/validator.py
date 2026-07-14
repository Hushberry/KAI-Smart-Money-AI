"""
=========================================================
KAI Smart Money AI

Liquidity Engine

validator.py

Liquidity Validation Layer

Author: Vincent Chimezirim
=========================================================
"""

from __future__ import annotations



from .models import (

    LiquidityZone,

    LiquidityState,

)



from .constants import (

    MIN_TOUCHES,

    BUY_SIDE,

    SELL_SIDE,

)



# ==========================================================
# PRICE VALIDATION
# ==========================================================

def validate_price(
    zone: LiquidityZone,
):
    """
    Ensure valid liquidity price.
    """

    return (

        zone.price > 0

    )



# ==========================================================
# TYPE VALIDATION
# ==========================================================

def validate_type(
    zone: LiquidityZone,
):
    """
    Validate liquidity type.
    """

    return zone.liquidity_type in (

        BUY_SIDE,

        SELL_SIDE,

    )



# ==========================================================
# TOUCH VALIDATION
# ==========================================================

def validate_touches(
    zone: LiquidityZone,
):
    """
    Confirm liquidity strength.
    """

    if zone.equal:

        return (

            zone.touches >= MIN_TOUCHES

        )



    return (

        zone.touches >= 1

    )



# ==========================================================
# DUPLICATE REMOVAL
# ==========================================================

def remove_duplicate_zones(
    zones,
):
    """
    Remove repeated liquidity levels.
    """

    clean = []



    for zone in zones:


        duplicate = False



        for existing in clean:


            if (

                zone.liquidity_type

                ==

                existing.liquidity_type

                and

                abs(

                    zone.price

                    -

                    existing.price

                )

                <

                0.00001

            ):

                duplicate = True

                break



        if not duplicate:

            clean.append(

                zone

            )



    return clean



# ==========================================================
# SINGLE VALIDATION
# ==========================================================

def validate_liquidity_zone(
    zone: LiquidityZone,
):
    """
    Validate liquidity zone.
    """

    checks = [

        validate_price(

            zone

        ),


        validate_type(

            zone

        ),


        validate_touches(

            zone

        ),

    ]



    if all(checks):

        zone.add_reason(

            "Liquidity validation passed"

        )


        return True



    zone.add_reason(

        "Liquidity validation failed"

    )


    zone.active = False



    return False



# ==========================================================
# STATE VALIDATION
# ==========================================================

def validate_liquidity_state(
    state: LiquidityState,
):
    """
    Validate complete liquidity state.
    """


    buy = remove_duplicate_zones(

        state.buy_side

    )


    sell = remove_duplicate_zones(

        state.sell_side

    )



    state.buy_side = [

        zone

        for zone in buy

        if validate_liquidity_zone(

            zone

        )

    ]



    state.sell_side = [

        zone

        for zone in sell

        if validate_liquidity_zone(

            zone

        )

    ]



    return state



# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "validate_liquidity_zone",

    "validate_liquidity_state",

    "remove_duplicate_zones",

]