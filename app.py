import streamlit as st
import requests
import io
from PIL import Image

#Configuration
st.set_page_config(page_title="AI Art Studio", page_icon="🎨")

st.title("AI Art Studio")
st.caption("Generate AI images using Stable Diffusion (HF)")

#API Calls to Hugging Face Inference Endpoint
API_URL = "https://router.huggingface.co/hf-inference/models/stabilityai/stable-diffusion-xl-base-1.0"

API_KEY = "PLACE API KEY HERE"  
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

#Style Map
style_map = {
    "Realistic": (
        "photorealistic, ultra detailed, 8k resolution, DSLR photography, "
        "sharp focus, cinematic lighting, soft shadows, high dynamic range (HDR), "
        "35mm lens, depth of field, natural skin texture, realistic colors"
    ),

    "Anime": (
        "anime style, studio ghibli inspired, highly detailed, vibrant colors, "
        "soft shading, expressive characters, clean line art, cinematic composition, "
        "detailed background, dreamy lighting"
    ),

    "Cyberpunk": (
        "cyberpunk style, futuristic neon city, glowing lights, rain-soaked streets, "
        "high contrast lighting, holograms, reflective surfaces, ultra detailed, "
        "dark atmosphere, cinematic angle"
    ),

    "Oil Painting": (
        "oil painting, classical fine art style, rich textures, thick brush strokes, "
        "canvas grain, dramatic lighting, renaissance style, detailed composition, "
        "museum quality"
    ),

    "No Style": ""
}

style = st.selectbox("Choose style", list(style_map.keys()))
prompt = st.text_area("Enter prompt")

#Image Gen
def generate_image(prompt):
    full_prompt = prompt + ", " + style_map[style]

    response = requests.post(
        API_URL,
        headers=headers,
        json={"inputs": full_prompt},
        timeout=30
    )

    if response.status_code == 503:
        raise RuntimeError("Model is loading... try again in 10 seconds")

    if response.status_code == 404:
        raise RuntimeError("Model not found (check endpoint)")

    if response.status_code != 200:
        raise RuntimeError(response.text)

    return response.content

#Basic Streamlit UI
if st.button("Generate 🚀"):

    if not prompt.strip():
        st.warning("Enter a prompt")
        st.stop()

    with st.spinner("Generating... (first run may take ~15s)"):

        try:
            image_bytes = generate_image(prompt)

            img = Image.open(io.BytesIO(image_bytes)).convert("RGB")

            st.image(img, use_container_width=True)

            st.download_button(
                "Download Image",
                data=image_bytes,
                file_name="ai_art.png",
                mime="image/png"
            )

        except Exception as e:
            st.error(f"Error: {e}")