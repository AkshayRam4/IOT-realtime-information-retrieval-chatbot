#  AIoT Knowledge Agent

A simple agentic application that answers questions about AIoT, SenzMate products, and IoT best practices using Retrieval-Augmented Generation (RAG) with web search.

## Features
- Chat interface powered by Gradio
- Uses OpenAI and Tavily for up-to-date answers
- Easy to extend for local document retrieval

## Setup

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd senzmate-agentic-aiot
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set API keys:**
   - Create a file named `.env` in your project root (the same folder as `requirements.txt`).
   - Add the following lines (replace with your actual keys, and **do NOT use quotes**):

     ```env
     OPENAI_API_KEY=your_openai_key_here
     TAVILY_API_KEY=your_tavily_key_here
     ```

   - Make sure the variable names are spelled exactly as above.
   - Your `.env` file should **NOT** be committed to GitHub (it is already in `.gitignore`).

## Usage

Run the Gradio app:
```bash
python ui/app.py
```

Open the link in your browser and start chatting!

## Example Questions
- What is SenzMate's SenzMatica platform?
- How does AIoT benefit agriculture?
- What are best practices for IoT device security?

## License
MIT 
