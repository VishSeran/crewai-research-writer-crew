
from crewai import Agent
from crewai_tools import SerperDevTool

from configs.logger import get_logger

from agents.llm import llm


logger = get_logger("writer-agent")

class WriterAgent:
    
    def __init__(self):
        
        try:
            
            self.writer_agent = Agent(
                role = "Tech Content Strategist",
                goal = "Craft well-structured and engaging content based on research findings",
                backstory = """You are a skilled content strategist known for translating 
                complex topics into clear and compelling narratives. Your writing makes 
                information accessible and engaging for a wide audience.""",
                
                llm = llm,
                verbose = True,
                allow_delegation = False,
                tools = [SerperDevTool()]
            )
            
            logger.info("Writer agent has initialized")
            
        except ValueError:
            logger.exception("Value error in writer agent init")
            raise
        
        except Exception:
            logger.exception("Error in writer agent init")
            raise