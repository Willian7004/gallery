import os
import random
import streamlit as st
from glob import glob

st.set_page_config(layout="wide")
with st.expander("YuE音乐集 （展开项目说明）"):
    st.write("本项目内容为本人使用YuE生成的音乐。通过sgsdxzy/YuE-exllamav2项目进行部署，stage1模型使用4.25bpw版本，stage2模型使用8.0bpw版本，显存门槛约为6g。提示词使用Qwq 32b创建，其中风格提示词使用官方的说明、参考词汇和示例作为提示词进行创建，歌词根据风格提示词、官方说明和示例创建并根据长度进行筛选,本页使用风格提示词作为标题。生成按默认参数，调低了batch size和cache以减少显存占用。标题使用风格提示词。歌词不使用连续两次换行，在这里为了能正常显示换行进行了转换。生成效果方面，YuE生成慢一些但效果比Stable Audio Open等模型好很多，虽然稳定性和音质一般但总体上达到可用水平。")
# 获取音乐文件夹路径
music_dir = "files/music"

# 获取所有有效的音乐文件及其对应的文本文件
valid_files = []
for mp3_file in glob(os.path.join(music_dir, "*.mp3")):
    # 提取文件编号
    filename = os.path.basename(mp3_file)
    number_str = os.path.splitext(filename)[0]
    
    if number_str.isdigit():
        number = int(number_str)
        genre_file = os.path.join(music_dir, f"genre{number}.txt")
        lyrics_file = os.path.join(music_dir, f"lyrics{number}.txt")
        
        if os.path.exists(genre_file) and os.path.exists(lyrics_file):
            valid_files.append({
                "number": number,
                "mp3": mp3_file,
                "genre": genre_file,
                "lyrics": lyrics_file
            })

# 按数字排序
valid_files.sort(key=lambda x: x["number"])

# 创建分页选项
total_files = len(valid_files)
total_pages = (total_files + 9) // 10  # 每页10个文件

options = ["随机"]
options.extend([f"Page {i+1}" for i in range(total_pages)])
selected_option = st.selectbox("选择页面或随机播放", options)

# 根据选择获取文件列表
if selected_option == "随机":
    selected_files = random.sample(valid_files, min(10, total_files))
else:
    page = int(selected_option.split()[-1]) - 1
    start = page * 10
    end = start + 10
    selected_files = valid_files[start:end]

# 显示文件内容
for file_info in selected_files:
    st.divider()
    #st.subheader(f"文件编号: {file_info['number']}")
    with open(file_info["genre"], "r") as f:        
        st.subheader(f.read())
    # 显示音频播放器
    st.audio(file_info["mp3"], format="audio/mp3")
    with open(file_info["lyrics"], "r") as f:
        with st.container(border=True):
            st.write(f.read())
