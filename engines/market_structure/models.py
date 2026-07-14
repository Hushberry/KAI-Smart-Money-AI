"""
=========================================================
KAI Smart Money AI

Market Structure Engine

models.py

Structure Data Models

Author: Vincent Chimezirim
=========================================================
"""

from __future__ import annotations



from dataclasses import dataclass, field


from typing import Optional, List



# ==========================================================
# STRUCTURE EVENT MODEL
# ==========================================================

@dataclass
class StructureEvent:
    """
    Represents BOS or CHoCH event.
    """


    # ------------------------------------------------------
    # Identity
    # ------------------------------------------------------

    id: Optional[str] = None


    index: int = 0


    timestamp: Optional[str] = None



    # ------------------------------------------------------
    # Event
    # ------------------------------------------------------

    event_type: str = ""


    direction: str = "neutral"



    # ------------------------------------------------------
    # Price Information
    # ------------------------------------------------------

    broken_price: float = 0.0


    previous_price: float = 0.0



    # ------------------------------------------------------
    # Quality
    # ------------------------------------------------------

    confirmed: bool = False


    score: float = 0.0


    grade: str = "D"



    # ------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------

    active: bool = True


    invalidated: bool = False



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



    def invalidate(
        self,
    ):
        """
        Disable structure event.
        """

        self.invalidated = True

        self.active = False



# ==========================================================
# MARKET STRUCTURE STATE
# ==========================================================

@dataclass
class MarketStructureState:
    """
    Current market structure condition.
    """


    trend: str = "neutral"



    last_high: float = 0.0


    last_low: float = 0.0



    previous_high: float = 0.0


    previous_low: float = 0.0



    bullish_structure: bool = False


    bearish_structure: bool = False



    # ------------------------------------------------------
    # Events
    # ------------------------------------------------------

    events: List[StructureEvent] = field(

        default_factory=list

    )



    # ------------------------------------------------------
    # Score
    # ------------------------------------------------------

    score: float = 0.0


    grade: str = "D"



    # ======================================================
    # METHODS
    # ======================================================

    def add_event(
        self,
        event: StructureEvent,
    ):
        """
        Store structure event.
        """

        self.events.append(

            event

        )