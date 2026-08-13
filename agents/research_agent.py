
from crewai import Agent

from configs.logger import get_logger


logger = get_logger("research-agent")


class ResearchAgent:
    
    def __init__(self):
        
        
        try:
            
        except ValueError:
            logger.exception("Value error in research agent init")
            raise
        
        except Exception:
            logger.exception("Error in research agent init")
            raise