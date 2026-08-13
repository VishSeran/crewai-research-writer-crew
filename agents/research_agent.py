
from crewai import Agent
from crewai_tools import SerperDevTool

from agents.llm import llm
from configs.logger import get_logger


logger = get_logger("research-agent")


class ResearchAgent:
    
    def __init__(self):
        
        
        try:
            
            self.research_agent = Agent(
                role = "Senior Research Analyst",
                goal = "Uncover cutting-edge information and insights on any subject with comprehensive analysis",
                backstory = """You are an expert researcher with extensive experience in gathering, analyzing, and synthesizing information across multiple domains. 
                                Your analytical skills allow you to quickly identify key trends, separate fact from opinion, and produce insightful reports on any topic. 
                                You excel at finding reliable sources and extracting valuable information efficiently.""",
                verbose = True,
                allow_delegation = False,
                llm = llm,
                tools = [SerperDevTool()]                            
            )
            
            logger.info("research agent has initialized")
            
        except ValueError:
            logger.exception("Value error in research agent init")
            raise
        
        except Exception:
            logger.exception("Error in research agent init")
            raise