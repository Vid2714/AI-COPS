import streamlit as st
import os
# Importing replicate library
import replicate
from dotenv import load_dotenv
load_dotenv()

os.environ["REPLICATE_API_TOKEN"] = "r8_XWegXlXa2svAZDmhk8J5Fd4k8wI1q8w11AmxD"
#REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")
#api = replicate.Client(api_token=REPLICATE_API_TOKEN)
# Function to generate image
def generate_image(input_text):
    # Input parameters
    input_params = {
        "width": 768,
        "height": 768,
        "prompt": input_text,
        "refine": "expert_ensemble_refiner",
        "disable_safety_checker": True,
        "negative_prompt": '''colored sketch, color photo, blurry, ugly, distorted, text, anime, worst quality, 
                                normal quality, low quality, low res, blurry, text, watermark, signature, borders, photo frame, 
                                logo, banner, extra digits, cropped, jpeg artifacts, signature, 
                                username, error, duplicate, ugly, horror, multiple images, multiple sketches, 
                                geometry, mutation, disgusting, bad anatomy, bad hands, three hands, 
                                three legs, bad arms, missing legs, missing arms, poorly drawn face, 
                                bad face, fused face, cloned face, worst face, three crus, extra crus, 
                                fused crus, worst feet, three feet, fused feet, fused thigh, three thigh, 
                                fused thigh, extra thigh, worst thigh, missing fingers, extra fingers, 
                                ugly fingers, long fingers, horn, extra eyes, huge eyes, 2girl, amputation, 
                                disconnected limbs, cartoon, cg, 3d, unreal, cartoon, anime''',
        "apply_watermark": False,
        "num_inference_steps": 25
    }

    # Running the replicate
    output = replicate.run(
        "stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b",
        input=input_params
    )

    # Returning the generated image URL
    return output[0]


# Streamlit app
def main():
    st.title("Mugshot Generator")

    # Input box for the prompt
    prompt_text = st.text_area("Enter Suspect Description:", "human face, sharp focus, uhd, 4k")

    # Generate button
    if st.button("Generate Mugshot"):
        # Generating image
        image_url = generate_image(prompt_text)

        # Displaying the image
        st.image(image_url, caption='Generated Mugshot', use_column_width=True)


if __name__ == "__main__":
    main()

