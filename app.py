import gradio as gr

from configs.logger import get_logger
from crew.crew import AppCrew

logger = get_logger("app")


def application(topic):
    
    try:
        
        if not topic:
            raise ValueError("Topic is missing")
        
        crew = AppCrew()
        response = crew.get_response(topic)
        
        logger.info("response is fetched")
        return response
        
        
    except Exception:
        logger.exception("Error in application")
        raise


def gradio_interface():
    
    
    with gr.Blocks() as interface:
        
        gr.Markdown(
            "<h2 style='text-align: center;'>Crew-AI Research Writer</h2>"
        )
        
        #inputs
        topic = gr.Textbox(
            label="Topic",
            placeholder="Give a topic about for research"
        )
        
        result = gr.TextArea(
            label="Research",
            placeholder="Please wait until the research will generate..."
        )
        
        submit_btn = gr.Button("Submit")
        
        submit_btn.click(
            fn=
        )
    