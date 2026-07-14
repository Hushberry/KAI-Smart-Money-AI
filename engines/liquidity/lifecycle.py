"""
=========================================================
KAI Smart Money AI

Liquidity Engine

lifecycle.py

Liquidity Lifecycle Management

Author: Vincent Chimezirim
=========================================================
"""

from __future__ import annotations



from .models import (

    LiquidityZone,

    LiquiditySweep,

    LiquidityState,

)



from .constants import (

    BUY_SIDE,

    SELL_SIDE,

    SWEEP,

)



# ==========================================================
# CHECK BUY SIDE SWEEP
# ==========================================================

def check_buy_side_sweep(
    zone: LiquidityZone,
    candles,
):
    """
    Detect price taking buy-side liquidity.
    """

    for i in range(

        zone.index + 1,

        len(candles)

    ):


        high = float(

            candles.iloc[i]["high"]

        )



        if high > zone.price:


            zone.mark_swept()



            sweep = LiquiditySweep(

                index=i,

                liquidity_type=BUY_SIDE,

                price=zone.price,

                confirmed=True,

            )


            sweep.add_reason(

                "Buy-side liquidity swept"

            )


            return sweep



    return None



# ==========================================================
# CHECK SELL SIDE SWEEP
# ==========================================================

def check_sell_side_sweep(
    zone: LiquidityZone,
    candles,
):
    """
    Detect price taking sell-side liquidity.
    """

    for i in range(

        zone.index + 1,

        len(candles)

    ):


        low = float(

            candles.iloc[i]["low"]

        )



        if low < zone.price:


            zone.mark_swept()



            sweep = LiquiditySweep(

                index=i,

                liquidity_type=SELL_SIDE,

                price=zone.price,

                confirmed=True,

            )


            sweep.add_reason(

                "Sell-side liquidity swept"

            )


            return sweep



    return None



# ==========================================================
# UPDATE ZONE
# ==========================================================

def update_liquidity_zone(
    zone: LiquidityZone,
    candles,
):
    """
    Update one liquidity zone.
    """

    if not zone.active:

        return None



    if zone.liquidity_type == BUY_SIDE:

        return check_buy_side_sweep(

            zone,

            candles

        )



    if zone.liquidity_type == SELL_SIDE:

        return check_sell_side_sweep(

            zone,

            candles

        )



    return None



# ==========================================================
# UPDATE ALL LIQUIDITY
# ==========================================================

def update_liquidity_state(
    state: LiquidityState,
    candles,
):
    """
    Update liquidity lifecycle.
    """

    sweeps = []



    for zone in state.all_zones():


        result = update_liquidity_zone(

            zone,

            candles

        )


        if result:

            sweeps.append(

                result

            )



    state.sweeps.extend(

        sweeps

    )


    return state



# ==========================================================
# ACTIVE LIQUIDITY
# ==========================================================

def active_liquidity(
    state: LiquidityState,
):
    """
    Return untouched liquidity.
    """

    return [

        zone

        for zone in state.all_zones()

        if zone.active

    ]



# ==========================================================
# SWEPT LIQUIDITY
# ==========================================================

def swept_liquidity(
    state: LiquidityState,
):
    """
    Return consumed liquidity.
    """

    return [

        zone

        for zone in state.all_zones()

        if zone.swept

    ]



# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "update_liquidity_state",

    "update_liquidity_zone",

    "active_liquidity",

    "swept_liquidity",

]