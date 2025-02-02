import { useState } from "react";
import axios from "axios";
import { useDropzone } from "react-dropzone";

const VideoUpload = ({ onUpload }) => {
  const [uploading, setUploading] = useState(false);
  const [progress, setProgress] = useState(0);

  const { getRootProps, getInputProps } = useDropzone({
    accept: "video/*",
    onDrop: async (acceptedFiles) => {
      setUploading(true);
      const file = acceptedFiles[0];
      const formData = new FormData();
      formData.append("file", file);

      try {
        const response = await axios.post("http://127.0.0.1:5001/api/upload", formData, {
          onUploadProgress: (progressEvent) => {
            const percentCompleted = Math.round((progressEvent.loaded * 100) / progressEvent.total);
            setProgress(percentCompleted);
          },
        });

        onUpload(response.data.filename);
      } catch (error) {
        console.error("Upload failed:", error);
      } finally {
        setUploading(false);
      }
    },
  });

  return (
    <div className="flex flex-col items-center gap-4">
      <div {...getRootProps()} className="border-2 border-dashed border-gray-500 p-6 rounded-lg text-center cursor-pointer w-80">
        <input {...getInputProps()} />
        {uploading ? <p className="text-gray-300">Uploading {progress}%...</p> : <p>📂 Drag & drop a video, or click to select</p>}
      </div>

      {uploading && (
        <div className="w-80 bg-gray-700 rounded-full h-2">
          <div className="bg-blue-500 h-2 rounded-full" style={{ width: `${progress}%` }}></div>
        </div>
      )}
    </div>
  );
};

export default VideoUpload;
