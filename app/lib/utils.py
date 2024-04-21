import streamlit as st
from lib import const

def sub_process(value):
    return value

def sub_process2(value):
    st.sidebar.write(value)# ファイルアップロードのUIを作成
    uploaded_file = st.file_uploader("ファイルをアップロードしてください", type=['xlsx'])

def setup_page(page_title, title, icon):
    st.set_page_config(page_title=page_title, page_icon=icon, layout="wide")
    st.markdown(const.HIDE_ST_STYLE, unsafe_allow_html=True)
    st.markdown(title)

def show_description(title,description):
    st.sidebar.title(title)
    st.sidebar.write(description)

def select_tag(select_list, message, help_message):
    tag = st.selectbox(
        message,
        select_list,
        None,
        help=help_message
    )
    return tag

def show_html(file_path):
    # HTMLファイルを読み込む
    with open(file_path, "r") as f:
        html_content = f.read()
    # HTMLを表示する
    st.components.v1.html(html_content, height=600, scrolling=True)
    
def show_markdown(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        markdown_text = f.read()
    st.markdown(markdown_text)
    