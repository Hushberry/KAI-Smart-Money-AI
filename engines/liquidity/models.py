"""
=========================================================
KAI Smart Money AI

Liquidity Engine

models.py

Liquidity Data Models

Author: Vincent Chimezirim
=========================================================
"""

from __future__ import annotations



from dataclasses import dataclass, field


from typing import Optional, List



# ==========================================================
# LIQUIDITY ZONE MODEL
# ==========================================================

@dataclass
class LiquidityZone:
    """
    Represents an institutional liquidity area.
    """


    # ------------------------------------------------------
    # Identity
    # ------------------------------------------------------

    id: Optional[str] = None


    index: int = 0


    timestamp: Optional[str] = None



    # ------------------------------------------------------
    # Price
    # ------------------------------------------------------

    price: float = 0.0


    high: float = 0.0


    low: float = 0.0



    # ------------------------------------------------------
    # Type
    # ------------------------------------------------------

    liquidity_type: str = ""



    # ------------------------------------------------------
    # Structure
    # ------------------------------------------------------

    touches: int = 0


    equal: bool = False



    # ------------------------------------------------------
    # Status
    # ------------------------------------------------------

    swept: bool = False


    active: bool = True



    # ------------------------------------------------------
    # Quality
    # ------------------------------------------------------

    score: float = 0.0


    grade: str = "D"



    # ------------------------------------------------------
    # Explanation
    # ------------------------------------------------------

    reasons: List[str] = field(

        default_factory=list

    )



    # ======================================================
    # METHODS
    # ======================================================

    def add_reason(
        self,
        reason: str,
    ):
        """
        Add explanation.
        """

        if reason not in self.reasons:

            self.reasons.append(

                reason

            )



    def mark_swept(
        self,
    ):
        """
        Mark liquidity consumed.
        """

        self.swept = True

        self.active = False



# ==========================================================
# LIQUIDITY SWEEP MODEL
# ==========================================================

@dataclass
class LiquiditySweep:
    """
    Represents a liquidity raid.
    """


    index: int = 0


    timestamp: Optional[str] = None



    liquidity_type: str = ""


    price: float = 0.0



    confirmed: bool = False



    score: float = 0.0


    grade: str = "D"



    reasons: List[str] = field(

        default_factory=list

    )



    def add_reason(
        self,
        reason: str,
    ):

        if reason not in self.reasons:

            self.reasons.append(

                reason

            )



# ==========================================================
# LIQUIDITY STATE
# ==========================================================

@dataclass
class LiquidityState:
    """
    Complete liquidity analysis state.
    """


    buy_side: List[LiquidityZone] = field(

        default_factory=list

    )


    sell_side: List[LiquidityZone] = field(

        default_factory=list

    )


    sweeps: List[LiquiditySweep] = field(

        default_factory=list

    )



    # ------------------------------------------------------
    # Metrics
    # ------------------------------------------------------

    total_score: float = 0.0


    grade: str = "D"



    # ======================================================
    # METHODS
    # ======================================================

    def all_zones(
        self,
    ):

        return (

            self.buy_side

            +

            self.sell_side

        )