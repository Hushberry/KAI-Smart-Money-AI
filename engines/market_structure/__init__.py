"""
=========================================================
KAI Smart Money AI

Market Structure Engine

Package Initializer

Author: Vincent Chimezirim
=========================================================
"""


from .engine import (

    MarketStructureEngine,

)


from .models import (

    StructureEvent,

    MarketStructureState,

)


from .detector import (

    detect_structure,

    detect_bos,

    detect_choch,

    detect_swing_relationships,

)


from .validator import (

    validate_structure_event,

    validate_structure_state,

)


from .scorer import (

    calculate_event_score,

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



__all__ = [

    "MarketStructureEngine",

    "StructureEvent",

    "MarketStructureState",

    "detect_structure",

    "detect_bos",

    "detect_choch",

    "detect_swing_relationships",

    "validate_structure_event",

    "validate_structure_state",

    "calculate_event_score",

    "calculate_structure_score",

    "score_structure_events",

    "update_structure_state",

    "active_structure_events",

    "structure_summary",

]