import streamlit as st
import os
import replicate
import base64
import tempfile
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")
api = replicate.Client(api_token=REPLICATE_API_TOKEN)
# Function to generate image
def generate_image(input_image, input_text):
    # Create a temporary file for the input image
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp:
        temp.write(input_image)
        temp_path = Path(temp.name)

    # Running the replicate with the image file directly
    output = replicate.run(
         "qr2ai/outline:ba60c1777f6ced951496e504124841978041baaf72e6e82e9e005bddcbdb307c",
        input={
            "image": temp_path,
            "prompt": input_text,
            "width": 768,
            "height": 768,
            "refine": "expert_ensemble_refiner",
            "disable_safety_checker": True,
            "negative_prompt": "blurry, ugly, distorted, text, bw,Dull and Lifeless Colors, Poor Lighting, Blurred and Unfocused, Overexposed,Higlights,Distorted Perspective, Gritty Texture, low res, draft, cgi, low quality,render,thumbnail,cg, 3d, unreal, cartoon, anime,futuristic,",
            "apply_watermark": False,
            "num_inference_steps": 25,
            "color_prompts": "True"
        }
    )

    # Remove the temporary file
    temp_path.unlink()

    # Returning the generated image URL
    return output[0]

# Streamlit app
def main():
    st.title("Generate Hyper-realistic Portrait from Drawing")

    # File uploader for the input image
    input_image = st.file_uploader("Upload a drawing of a face", type=["jpg", "png"])

    # Input box for the prompt
    prompt_text = st.text_area("Enter your prompt:", "a hyper-realistic human portrait based on the input drawing,human face, sharp focus, uhd, 4k")

    # Generate button
    if st.button("Generate Portrait") and input_image is not None:
        # Converting the uploaded file to bytes
        input_image_bytes = input_image.getvalue()

        # Generating image
        image_url = generate_image(input_image_bytes, prompt_text)

        # Displaying the image
        st.image(image_url, caption='Generated Portrait', use_column_width=True)

if __name__ =="__main__":
    main()
