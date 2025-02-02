import React from "react";
import "video.js/dist/video-js.css";

const VideoPlayer = ({ src }) => {
  return (
    <video
      className="w-full max-w-2xl rounded-lg mt-4"
      controls
      src={`http://127.0.0.1:5000/uploads/${src}`}
    />
  );
};

export default VideoPlayer;
