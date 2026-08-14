from crewai import Crew
from crewai import Process

from agents.writer_agent import WriterAgent
from configs.logger import get_logger
from agents.research_agent import ResearchAgent
from crew.tasks import CrewTasks



logger = get_logger("crew")

class AppCrew:
    
    def __init__(self):
        
        try:
            
            self.tasks = CrewTasks()
            self.research_agent = ResearchAgent()
            self.writer_agent = WriterAgent()
            
            self.crews = Crew(
                agents=[self.research_agent.research_agent, self.writer_agent.writer_agent],
                tasks=[self.tasks.research_task, self.tasks.writer_task],
                process=Process.sequential,
                verbose=True
            )
            
            logger.info("Crews are configured")
            
        
        except ValueError:
            logger.exception("Value error in app crew init")
            raise
        
        except Exception:
            logger.exception("Error in app crew init")
            raise
        
        
    def get_response(self, topic):
        
        
        try:
            
            if not topic:
                raise ValueError("topic is missing")
            
            response = self.crews.kickoff(inputs={
                "topic": topic
            })
            
            logger.info("response is fetched")
            return response.raw
            
        except ValueError:
            logger.exception("Value error in app crew get_response")
            raise
        
        except Exception:
            logger.exception("Error in app crew get_response")
            raise    
    