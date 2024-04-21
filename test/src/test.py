import time
import streamlit as st
import traceback

def sub_process(value):
    return value

def log_error(error_message, error_file="././output/err.log"):
    with open(error_file, "w") as file:
        file.write("=" * 50 + "\n")
        file.write("Error Message:\n")
        file.write(error_message + "\n")
        file.write("Traceback:\n")
        traceback.print_exc(file=file)
        file.write("=" * 50 + "\n")

total_iterations = 10

for i in range(total_iterations):
    # 何らかの処理
    time.sleep(0.1)
    # 進捗情報を出力
    progress = (i + 1) / total_iterations * 100
    print(f"進捗: {progress}% 完了")
    
log_error("エラーだよ")