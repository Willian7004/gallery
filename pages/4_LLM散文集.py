import streamlit as st
import os
import random
from pathlib import Path
st.set_page_config(layout="wide")
with st.expander("LLM散文集 （展开项目说明）"):
    st.write("有网友实测Deepseek R1的思维链能带来写作能力优势，我确认有优势后决定用于写作。目前规划的内容包括写关于我之前的谷歌地球项目中的较大的城市以及中国各省省会的散文，并使用Fish Speech1.5合成音频。")

# 获取文件列表
def get_files():
    files_dir = Path("files/articles-by-llm")
    txt_files = sorted(files_dir.glob("*.txt"))
    return txt_files

# 显示文件内容
def display_file(file_path):
    st.divider()
    # 显示文件名
    file_name = file_path.stem
    st.subheader(file_name)
    
    # 显示MP3文件
    mp3_path = file_path.with_suffix(".mp3")
    if mp3_path.exists():
        st.audio(str(mp3_path))
    
    # 显示文本内容
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    with st.container(border=True):
        st.markdown(content)
        


txt_files = get_files()

# 第一行布局
col1, col2 = st.columns([1, 1])
with col1:
    mode = st.selectbox("选择模式", ["选择页面", "随机", "搜索"])

# 根据模式处理文件列表
if mode == "选择页面":
    total_pages = (len(txt_files) + 9) // 10
    with col2:
        page = st.selectbox("选择页数", range(1, total_pages + 1)) - 1
    files_to_show = txt_files[page*10 : (page+1)*10]

elif mode == "随机":
    files_to_show = random.sample(txt_files, min(10, len(txt_files)))

elif mode == "搜索":
    with col2:
        search_term = st.text_input("输入搜索关键词")
    files_to_show = [f for f in txt_files if search_term.lower() in f.stem.lower()]

# 显示文件内容
for file_path in files_to_show:
    display_file(file_path)
    

