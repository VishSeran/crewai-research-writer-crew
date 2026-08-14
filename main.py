
from app import gradio_interface
from configs.logger import get_logger


logger = get_logger("main")


if __name__ == "__main__":
    
    print("Application is starting....")
    gradio_interface()



    
    