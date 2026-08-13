
from crewai import Task

from configs.logger import get_logger
from agents.research_agent import ResearchAgent
from agents.writer_agent import WriterAgent


logger = get_logger("tasks")

class CrewTasks:
    
    def __init__(self):
        
        
        try:
            
            self.research_agent = ResearchAgent().research_agent
            logger.info("Research agent is up")
            
            self.writer_agent =  WriterAgent().writer_agent
            logger.info("Writer agent is up")
            
            self.research_task = Task(
                description="analyze the major {topic}, identifying key trends and technologies. Provide a detailed report on their potential impact.",
                agent=self.research_agent,
                expected_output="A detailed report on {topic}, including trends, emerging technologies, and their impact."
            )
            
            self.writer_task = Task(
                description="Create an engaging blog post based on the research findings about {topic}. Tailor the content for a tech-savvy audience, ensuring clarity and interest.",
                agent = self.writer_agent,
                expected_output = "A 4-paragraph blog post on {topic}, written clearly and engagingly for tech enthusiasts."
            )
            
        except ValueError:
            logger.exception("Value error in crew tasks init")
            raise
        
        except Exception:
            logger.exception("Error in crew tasks init")
            raise