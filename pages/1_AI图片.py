import os
import random
import streamlit as st
st.set_page_config(layout="wide")
with st.expander("Hunyuan Video图集 （展开项目说明）"):
    st.write("本项目内容为本人使用Hunyuan Video生成的有提示词的图片内容，并覆盖了因为无提示词导致效果一般的Hunyuan Video Gallery Without Prompt项目。由于改用了q6_k精度的模型，细节比之前的Hunyuan Video Gallery项目中的好一些，此外复用了这一项目的代码。提示词方面，复用了之前使用Flux.1的提示词，移除了生成效果一般的内容，也添加了一些新的提示词")
# 获取当前目录下files文件夹中的所有文件夹
def get_folders():
    base_dir = "files/gallery1"
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    folders = [f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f))]
    return folders

# 获取指定文件夹中的所有jpg文件
def get_images(folder):
    base_dir = "files/gallery1"
    folder_path = os.path.join(base_dir, folder)
    images = [f for f in os.listdir(folder_path) if f.endswith(('.jpg'))]
    return images

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
        
        # 获取该文件夹中的所有图片
        images = get_images(selected_folder)
        if images:
            # 在页面上显示图片
            for image in images:
                image_path = os.path.join("files/gallery1", selected_folder, image)
                st.image(image_path)
        else:
            st.write("该文件夹中没有图片文件。")
    else:
        st.write("files文件夹中没有子文件夹。")
else:
    # 如果未选中“随机选择文件夹”，在侧边栏创建单选按钮
    folders = get_folders()
    if folders:
        selected_folder = st.sidebar.radio("选择文件夹", folders)
        
        # 获取该文件夹中的所有图片
        images = get_images(selected_folder)
        if images:
            # 在页面上显示图片
            for image in images:
                image_path = os.path.join("files/gallery1", selected_folder, image)
                st.image(image_path)
        else:
            st.write("该文件夹中没有图片文件。")
    else:
        st.write("files文件夹中没有子文件夹。")
  
