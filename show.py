import pandas as pd
import streamlit as st
import os

#  pip install -i https://pypi.tuna.tsinghua.edu.cn/simple streamlit
# streamlit version

# 设置页面标题
st.title('华北医疗邢台总医院')
# 输出一行文字
st.write("欢迎使用预住院日间手术报表！")

data_directory = 'Data'

# 获取 Data 目录下所有的.xlsx 文件
excel_files = [f for f in os.listdir(data_directory) if f.endswith('.xlsx')]

# 提取文件名作为选项
file_name_options = [f[:-5] for f in excel_files]

Report = st.selectbox(
    label='请选择要看的文档',
    options=file_name_options,
    format_func=str,
    help='选择一个文件名以查看相应内容'
)

selected_file_path = os.path.join(data_directory, f'{Report}.xlsx')

if os.path.exists(selected_file_path):
    xlsx = pd.ExcelFile(selected_file_path)
    sheet_names = xlsx.sheet_names
    selected_sheet = st.selectbox(
        label='请选择要查看的工作表',
        options=sheet_names,
        format_func=str
    )
    df = pd.read_excel(selected_file_path, sheet_name=selected_sheet)
    st.write(df)
else:
    st.write(f'找不到名为 {Report} 的文件。')