# Teams AI Bot 🤖

An intelligent Microsoft Teams bot that joins meetings, listens to conversations in real-time, and answers questions using AI.

## Features

✅ **Auto-join Teams Meetings** - Bot automatically joins when invited  
✅ **Real-time Speech Recognition** - Understands spoken questions  
✅ **AI-Powered Responses** - Answers using GPT-4  
✅ **Chat Integration** - Responds in meeting chat  
✅ **Meeting Transcription** - Captures meeting content  

## Prerequisites

- Python 3.8+
- Azure Account (Bot Service, Cognitive Services)
- OpenAI API Key
- Microsoft Teams

## Installation

1. Clone the repository:
```bash
git clone https://github.com/SampadaJCI/teams-ai-bot.git
cd teams-ai-bot

Create virtual environment:
bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:
bash
pip install -r requirements.txt
Setup configuration:
bash
cp .env.example .env
# Edit .env with your credentials
Run the bot:
bash
python bot.py
Architecture
Bot Framework - Microsoft Bot Framework SDK
Speech Services - Azure Cognitive Services
LLM - OpenAI GPT-4
Teams Integration - Microsoft Graph API
Next Steps
 Setup Azure Bot Service
 Configure Speech Recognition
 Integrate OpenAI API
 Deploy to Azure
 Test in Teams
Contributing
Feel free to fork and submit pull requests!
