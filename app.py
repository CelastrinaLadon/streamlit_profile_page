import streamlit as st
from PIL import Image
import requests
from io import BytesIO

import json 
with open('./experience.json','r', encoding='utf-8') as fp:
    data = json.load(fp)


# Profile data
PROFILE_IMAGE_URL = data['profile_url']
NAME = data['name']
TITLE = data['title']
EMAIL = data['email']
LOCATION = data['location']
SUMMARY = data['summary']

# Streamlit App
st.set_page_config(page_title="Thotsaphon Sirikutta Profile", page_icon=":wave:", layout="centered")
col1, col2 = st.columns([0.8, 0.2])

with col2:
    # Profile Image and Header
    if PROFILE_IMAGE_URL:
        response = requests.get(PROFILE_IMAGE_URL)
        image = Image.open(BytesIO(response.content))
        st.image(image, width=20, use_container_width=True)

with col1:
    st.title(NAME)
    st.subheader(TITLE)
    col_t1, col_t2 = st.columns([0.5, 0.5])
    with col_t1:
        st.write(f":link: [LinkedIn](https://www.linkedin.com/in/thotsaphon-sirikutta-82511a154/)")
        st.write(f":email: [EMAIL](mailto:{EMAIL})")
        st.write(f":round_pushpin: {LOCATION}")
    with col_t2:
        st.write(f":link: [Download CV](https://www.linkedin.com/in/thotsaphon-sirikutta-82511a154/)")
    
    

# Summary Section
st.divider()

con_1 =  st.container(border=False)
with con_1:
    st.header("About Me")
    st.write(SUMMARY)

#     # Skills Section
#     st.markdown("---")
#     st.header("Key Skills")
#     st.write(
#         "- Leadership and team management\n"
#         "- Data engineering and development\n"
#         "- Cloud technologies and DevOps\n"
#         "- Programming and software development\n"
#         "- Data analytics and visualization\n"
#         "- Standards and compliance\n"
#         "- Strategic and analytical thinking"
#     )



st.divider()
st.header("Professional Experience")
for data in data['lst_exp']:
    second_line = f"{data.get('company', '')} – {data.get('location', '')} | {data.get('start', '')} – {data.get('end', '')}"
    with st.container(border=True):
        st.subheader(data['roles'])
        st.write(second_line)
        st.write(*data['details'])
        st.write('\n')

# Footer
st.divider()
st.markdown(
    "<small>Built with ❤️ using [Streamlit](https://streamlit.io)</small>",
    unsafe_allow_html=True
)
