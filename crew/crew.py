

from configs.logger import get_logger


logger = get_logger("crew")

class AppCrew:
    
    def __init__(self):
        
        try:
            
        
        except ValueError:
            logger.exception("Value error in app crew init")
            raise
        
        except Exception:
            logger.exception("Error in app crew init")
            raise
    