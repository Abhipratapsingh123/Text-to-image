import requests  
import streamlit as st

# Define the URL for the image generation API
url = "https://open-ai21.p.rapidapi.com/texttoimage2"

# Define the headers for the API request
headers = {
    "x-rapidapi-key": "4397f85e77mshaf2c5c3aca06607p187fcdjsnb57f03614d8c",
    "x-rapidapi-host": "open-ai21.p.rapidapi.com",
    "Content-Type": "application/json"
}

# Streamlit app header
st.title("Image Generator using Text")

# Add a text input for the user to enter their prompt
user_input = st.text_input("Enter a description:", "A Dog")

# When the button is pressed, send the request to the API
if st.button("Generate Image"):
    payload = {
        "text": user_input,
        "width": 512,
        "height": 512,
        "steps": 10
    }
    
    response = requests.post(url, json=payload, headers=headers)

    # Print the raw response for debugging
    # st.write("API Response:", response.json())

    # If the API request is successful, display the image
    if response.status_code == 200:
        image_data = response.json()  # Get the response as JSON
        
        # Check if 'generated_image' is in the response
        if "generated_image" in image_data:
            image_url = image_data["generated_image"]
            # Display the generated image with use_container_width
            st.image(image_url, caption=f"Generated image for: {user_input}", use_container_width=True)
        else:
            st.error("Image URL not found in the response.")
    else:
        st.error(f"Error: {response.status_code}, {response.text}")
