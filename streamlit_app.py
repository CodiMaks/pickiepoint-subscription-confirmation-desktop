import streamlit as st

st.set_page_config("Subscription confirmation", "pickiepoint_logo_profile_picture.jpg")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.title("Thanks for your subscription")
st.write("")

st.image("tick.png", use_container_width=True)
st.write("")
st.write("")

st.caption('<span style="font-size:25px; font-weight:bold; color:white;">\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0You are all set</span>', unsafe_allow_html=True)
st.caption('<span style="font-size:25px; font-weight:bold; color:white;">\u00A0\u00A0\u00A0\u00A0Start picking the main \u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0 points</span>', unsafe_allow_html=True)
st.subheader("")

return_to_website = st.button("Let's go", type="primary", use_container_width=True)
st.text("")
st.image("pickiepoint_logo_profile_picture.jpg", width=200)
