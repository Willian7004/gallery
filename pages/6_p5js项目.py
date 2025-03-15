import streamlit as st
import json
import os
import streamlit.components.v1 as components
st.write("本页面用于显示我的p5js项目，使用Deepseek R1或QwQ 32b编写。选择以这一形式展示p5js项目而没有展示其它html项目的原因是streamlit的iframe不适合使用本地页面而p5js提供在线部署功能。需要离线使用可以用https://github.com/Willian7004/p5js-programs ")
# 读取索引文件
with open('files/p5index.json', 'r', encoding="utf-8") as f:
    index_data = json.load(f)['index']

# 创建侧边栏单选按钮
names = [item['name'] for item in index_data]
selected_name = st.sidebar.radio("选择项目", names)

# 获取选中项目的数据
selected_item = next(item for item in index_data if item['name'] == selected_name)
url = selected_item['url']

# 构建文件路径
txt_file = os.path.join('files', 'p5programs', f"{selected_name}.txt")
js_file = os.path.join('files', 'p5programs', f"{selected_name}.js")

# 显示TXT文件内容
try:
    with open(txt_file, 'r', encoding="utf-8") as f:
        txt_content = f.read()
    with st.expander("项目说明和提示词", expanded=False):
        st.code(txt_content, language='text')
except FileNotFoundError:
    st.warning(f"未找到 {selected_name}.txt 文件")

# 显示JS文件内容
try:
    with open(js_file, 'r', encoding="utf-8") as f:
        js_content = f.read()
    with st.expander("源码（js文件）", expanded=False):
        st.code(js_content, language='javascript')
except FileNotFoundError:
    st.warning(f"未找到 {selected_name}.js 文件")

# 显示URL和iframe
st.write(f"需要全屏查看或不兼容iframe可使用以下地址：[{url}]({url})")
st.components.v1.html(
    f"""
    <iframe 
        src="{url}" 
        width="960" 
        height="540" 
        frameborder="0" 
        allowfullscreen
    ></iframe>
    """,
    height=720,
    scrolling=True
)