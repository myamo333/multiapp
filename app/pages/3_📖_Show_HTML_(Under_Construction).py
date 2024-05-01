import streamlit as st
from lib import utils
import pandas as pd
import json
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode

def show_df(tag, df):
    # 入力された文字列でフィルタリングを行う
    if "Test A" in df.columns and tag is not None:
        filtered_show = df[df["Test A"].astype(str).str.contains(tag, case=False, na=False)]
        if not filtered_show.empty:
            shows = filtered_show
        else:
            shows = df
    else:
        shows = df

    gb = GridOptionsBuilder.from_dataframe(shows)
    gb.configure_default_column(editable=True)
    gb.configure_selection(selection_mode="single", use_checkbox=True)
    grid_options = gb.build()
    data = AgGrid(shows, 
            gridOptions=grid_options, 
            enable_enterprise_modules=True, 
            allow_unsafe_jscode=True, 
            update_mode=GridUpdateMode.SELECTION_CHANGED)
    return data

def df_to_json(data):
    if data["selected_rows"] is not None:
        json_data = data["selected_rows"].reset_index(drop=True).to_json(orient='records').replace("[","").replace("]","")
        return json_data
        

#ベースのhtmlをエクセルの内容に置換する
def json_to_html(data, json_data, base_html):
    if json_data is not None:
        # HTMLファイルを読み込む
        with open(base_html, "r") as f:
            html_content = f.read()
        # JSON文字列を辞書型に変換
        json_dict = json.loads(json_data)
        # {}で囲まれた部分をデータで置換
        new_html = html_content.format(**json_dict)
        # 新しいHTMLを出力
        st.markdown("### 📄Preview Image")
        with st.container(border=True):
            st.components.v1.html(new_html, height=2000, scrolling=True)

def move_columns_to_front(df, columns):
    # 指定された列を一時的に切り出す
    moved_columns = df[columns]
    # 指定された列を削除
    df = df.drop(columns=columns)
    # 切り出した列を一番左側に挿入
    for column_name in reversed(columns):
        df.insert(0, column_name, moved_columns[column_name])
    return df

def main():

    utils.setup_page("Show HTML(Construction)", "# Show HTML", "📖")
    utils.show_description('ウェブアプリの説明',"""
    このウェブアプリは、HTMLファイルの内容を表示するものです。  
    """)
    select_list = ['test', 'test2', 'test3','test_tag']
    with st.sidebar.container():
        tag = utils.select_tag(select_list, '#### ①タグを選択してください', "タグを選択もしくは入力してください")
    tab1, tab2 = st.tabs(["Test tab", "Test tab2"])

    # 2つのデータフレームを作成
    df1 = pd.read_csv('./test/output/data3.csv', dtype=str)
    df1 = move_columns_to_front(df1, ["Test R","Test Q"])
    #df1 = move_column_to_front(df1, "Test Q")
    df2 = pd.read_csv('./test/output/data2.csv', dtype=str)

    #タブ1の処理
    with tab1:
        col1, col2 = st.columns([0.2,0.8])
        with col1:
            st.markdown('### 🔖dataFrame')
            data1 = show_df(tag, df1)
            json_data1 = df_to_json(data1)
        with col2:
            json_to_html(data1,json_data1,'./test/bese_html/base_html.html')

    #タブ2の処理
    with tab2:
        col3, col4 = st.columns([0.2, 0.8])
        with col3:
            st.markdown('### 🔖dataFrame')
            data2 = show_df(tag, df2)
            json_data2 = df_to_json(data2)
            

if __name__ == "__main__":
    main()