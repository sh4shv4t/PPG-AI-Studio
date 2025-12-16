# 🎨 PPG AI Studio

> **Prompt-to-Product Generation Studio** - Transform your ideas into visual reality using AI-powered image generation and intelligent workflow orchestration.

[![Next.js](https://img.shields.io/badge/Next.js-14.2.35-black?style=flat-square&logo=next.js)](https://nextjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Latest-009688?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com/)
[![LangChain](https://img.shields.io/badge/LangChain-Powered-blue?style=flat-square)](https://python.langchain.com/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind-CSS-38B2AC?style=flat-square&logo=tailwind-css)](https://tailwindcss.com/)

## ✨ Features

- 🤖 **AI-Powered Planning**: Leverages Google's Gemini 1.5 Pro for intelligent prompt processing
- 🎨 **Image Generation**: Integrated with FLUX AI for high-quality image creation
- 🔄 **LangGraph Workflow**: Sophisticated state management and orchestration
- ⚡ **Real-time Streaming**: Live updates of generation progress
- 🎯 **Trace Panel**: Visualize the AI decision-making process
- 🌐 **Modern UI**: Built with Next.js 14 and Tailwind CSS

## 🏗️ Architecture

```
PPG-AI-Studio/
├── backend/                 # FastAPI backend
│   ├── api.py              # API endpoints
│   ├── main.py             # Application entry point
│   ├── graph/              # LangGraph workflow
│   │   ├── nodes.py        # Workflow nodes
│   │   ├── state.py        # State management
│   │   └── workflow.py     # Workflow orchestration
│   └── services/           # External services
│       ├── flux.py         # FLUX image generation
│       └── llm.py          # LLM configuration
└── frontend/               # Next.js frontend
    ├── app/                # Next.js app directory
    │   ├── layout.tsx      # Root layout
    │   └── page.tsx        # Home page
    ├── components/         # React components
    │   ├── PromptInput.tsx
    │   ├── ResultView.tsx
    │   ├── TracePanel.tsx
    │   └── LoadingSkeleton.tsx
    └── styles/             # Global styles
        └── globals.css
```

## 🚀 Getting Started

### Prerequisites

- **Node.js** 18+ and npm
- **Python** 3.9+ and pip
- **API Keys**:
  - Google Gemini API Key ([Get it here](https://makersuite.google.com/app/apikey))
  - FLUX AI API Key (if using FLUX for image generation)

### Installation

#### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/PPG-AI-Studio.git
cd PPG-AI-Studio
```

#### 2. Backend Setup
```bash
cd backend

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
echo "GEMINI_API_KEY=your_gemini_api_key_here" > .env
echo "FLUX_API_KEY=your_flux_api_key_here" >> .env
```

#### 3. Frontend Setup
```bash
cd ../frontend

# Install dependencies
npm install

# Create .env file
echo "NEXT_PUBLIC_API_BASE_URL=http://127.0.0.1:8000" > .env
```

### 🏃 Running the Application

#### Start Backend Server
```bash
cd backend
uvicorn main:app --reload
```
Server will run on `http://127.0.0.1:8000`

#### Start Frontend Development Server
```bash
cd frontend
npm run dev
```
Frontend will run on `http://localhost:3000`

## 📖 Usage

1. **Enter Your Idea**: Type your creative prompt in the input field
2. **Submit**: Click "Generate" to start the AI workflow
3. **Watch the Magic**: View real-time trace of the AI's decision-making process
4. **Get Results**: See your generated image with the refined prompt

### Example Prompts
```
"A futuristic cityscape at sunset with flying cars"
"Minimalist logo for a tech startup"
"Abstract art combining nature and technology"
```

## 🛠️ Technology Stack

### Backend
- **FastAPI**: High-performance Python web framework
- **LangGraph**: State machine for complex AI workflows
- **LangChain**: LLM integration and orchestration
- **Google Gemini**: Advanced language model
- **FLUX AI**: State-of-the-art image generation

### Frontend
- **Next.js 14**: React framework with App Router
- **TypeScript**: Type-safe JavaScript
- **Tailwind CSS**: Utility-first CSS framework
- **React Hooks**: Modern state management

## 🔧 Configuration

### Environment Variables

#### Backend (`.env`)
```env
GEMINI_API_KEY=your_gemini_api_key
FLUX_API_KEY=your_flux_api_key
```

#### Frontend (`.env`)
```env
NEXT_PUBLIC_API_BASE_URL=http://127.0.0.1:8000
```

## 📝 API Documentation

Once the backend is running, visit:
- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`

### Main Endpoint
```http
POST /api/generate
Content-Type: application/json

{
  "idea": "Your creative prompt here"
}
```


## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Google Gemini](https://ai.google.dev/) for powerful language models
- [LangChain](https://python.langchain.com/) for LLM orchestration
- [Next.js](https://nextjs.org/) for the amazing React framework
- [FastAPI](https://fastapi.tiangolo.com/) for the modern Python web framework

## 📧 Contact

Your Name - [@shashvatsingh05](https://x.com/shashvatsingh05)

Project Link: [https://github.com/sh4shv4t/PPG-AI-Studio](https://github.com/sh4shv4t/PPG-AI-Studio)

---
