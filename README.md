Streamlit Image Generation Chatbot

An AI-powered image generation chatbot built using Streamlit, featuring a chat-style interface, real-time image generation via APIs, and efficient image fetching & caching.
This project was developed and demonstrated as part of a hands-on GenAI workshop at DataVista.

Features

Chat-based UI using Streamlit

AI image generation from text prompts

Real-time API integration

Image fetching and caching for performance

🔄 Clean state management with st.session_state

🚀 Deployable on Streamlit Cloud

🛠️ Tech Stack

Frontend & UI: Streamlit

Language: Python

APIs: Image generation API (provider-agnostic design)

State Management: Streamlit Session State


⚙️ Setup & Installation

1️⃣ Clone the Repository
```bash
git clone https://github.com/sasmit206/iecse_ws.git
cd iecse_ws
```

2️⃣ Create a Virtual Environment 
```
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows
```

3️⃣ Install Dependencies
```
pip install -r requirements.txt
```

4️⃣ Configure API Keys

Create a API key on hugging face and add it at ADD API KEY
IMAGE_API_KEY=your_api_key_here
```

▶️ Running the Application
```
streamlit run app.py
```


The app will start locally at:
```
http://localhost:8501
```
