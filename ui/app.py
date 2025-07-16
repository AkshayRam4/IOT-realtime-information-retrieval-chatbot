import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import gradio as gr
from agent import SenzMateAgent

agent = SenzMateAgent()

def chat_fn(message, history):
    answer = agent.answer(message)
    return answer

iface = gr.ChatInterface(
    fn=chat_fn,
    title="SenzMate AIoT Knowledge Agent",
    description="Ask anything about AIoT, SenzMate products, or IoT best practices."
)

if __name__ == "__main__":
    iface.launch() 
