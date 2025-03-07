# Importing the requirements
from src.minicpm.response import describe_image
import gradio as gr
import warnings
warnings.filterwarnings("ignore")


# Image, text query, and input parameters
image = gr.Image(type="pil", label="Image")
question = gr.Textbox(label="Question", placeholder="Enter your question here")
temperature = gr.Slider(
    minimum=0.01, maximum=1.99, step=0.01, value=0.7, label="Temperature"
)
top_p = gr.Slider(minimum=0, maximum=1, step=0.01, value=0.8, label="Top P")
top_k = gr.Slider(minimum=0, maximum=1000, step=1, value=100, label="Top K")
max_new_tokens = gr.Slider(minimum=1, maximum=4096,
                           step=1, value=512, label="Max Tokens")

# Output for the interface
answer = gr.Textbox(label="Predicted answer",
                    show_label=True, show_copy_button=True)

# Examples for the interface
examples = [
    [
        "images/cat.jpg",
        "How many cats are there?",
        0.7,
        0.8,
        100,
        512,
    ],
    [
        "images/dog.jpg",
        "What is the color of the dog?",
        0.7,
        0.8,
        100,
        512,
    ],
    [
        "images/bird.jpg",
        "What does the bird do?",
        0.7,
        0.8,
        100,
        512,
    ],
]

# Title, description, and article for the interface
title = "Prismlab Demo"
description = "A GPT-4o Level MLLM for Vision, Speech and Multimodal Live Streaming. This model can answer questions about images in natural language. To use it, upload your image, type a question, select associated parameters, use the default values, click 'Submit', or click one of the examples to load them. You can read more at the links below."


# Launch the interface
interface = gr.Interface(
    fn=describe_image,
    inputs=[image, question, temperature, top_p, top_k, max_new_tokens],
    outputs=answer,
    examples=examples,
    cache_examples=True,
    cache_mode="lazy",
    title=title,
    description=description,
    theme="Glass",
    flagging_mode="never",
)
interface.launch(debug=False)
