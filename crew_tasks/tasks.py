
from crewai import Task

from configs.logger import get_logger
from agents.research_agent import ResearchAgent
from agents.writer_agent import WriterAgent


logger = get_logger("tasks")

class CrewTasks:
    
    def __init__(self):
        
        
        try:
            
            self.research_agent = ResearchAgent().research_agent
            self.writer_agent =  WriterAgent().writer_agent
            
            self.research_task = Task(
                description="analyze the major {topic}, identifying key trends and technologies. Provide a detailed report on their potential impact.",
                agent=ResearchAgent
            )
            
        except ValueError:
            logger.exception("Value error in crew tasks init")
            raise
        
        except Exception:
            logger.exception("Error in crew tasks init")
            raise