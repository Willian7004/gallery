import os
import random
import streamlit as st
import re
st.set_page_config(layout="wide")
with st.expander("Wan2.1 视频集 （展开项目说明）"):
    st.write("本项目内容为本人使用Wan2.1 1.3b生成的视频，复用了之前在社交媒体发布的使用其它模型生成的视频的提示词，文件夹以主题命名，5个视频为1组并在每个视频下面显示提示词。新添加的内容在每个主题只出5个视频。")
# 获取当前目录下files文件夹中的所有文件夹
def get_folders():
    base_dir = "files/gallery2"
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    folders = [f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f))]
    return folders

# 获取指定文件夹中的所有视频文件
def get_videos(folder):
    base_dir = "files/gallery2"
    folder_path = os.path.join(base_dir, folder)
    videos = [f for f in os.listdir(folder_path) if f.endswith(('.mp4', '.avi', '.mkv'))]
    return videos

# 在侧边栏创建复选框
random_folder = st.sidebar.toggle("随机选择文件夹", value=True)

# 根据复选框的状态显示不同的内容
if random_folder:
    # 如果选中了“随机选择文件夹”，显示刷新按钮
    if st.sidebar.button("刷新"):
        pass  # 刷新按钮的逻辑在下面处理

    # 获取所有文件夹
    folders = get_folders()
    if folders:
        # 随机选择一个文件夹
        selected_folder = random.choice(folders)
        st.sidebar.write(f"当前选择的文件夹: {selected_folder}")

        # 获取该文件夹中的所有视频
        videos = get_videos(selected_folder)
        if videos:
            # 在页面上显示视频
            for video in videos:
                video_path = os.path.join("files/gallery2", selected_folder, video)
                st.video(video_path,loop=True, autoplay=True)
                # 使用正则表达式匹配并打印提示词
                pattern = r'）\\(.*?)\_'
                match = re.search(pattern,video_path)
                if match:
                    st.write(match.group(1))
  
        else:
            st.write("该文件夹中没有视频文件。")
    else:
        st.write("files文件夹中没有子文件夹。")
else:
    # 如果未选中“随机选择文件夹”，在侧边栏创建单选按钮
    folders = get_folders()
    if folders:
        selected_folder = st.sidebar.radio("选择文件夹", folders)
        
        # 获取该文件夹中的所有视频
        videos = get_videos(selected_folder)
        if videos:
            # 在页面上显示视频
            for video in videos:
                video_path = os.path.join("files/gallery2", selected_folder, video)
                st.video(video_path,loop=True, autoplay=True)
                #使用正则表达式匹配并打印提示词
                pattern = r'）\\(.*?)\_'
                match = re.search(pattern,video_path)
                if match:
                    st.write(match.group(1))
    
        else:
            st.write("该文件夹中没有视频文件。")
    else:
        st.write("files文件夹中没有子文件夹。")
        
 
