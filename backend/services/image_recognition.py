import openai
from config import Config
from PIL import Image
import base64

def encode_image(image_path):
    """Converts an image to base64 format for OpenAI API."""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def analyze_images(image_paths):
    """Sends extracted images to OpenAI's Vision API for recognition."""
    results = []
    
    for image_path in image_paths:
        image_data = encode_image(image_path)

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4-vision-preview",
                messages=[
                    {"role": "system", "content": "You are an image recognition assistant."},
                    {"role": "user", "content": [
                        {"type": "text", "content": "Describe the content of this image."},
                        {"type": "image", "image_data": image_data}
                    ]}
                ],
                max_tokens=300
            )
            description = response["choices"][0]["message"]["content"]
            results.append({"image": image_path, "description": description})

        except Exception as e:
            print(f"Error processing {image_path}: {e}")

    return results
