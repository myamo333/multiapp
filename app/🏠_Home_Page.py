import streamlit as st
import lib.const as const
from lib import utils


def main():
    utils.setup_page("Hello", "# Welcome to Streamlit! 👋", "👋")
    st.sidebar.success("Select a demo above.") 
    utils.show_markdown('./docs/Home_Page_description.md')

if __name__ == "__main__":
    main()