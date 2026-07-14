"""
=========================================================
KAI Smart Money AI

Integration Layer

pipeline.py

Engine Communication Pipeline

Author: Vincent Chimezirim
=========================================================
"""

from __future__ import annotations



from engines.swing import (

    SwingEngine,

)



from engines.market_structure import (

    MarketStructureEngine,

)



from engines.order_block import (

    OrderBlockEngine,

)



from engines.fair_value_gap import (

    FairValueGapEngine,

)



from engines.confluence import (

    ConfluenceEngine,

)



from engines.liquidity import (

    LiquidityEngine,

)





# ==========================================================
# KAI PIPELINE
# ==========================================================

class KAIAnalysisPipeline:


    def __init__(self):


        self.swing_engine = SwingEngine()


        self.market_structure_engine = MarketStructureEngine()


        self.liquidity_engine = LiquidityEngine()


        self.order_block_engine = OrderBlockEngine()


        self.fvg_engine = FairValueGapEngine()


        self.confluence_engine = ConfluenceEngine()



    # ======================================================
    # RUN
    # ======================================================

    def run(
        self,
        candles,
    ):


        # ----------------------------------------------
        # 1. Swing Detection
        # ----------------------------------------------

        swing_result = self.swing_engine.analyze(

            candles

        )



        swing_collection = (

            self.swing_engine.detect(

                candles

            )

        )



        swing_collection = (

            self.swing_engine.validate(

                swing_collection

            )

        )



        swing_collection = (

            self.swing_engine.score(

                swing_collection

            )

        )



        # ----------------------------------------------
        # 2. Market Structure
        # ----------------------------------------------

        structure = (

            self.market_structure_engine.analyze(

                candles,

                swing_collection,

            )

        )



        # ----------------------------------------------
        # 3. Liquidity
        # ----------------------------------------------

        liquidity = (

            self.liquidity_engine.analyze(

                candles,

                structure,

            )

        )



        # ----------------------------------------------
        # 4. Order Blocks
        # ----------------------------------------------

        order_blocks = (

            self.order_block_engine.detect(

                candles,

                structure,

                liquidity,

            )

        )



        # ----------------------------------------------
        # 5. Fair Value Gaps
        # ----------------------------------------------

        fvgs = (

            self.fvg_engine.analyze(

                candles,

                structure,

            )

        )



        # ----------------------------------------------
        # 6. Confluence
        # ----------------------------------------------

        confluence = (

            self.confluence_engine.run(

                order_blocks,

                fvgs,

                liquidity,

                structure,

            )

        )



        return {


            "swings":

                swing_result,


            "market_structure":

                structure,


            "liquidity":

                liquidity,


            "order_blocks":

                order_blocks,


            "fair_value_gaps":

                fvgs,


            "confluence":

                confluence,


        }



__all__ = [

    "KAIAnalysisPipeline",

]