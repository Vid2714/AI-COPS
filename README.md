# AI-COPS
## Table of Contents

- [Dependencies](#Dependencies)
- [Setup](#Setup)
- [Project Description](#Project-Description)
- [Mugshot Generator](#Mugshot-Generator)
- [Drawing to Hyperrealistic Portrait](#Drawing-to-Hyperrealistic-Portrait)
- [Knowledge Graph Generator](#Knowledge-Graph-Generator)


## Dependencies

You'll need a OpenAI account, and a Replicate (replicate.com) account.

## Setup 

```
pip install -r req.txt
```
```
Edit the .env file to include your API keys.
```
```
streamlit run Mugshot-Generator.py
```

# Project Description

This project leverages generative AI models to create mugshots and hyper-realistic portraits from textual descriptions and drawings, while also generating knowledge graphs from prompts, aiding police and investigative agencies in their efforts.

# Mugshot Generator
- Utilizes the Stable Diffusion XL (SDXL) model from Stability AI to generate mugshots of suspects or perpetrators based on a textual description.
- Allows users to provide a detailed prompt, specifying the desired characteristics of the subject's face, such as gender, age, ethnicity, and other distinguishing features.
- The generated mugshots are highly realistic, with sharp focus and ultra-high definition (4K) quality.
  
# Drawing to Hyperrealistic Portrait
- Leverages the power of ControlNet, a technique that allows for better control over the image generation process by providing a reference image or drawing.
- Users can upload a drawing or sketch of a face, and the model will generate a hyper-realistic portrait based on the input.
- The generated portraits are highly detailed and lifelike, capturing the essence of the original drawing while enhancing it with realistic textures, lighting, and depth.

# Knowledge Graph Generator
- Utilizes the GPT-3.5-turbo model from OpenAI to extract relationships and entities from a given prompt.
- Based on the provided prompt, the model generates a list of relationships in the format [ENTITY 1, RELATIONSHIP, ENTITY 2].
- The extracted relationships are then visualized as a knowledge graph using the NetworkX library in Python, allowing for easy interpretation and understanding of the underlying connections.



