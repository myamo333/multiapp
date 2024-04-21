import streamlit as st
import subprocess
from lib import utils

def toggle_admin_mode():
    return st.sidebar.toggle('管理者モード (工事中)')

def file_uploader():
    uploaded_file = st.file_uploader("#### ①ファイルをアップロードしてください")
    return uploaded_file



def test_lib_functions():
    st.sidebar.write(utils.sub_process("libフォルダのutils.pyで宣言している関数を実行できるかを確認。表示されれば実行できています"))
    utils.sub_process2("libフォルダのutils.pyで宣言している関数でstreamlitのコードを実行。表示されれば実行できています")

def execute_error_check(tag, uploaded_file):
    output_text = ""
    st.markdown("#### ③エラーチェックを実行したい場合、下記ボタンを押してください")
    disable_flg = tag is None or uploaded_file is None
    if st.button(":technologist:エラーチェックを実行", type="primary", help="選択したタグの要件について、エラーチェックを実行します", disabled=disable_flg):
        with st.spinner('Wait for it...'):
            try:
                process = subprocess.run(["python", "../test/src/test.py"], capture_output=True, text=True, check=True)
                output_text = process.stdout
                with st.expander("test.pyスクリプトの実行結果:"):
                    st.code(output_text.strip(), language='text')
            except subprocess.CalledProcessError as e:
                st.error(f"エラーが発生しました: {e.output}")
            except subprocess.TimeoutExpired:
                st.error("タイムアウトしました。")

def show_error_log(err_log_path):
    with open(err_log_path, "r") as f:
        err_log_content = f.read()

    st.write("#### ④err.logファイルの内容:")
    st.code(err_log_content, language='text')


def main():
    utils.setup_page("Test (Construction)", "# Test", "🛠️")
    utils.show_description('ウェブアプリの説明',"""
    このウェブアプリは、err.logファイルの内容を表示するものです。
    """)
    select_list = ['タグ1', 'タグ2', 'タグ3','test_tag']
    uploaded_file =file_uploader()
    if  toggle_admin_mode():
        st.write("### 管理者モード (工事中)")
        utils.show_html("../test/output/タグ1/test.html")
    else:
        #test_lib_functions()
        tag = utils.select_tag(select_list, '#### ②タグを選択してください', "タグを選択もしくは入力してください")
        execute_error_check(tag,uploaded_file)
        show_error_log("./output/err.log")

if __name__ == "__main__":
    main()
