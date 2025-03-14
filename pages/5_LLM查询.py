import os
import glob
import random
import streamlit as st
st.set_page_config(layout="wide")
def get_md_files():
    """获取files目录下所有以数字命名的md文件"""
    files = []
    for filepath in glob.glob("files/llm-inquiry/*.md"):
        try:
            filename = os.path.basename(filepath)
            num = int(filename.split('.')[0])
            files.append((num, filepath))
        except (ValueError, IndexError):
            continue
    return sorted(files, key=lambda x: x[0])

def display_files(file_list):
    """显示文件列表内容"""
    for num, filepath in file_list:
        with st.container(height=350):
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                st.markdown(content)
            except Exception as e:
                st.error(f"读取文件失败: {str(e)}")

with st.expander("LLM查询 （展开项目说明）"):
    st.write("本项目用于展示我使用LLM查询一些难检索的问题的记录。一些问题由于位于一个关键词所包含的内容的细节、涉及多个搜索关键词的内容或需要查找的历史内容被新闻覆盖，使用LLM回答相比搜索引擎有优势。本项目主要展示我使用LLM解答的这类问题，总体偏向杂谈形式。内容筛选方面，排除了一些可能出现事实错误的回答。使用过的LLM包括deepseek v2.5、deepseek v3、deepseek r1 lite preview和deepseek r1,近期改用了QwQ 32b。重构后增加了随机选择文件和搜索功能。")

# 第一行布局
col1, col2 = st.columns(2)
with col1:
    mode = st.selectbox("选择模式", ["选择页面", "随机", "搜索"], key="mode")

files = get_md_files()


if mode == "选择页面":
    if files:
        max_num = max(f[0] for f in files)
        page_options = []
        for i in range(0, max_num + 1, 10):
            start = i + 1
            end = i + 10
            page_options.append(f"{start}-{end}")
        with col2:    
            selected_range = st.selectbox("选择范围", page_options)
        start, end = map(int, selected_range.split("-"))
        selected_files = [f for f in files if start <= f[0] <= end]
        display_files(selected_files)
    else:
        st.warning("没有找到任何文件")

elif mode == "随机":
    if files:
        random_files = random.sample(files, min(10, len(files)))
        display_files(random_files)
    else:
        st.warning("没有找到任何文件")

elif mode == "搜索":
    with col2:
        search_term = st.text_input("输入搜索关键词")
    if search_term:
        matched_files = []
        for num, path in files:
            try:
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                    if search_term in content:
                        matched_files.append((num, path))
            except Exception as e:
                st.error(f"读取文件失败: {str(e)}")
        if matched_files:
            display_files(matched_files)
        else:
            st.warning("没有找到匹配的文件")

