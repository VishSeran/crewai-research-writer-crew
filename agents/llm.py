
from crewai import LLM

from configs.logger import get_logger
from configs.config import GROQ_MODEL


logger = get_logger("llm")

class LLMHandler:
    
    def __init__(self):
        
        try:
            
        
            self.llm = LLM(
                model=GROQ_MODEL
            )
            
        except ValueError as e:
            logger.exception("Value error in llm handler")
            raise
        
        except Exception as e:
            logger.exception("Error in llm handler")
            raise