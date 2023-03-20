# core pkgs
import streamlit as st

from PIL import Image
img = Image.open("data/poke.png")

st.set_page_config(page_title="Kumay's Page",
    page_icon=img, 
    initial_sidebar_state="collapsed") # or expanded / auto


# #Method 2 (DICTIONARY)
# page_config = {
#     "page_title":"KUMAYY",
#     "page_icon":"data/poke.png"
# }
# st.set_page_config(**page_config)


def main():
    st.title("hello MAMAA :heart:")
    st.sidebar.success("MENU")

if __name__ == "__main__":
    main()