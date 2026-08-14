import gradio as gr


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
    