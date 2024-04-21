import streamlit as st
import lib.const as const
from lib import utils
import streamlit_antd_components as sac


def main():
    
    utils.setup_page("Hello", "# Welcome to Streamlit! 👋", "👋")
    st.sidebar.success("Select a demo above.") 
    utils.show_markdown('./docs/Home_Page_description.md')
    st.snow()
    sac.divider(label='Home Page', icon='house', align='center', color='gray')
    sac.rate(label='Give a Rating!', value=3.0, align='left')
    sac.buttons([
        sac.ButtonsItem(label='Page Link', icon='book', href='https://nicedouble-streamlitantdcomponentsdemo-app-middmy.streamlit.app/'),
        sac.ButtonsItem(label='Teams Contact', icon='microsoft-teams', color="#5864A6"),
        sac.ButtonsItem(label='Slack Contact', icon='slack', color="#ECB32D"),
        sac.ButtonsItem(label='google', icon='google', color='#25C3B0', href='http://www.google.com'),
        sac.ButtonsItem(label='Github', icon='github',color='#171a19')
    ], label='Link', align='left',variant='filled')
if __name__ == "__main__":
    main()