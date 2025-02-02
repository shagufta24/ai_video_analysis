import { useState } from "react";

const ImageCarousel = ({ images }) => {
  const [currentIndex, setCurrentIndex] = useState(0);

  const nextSlide = () => {
    setCurrentIndex((prevIndex) => (prevIndex + 1) % images.length);
  };

  const prevSlide = () => {
    setCurrentIndex((prevIndex) => (prevIndex - 1 + images.length) % images.length);
  };

  if (images.length === 0) return null;

  return (
    <div className="relative w-full max-w-lg mx-auto mt-6">
      <img src={`http://127.0.0.1:5001/${images[currentIndex]}`} alt="Extracted Frame" className="rounded-lg shadow-lg" />
      
      <button
        onClick={prevSlide}
        className="absolute left-0 top-1/2 transform -translate-y-1/2 bg-gray-800 text-white px-3 py-2 rounded-full"
      >
        ◀
      </button>
      
      <button
        onClick={nextSlide}
        className="absolute right-0 top-1/2 transform -translate-y-1/2 bg-gray-800 text-white px-3 py-2 rounded-full"
      >
        ▶
      </button>
    </div>
  );
};

export default ImageCarousel;
