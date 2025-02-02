import { useState } from "react";
import VideoUpload from "./components/VideoUpload";
import Transcript from "./components/Transcript";

export default function App() {
  const [filename, setFilename] = useState("");

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-900 text-white p-6">
      {/* Hero Section */}
      <div className="text-center max-w-3xl">
        <h1 className="text-5xl font-bold mb-4 animate-fade-in">🎥 Smart Video Summarizer</h1>
        <p className="text-lg text-gray-300 leading-relaxed mb-8 animate-fade-in">
          Upload a video, and our AI-powered system will **transcribe, summarize, and analyze** 
          the video content. It even extracts frames for **image recognition**!
        </p>

        {/* Show Upload Section Initially */}
        {!filename ? (
          <div className="flex flex-col items-center gap-6 animate-fade-in">
            <VideoUpload onUpload={setFilename} />

            <p className="text-gray-400 text-sm">
              Supports: `.mp4`, `.mov`, `.avi`, `.mkv`
            </p>
          </div>
        ) : (
          // Show Transcript and Analysis Components After Upload
          <div className="w-full flex flex-col items-center animate-slide-up">
            <Transcript filename={filename} />
          </div>
        )}
      </div>
    </div>
  );
}
