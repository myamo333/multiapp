import streamlit as st
from lib import utils

def main():
    utils.setup_page("Kanban", "# Kanban", "📖")
    utils.show_description('ウェブアプリの説明',"""
    このウェブアプリは、かんばんボードを表示するものです  
    """)
   # カラムのスタイルを定義
    col_todo_style = """
        background-color: lightgray;
        color: #000000;
        padding: 10px;
        border-radius: 5px;
    """
    col_in_progress_style = """
        background-color: lightgreen;
        color: #000000;
        padding: 10px;
        border-radius: 5px;
    """
    col_done_style = """
        background-color: gray;
        color: #000000;
        padding: 10px;
        border-radius: 5px;
    """

    # タスクのリスト
    tasks = {
        "todo":["Task 1", "Task 2"],
        "in_progress" : ["Task 3"],
        "done" : ["Task 4", "Task 5"]
    }

    # かんばんボードの各列を作成
    col_todo, col_in_progress, col_done = st.columns(3)

    # 各列にタスクカードを追加
    with col_todo:
        st.header("To Do")
        for task in tasks["todo"]:
            st.markdown(f'<div style="{col_todo_style}">{task}</div>', unsafe_allow_html=True)
            st.markdown("")


    with col_in_progress:
        st.header("In Progress")
        for task in tasks["in_progress"]:
           st.markdown(f'<div style="{col_in_progress_style}">{task}</div>', unsafe_allow_html=True)
           st.markdown("")

    with col_done:
        st.header("Done")
        for task in tasks["done"]:
           st.markdown(f'<div style="{col_done_style}">{task}</div>', unsafe_allow_html=True)
           st.markdown("")


if __name__ == "__main__":
    main()