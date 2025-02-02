import { useState } from "react";
import axios from "axios";
import ImageCarousel from "./ImageCarousel";

const Transcript = ({ filename }) => {
  const [transcript, setTranscript] = useState("");
  const [imageAnalysis, setImageAnalysis] = useState([]);
  const [frames, setFrames] = useState([]);
  const [loadingImages, setLoadingImages] = useState(false);

  const fetchTranscript = async () => {
    try {
      const response = await axios.post("http://127.0.0.1:5001/api/transcribe", { filename });
      setTranscript(response.data.transcript);
    } catch (error) {
      console.error("Error fetching transcript:", error);
    }
  };

  const fetchImageAnalysis = async () => {
    setLoadingImages(true);
    try {
      const response = await axios.post("http://127.0.0.1:5001/api/extract-frames", { filename });
      setFrames(response.data.frames);
      setImageAnalysis(response.data.results);
    } catch (error) {
      console.error("Error fetching image analysis:", error);
    } finally {
      setLoadingImages(false);
    }
  };

  return (
    <div className="max-w-4xl mx-auto p-6 bg-gray-900 text-white rounded-lg shadow-lg">
      <h2 className="text-3xl font-bold text-center mb-6">📜 Video Transcript</h2>

      <button onClick={fetchTranscript} className="bg-blue-600 hover:bg-blue-700 px-6 py-2 rounded-lg text-white">
        Get Transcript
      </button>

      {transcript && (
        <div className="bg-gray-800 p-4 rounded-lg mt-6">
          <h3 className="text-xl font-bold mb-2">Transcript:</h3>
          <pre className="max-h-60 overflow-y-auto">{transcript}</pre>
        </div>
      )}

      <button onClick={fetchImageAnalysis} className="bg-purple-600 hover:bg-purple-700 px-6 py-2 rounded-lg text-white mt-6">
        Analyze Video Frames
      </button>

      {loadingImages && <p className="mt-2 text-gray-400">Extracting frames...</p>}

      {frames.length > 0 && <ImageCarousel images={frames} />}
    </div>
  );
};

export default Transcript;
