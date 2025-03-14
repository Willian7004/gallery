import os
import re

# 定义正则表达式模式，匹配单独的换行符（前后都不是换行符）
pattern = re.compile(r'(?<!\n)\n(?!\n)')

# 遍历当前目录下的所有.txt文件
for filename in os.listdir('.'):
    if filename.endswith('.txt'):
        # 读取文件内容
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # 替换单独的换行符为两个换行符
        modified_content = pattern.sub('\n\n', content)
        
        # 将修改后的内容写回文件
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(modified_content)
