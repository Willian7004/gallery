# Gallery

### 项目说明

为了优化项目结构，本人拆分了new-homepage项目，本项目包含展示类内容，原项目保留在Streamlit Cloud但不再更新。

本项目已部署到Streamlit Cloud，域名为https://william7004-blog.streamlit.app/

### 使用python部署
1.安装依赖
```
pip install -r requirements.txt
```
2.运行应用
```
streamlit run streamlit_app.py
```

### 使用docker部署
1.创建docker
```
docker build . -t new-homepage
```
2.运行docker
```
docker run -p 8501:8501 new-homepage
```

