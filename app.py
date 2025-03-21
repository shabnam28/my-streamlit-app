import streamlit as st
import google.generativeai as genai
from openai import OpenAI
from apikey import google_gemini_api_key, openai_api_key
client = OpenAI (api_key=openai_api_key)
genai.configure()
from streamlit_carousel import carousel

single_image = dict(
    title= "",
    text ="",
    interval = None,
    img = ""
)

generation_config = {
      "temperature": 0.9,
       "top_p":1,
       "top_k":1,
       "max_output_token": 2048
    }

safety_settings = [
    {"category": "HATE_SPEECH", "threshold": "BLOCK_NONE"},
    {"category": "HARASSMENT", "threshold": "BLOCK_ONLY_HIGH"},
    {"category": "DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"}
]
print("Safety Settings:", safety_settings)
#setting up model
model = genai.GenerativeModel(
    model_name="gemini-pro",
    generation_config=generation_config, safety_settings=safety_settings)

#Set app to wide mode
st.set_page_config(layout="wide")

#title of our app
st.title('blog craft: Your AI Writing Companion')

#create subheader
st.subheader('Now you can craft perfect blogs with the help of AI - BlogCraft is your new AL Blog Campinion')

#sidebar for user input
with st.sidebar:
    st.title('Input Your blog Details')
    st.subheader('Enter Details of Blog You want to generate')

    #blog title
    blog_title = st.text_input("Blog Title")

    #Keywords 
    keywords= st.text_area("Keywords (comma-seperated)")

    #Number of words
    num_words= st.slider("Number of words", min_value=250, max_value=1000, step=250)
       
    #Number of images
    num_images = st.number_input("Number of image", min_value=1, max_value=3,step=1)

    prompt_parts = [
        f"Generate a comprehensive, engaging blog post relevant to the given title \"{blog_title}\" and keywords {keywords} make sure to incorporate these keywords in blog post. The blog should be appriximately\"{num_words}\" words"
    ]
    

    #submit button
    submit_button = st.button("Generate Button")

    if submit_button: 
        response = model.generate_content(prompt_parts)
        images= []
        images_gallery = []
        for i in range (num_images):
        
            image_response = client.images.generate(
            model="dall-e-3",
            prompt= f"Generate a Blog Post Image on the title {blog_title}",
            size= "1028x1024",
            quality= "standard", 
            n=1
        )
        new_image = single_image.copy()
        new_image["title"] = f"image {i+1} "
        new_image["text"] = f" {blog_title}"
        new_image["img"] = image_response.data[0].url
        images_gallery.append(new_image)
    
    st.title("Your Blog IMAGES ARE HERE: ")
    carousel(items=images_gallery,width=1)
    st.title("Your Blog POST IS HERE: ")
    st.write(response.text)
    
