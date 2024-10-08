import streamlit as st

st.set_page_config("Subscription confirmation", "pickiepoint_logo_profile_picture-removebg-preview (1).png")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.caption('<span style="font-size:45px; font-weight:bold; color:white;">\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0Thanks for your subscription</span>', unsafe_allow_html=True)
st.write("")

col1, col2, col3 = st.columns(3)
with col2:
    st.image("tick.png", width=230)
    st.write("")
    st.write("")

st.caption('<span style="font-size:30px; font-weight:bold; color:white;">\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0You are all set</span>', unsafe_allow_html=True)
st.caption('<span style="font-size:30px; font-weight:bold; color:white;">\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0Start picking the main points</span>', unsafe_allow_html=True)
st.subheader("")

sub_col1, sub_col2, sub_col3 = st.columns(3)
with sub_col2:
    return_to_website = st.button("Let's go", type="primary", use_container_width=True)
    st.text("")
    st.image("pickiepoint_logo_profile_picture-removebg-preview (1).png", width=240)
