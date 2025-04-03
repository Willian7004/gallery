import os
import random
import streamlit as st
from PIL import Image

# 初始化session state
if 'selected_folder' not in st.session_state:
    st.session_state.selected_folder = None
if 'random_folder' not in st.session_state:
    st.session_state.random_folder = None

# 获取文件夹列表
def get_folders():
    base_path = os.path.join("files", "gallery1")
    if not os.path.exists(base_path):
        return []
    return [f for f in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, f))]

# 获取图片并分类
def get_images(folder):
    base_path = os.path.join("files", "gallery1", folder)
    if not os.path.exists(base_path):
        return [], []
    
    width_gt_height = []
    height_gt_width = []
    
    for file in os.listdir(base_path):
        if file.lower().endswith(('.png', '.jpg', '.jpeg')):
            try:
                img_path = os.path.join(base_path, file)
                with Image.open(img_path) as img:
                    width, height = img.size
                    if width > height:
                        width_gt_height.append(img_path)
                    else:
                        height_gt_width.append(img_path)
            except Exception as e:
                continue
    return width_gt_height, height_gt_width

# 下载按钮生成器
def create_download_button(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
    st.download_button(
        label="下载图片",
        data=data,
        file_name=os.path.basename(image_path),
        key=f"btn_{os.path.basename(image_path)}"
    )

# 侧边栏
with st.sidebar:
    random_mode = st.toggle("随机选择文件夹")
    
    folders = get_folders()
    if not folders:
        st.error("未找到任何文件夹")
        st.stop()

    if random_mode:
        if st.button("刷新") or not st.session_state.random_folder:
            st.session_state.random_folder = random.choice(folders)
        selected_folder = st.session_state.random_folder
    else:
        selected_folder = st.radio("选择文件夹", folders)
        st.session_state.selected_folder = selected_folder

# 主界面
with st.expander("Cogview4图集 （展开项目说明）"):
    st.write("本项目内容为本人使用Cogview4生成的图片，包含宽高比为16：9和9：16的图片。由于分辨率提高到1920x1080,提供了下载功能。")

if selected_folder:
    show_download = st.checkbox("显示下载按钮")
    
    # 获取分类后的图片
    width_gt, height_gt = get_images(selected_folder)
    
    # 显示宽度>高度的图片
    if width_gt:
        for i, img_path in enumerate(width_gt):
                st.image(img_path)
                if show_download:
                    create_download_button(img_path)
    
    # 显示高度>宽度的图片（分两列）
    if height_gt:
        col1, col2 = st.columns(2)
        for i, img_path in enumerate(height_gt):
            with col1 if i % 2 == 0 else col2:
                st.image(img_path)
                if show_download:
                    create_download_button(img_path)
else:
    st.warning("请先选择一个文件夹")
