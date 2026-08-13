import os
import dotenv

from crewai import LLM

from configs.logger import get_logger
from configs.config import GROQ_MODEL


logger = get_logger("llm")
dotenv.load_dotenv()
class LLMHandler:
    
    def __init__(self, model_name=GROQ_MODEL):
        
        try:
            if not model_name:
                raise ValueError("Model name is missing")
            
            groq_api = os.getenv("groq_api")
            
            if not groq_api:
                raise ValueError("Groq api is missing")
        
            self.llm = LLM(
                model=GROQ_MODEL,
                api_key=groq_api,
                max_tokens=4000
            )
            
            logger.info("llm is initialized")
            
        except ValueError:
            logger.exception("Value error in llm handler")
            raise
        
        except Exception:
            logger.exception("Error in llm handler")
            raise
        
        
llm_handler = LLMHandler()
llm = llm_handler.llm