# 🎥 Smart Video Summarizer 🚀

### AI-powered video analysis tool that transcribes, summarizes, and analyzes videos with OpenAI Vision API.

![Smart Video Summarizer](https://img.shields.io/badge/AI-Powered-blue?style=for-the-badge&logo=openai) ![Status](https://img.shields.io/badge/Status-Active-green?style=for-the-badge)

## 🌟 Features
✅ **Upload videos** (.mp4, .mov, .avi, .mkv)  
✅ **AI-powered transcription** (OpenAI Whisper)  
✅ **Summarization** using GPT-4  
✅ **Keyword extraction** (NLP-based insights)  
✅ **Frame extraction & image recognition** (OpenAI Vision API)  
✅ **Progress bar for uploads**  
✅ **Image carousel for extracted frames**  
✅ **Dark-mode responsive UI**  

---

## Demo

⚡ *Coming Soon!*

---

## Installation & Setup

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-username/smart-video-summarizer.git
cd smart-video-summarizer
```

### **2️⃣ Backend Setup (Flask)**
```bash
cd backend
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

pip install -r requirements.txt
```

#### **Environment Variables**
Create a `.env` file in the backend directory:
```
OPENAI_API_KEY=your_openai_api_key
```

### **3️⃣ Start the Backend**
```bash
python app.py
```

---

### **4️⃣ Frontend Setup (React + Vite)**
```bash
cd ../frontend
pnpm install
```

### **5️⃣ Start the Frontend**
```bash
pnpm dev
```

---

## ⚙️ API Endpoints

### **1️⃣ Upload Video**
```http
POST /api/upload
```
- Uploads a video file.

### **2️⃣ Transcribe Video**
```http
POST /api/transcribe
```
- Generates and returns the transcript.

### **3️⃣ Summarize Transcript**
```http
POST /api/summarize
```
- Returns a concise summary.

### **4️⃣ Extract Key Phrases**
```http
POST /api/keywords
```
- Extracts keywords using NLP.

### **5️⃣ Extract Frames & Analyze Images**
```http
POST /api/extract-frames
```
- Extracts keyframes and analyzes images using OpenAI Vision API.

---

## 🌟 Tech Stack
- **Frontend:** React, Tailwind CSS, Vite  
- **Backend:** Flask, OpenAI Whisper, OpenAI GPT-4 Vision  
- **Database:** SQLite  
- **AI Models:** Whisper (transcription), GPT-4 (summary), CLIP/OpenAI Vision (image recognition)  

---