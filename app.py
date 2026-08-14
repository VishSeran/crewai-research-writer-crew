import gradio as gr

from configs.logger import get_logger

logger = get_logger("app")


def application(topic):
    
    try:
        
        if not topic:
            raise ValueError("Topic is missing")
        
        
        
        
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
    