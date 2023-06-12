import requests
import streamlit as st
import base64
import time

# Use the full page instead of a narrow central column
st.set_page_config(layout="wide")

# Powered by OctoML displayed in top right
st.image("images/octoml-octopus-white.png", width=100)
st.markdown("""
<style>
.powered-by {
    position: absolute;
    top: -130px;
    right: 0;
    float: right;
}
.powered-by span {
    padding-right: 5;
</style>
<div class="powered-by">
<span>Powered by </span> <a href="https://octoai.cloud/"><img src="https://i.ibb.co/T1X1CHG/octoml-octo-ai-logo-vertical-container-white.png" alt="octoml-octo-ai-logo-vertical-container-white" border="0" width="200"></a>
</div>
""", unsafe_allow_html=True)

# Create a title and description for the app
st.title("Stable Diffusion Image Generation Playground 🖼️🤖")
st.subheader("Directions: Use the Stable Diffusion Playground to learn how parameters affect image generation.")
st.markdown("Example: Each scheduler and number of steps selected below is capable of producing high-quality results. Try increasing the Number of Steps or CFG Scale to see how the images change!")


# Create a prompt for the image
st.header("Prompt")
prompt = st.text_input("Text for Image Generation", "A photo of an octopus playing chess")

# Create three columns for the inputs and outputs
col1, col2, col3 = st.columns(3)

# Create user inputs for negative prompt, guidance scale, number of inference steps, and scheduler for each column
with col1:
    st.header("Image 1 Parameters")
    negative_prompt_1 = st.text_input("Negative Prompt", "Blurry photo, distortion, low-res, bad quality", help="Use negative prompts to specify image characteristics that represent the opposite of the output that you want.")
    num_inference_steps_1 = st.number_input("Number of Inference/Sampling Steps", 1, 500, 20, help="Increase steps when you believe the quality is low.")
    scheduler_1 = st.selectbox("Select Scheduler", ["PNDM", "KLMS", "DDIM", "K_EULER", "K_EULER_ANCESTRAL", "DPMSolverMultistep"], index=5, help="Schedulers define the denoising process for stable diffusion, and taken together with the number of inference steps the choice indicates a denoising speed versus quality tradeoff.")
    guidance_scale_1 = st.slider("Classifier-Free Guidance (CFG) Scale", 1.0, 20.0, 7.5, help="Increase CFG scale when the generated image does not follow the prompt.")
    seed_1 = st.number_input("Starting Seed", min_value=0, value=42, help="Initialize generations with the same starting seed for more reproducible images")
    # Create a button to trigger the request for image 1
    if st.button("Generate image 1"):
        # Define the URL and the payload
        endpoint_url = "https://stable-diffusion-demo-kk0powt97tmb.octoai.cloud/predict"
        payload_1 = {
            "prompt": prompt,
            "negative_prompt": negative_prompt_1,
            "guidance_scale": guidance_scale_1,
            "num_inference_steps": num_inference_steps_1,
            "solver": scheduler_1,
            "seed": seed_1
        }
        # Record the start time
        start_time_1 = time.time()
        # Send a POST request and get the response
        response_1 = requests.post(endpoint_url, json=payload_1)
        # Record the end time
        end_time_1 = time.time()
        # Calculate the elapsed time
        elapsed_time_1 = end_time_1 - start_time_1
        # Extract the image data from the response
        image_data_1 = response_1.json()["image_0"]
        # Decode the base64 data and save it as image.png
        with open("generated-images/image1.png", "wb") as f:
            f.write(base64.b64decode(image_data_1))
        # Store the image data and the elapsed time in session state
        st.session_state.image_data_1 = image_data_1
        st.session_state.elapsed_time_1 = elapsed_time_1
        
    # Display the image in the app if it exists in session state
    if "image_data_1" in st.session_state:
        st.image("generated-images/image1.png")
    
    # Display the time in the app if it exists in session state
    if "elapsed_time_1" in st.session_state:
        st.write(f"Generation took {st.session_state.elapsed_time_1:.2f} seconds")


with col2:
    st.header("Image 2 Parameters")
    negative_prompt_2 = st.text_input("Enter a negative prompt for the image", "Dark photo, noise, pixelated, low contrast", help="Use negative prompts to specify image characteristics that represent the opposite of the output that you want.")
    num_inference_steps_2 = st.number_input("Number of Inference/Sampling Steps", 1, 500, 30, help="Increase steps when you believe the quality is low.")
    scheduler_2 = st.selectbox("Select Scheduler", ["PNDM", "KLMS", "DDIM", "K_EULER", "K_EULER_ANCESTRAL", "DPMSolverMultistep"], index=3, help="Schedulers define the denoising process for stable diffusion, and taken together with the number of inference steps the choice indicates a denoising speed versus quality tradeoff.")
    guidance_scale_2 = st.slider("Classifier-Free Guidance (CFG) Scale", 1.0, 20.0, 10.0, help="Increase CFG scale when the generated image does not follow the prompt.")
    seed_2 = st.number_input("Starting Seed", min_value=0, value=24, help="Initialize generations with the same starting seed for more reproducible images")
    # Create a button to trigger the request for image 2
    if st.button("Generate image 2"):
        # Define the payload
        endpoint_url = "https://stable-diffusion-demo-kk0powt97tmb.octoai.cloud/predict"
        payload_2 = {
            "prompt": prompt,
            "negative_prompt": negative_prompt_2,
            "guidance_scale": guidance_scale_2,
            "num_inference_steps": num_inference_steps_2,
            "solver": scheduler_2,
            "seed": seed_2
        }
        # Record the start time
        start_time_2 = time.time()
        # Send a POST request and get the response
        response_2 = requests.post(endpoint_url, json=payload_2)
        # Record the end time
        end_time_2 = time.time()
        # Calculate the elapsed time
        elapsed_time_2 = end_time_2 - start_time_2
        # Extract the image data from the response
        image_data_2 = response_2.json()["image_0"]
        # Decode the base64 data and save it as image.png
        with open("generated-images/image2.png", "wb") as f:
            f.write(base64.b64decode(image_data_2))
        # Store the image data and the elapsed time in session state
        st.session_state.image_data_2 = image_data_2
        st.session_state.elapsed_time_2 = elapsed_time_2
        
    # Display the image in the app if it exists in session state
    if "image_data_2" in st.session_state:
        st.image("generated-images/image2.png")
    
    # Display the time in the app if it exists in session state
    if "elapsed_time_2" in st.session_state:
        st.write(f"Generation took {st.session_state.elapsed_time_2:.2f} seconds")

with col3:
    st.header("Image 3 Parameters")
    negative_prompt_3 = st.text_input("Enter a negative prompt for the image", "Cartoonish photo, unrealistic colors, low details, bad lighting", help="Use negative prompts to specify image characteristics that represent the opposite of the output that you want.")
    num_inference_steps_3 = st.number_input("Number of Inference/Sampling Steps", 1, 500, 35, help="Increase steps when you believe the quality is low.")
    scheduler_3 = st.selectbox("Select Scheduler", ["PNDM", "KLMS", "DDIM", "K_EULER", "K_EULER_ANCESTRAL", "DPMSolverMultistep"], index=4, help="Schedulers define the denoising process for stable diffusion, and taken together with the number of inference steps the choice indicates a denoising speed versus quality tradeoff.")
    guidance_scale_3 = st.slider("Classifier-Free Guidance (CFG) Scale", 1.0, 20.0, 5.0, help="Increase CFG scale when the generated image does not follow the prompt.")
    seed_3 = st.number_input("Starting Seed", min_value=0, value=1, help="Initialize generations with the same starting seed for more reproducible images")
    # Create a button to trigger the request for image 3
    if st.button("Generate image 3"):
        # Define the URL and the payload
        endpoint_url = "https://stable-diffusion-demo-kk0powt97tmb.octoai.cloud/predict"
        payload_3 = {
            "prompt": prompt,
            "negative_prompt": negative_prompt_3,
            "guidance_scale": guidance_scale_3,
            "num_inference_steps": num_inference_steps_3,
            "solver": scheduler_3,
            "seed": seed_3
        }
        # Record the start time
        start_time_3 = time.time()
        # Send a POST request and get the response
        response_3 = requests.post(endpoint_url, json=payload_3)
        # Record the end time
        end_time_3 = time.time()
        # Calculate the elapsed time
        elapsed_time_3 = end_time_3 - start_time_3
        # Extract the image data from the response
        image_data_3 = response_3.json()["image_0"]
        # Decode the base64 data and save it as image.png
        with open("generated-images/image3.png", "wb") as f:
            f.write(base64.b64decode(image_data_3))
        # Store the image data and the elapsed time in session state
        st.session_state.image_data_3 = image_data_3
        st.session_state.elapsed_time_3 = elapsed_time_3
        
    # Display the image in the app if it exists in session state
    if "image_data_3" in st.session_state:
        st.image("generated-images/image3.png")
    
    # Display the time in the app if it exists in session state
    if "elapsed_time_3" in st.session_state:
        st.write(f"Generation took {st.session_state.elapsed_time_3:.2f} seconds")
