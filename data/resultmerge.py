

import pandas as pd
import os

# 指定目录
directory = '../files/merge'

# 获取目录下所有的 Excel 文件
excel_files = [f for f in os.listdir(directory) if f.endswith('.xlsx') or f.endswith('.xls')]

# 读取并合并所有的 Excel 文件
data_frames = []
for file in excel_files:
    data = pd.read_excel(os.path.join(directory, file))
    data_frames.append(data)

merged_data = pd.concat(data_frames)

# 写入新的 Excel 文件
merged_data.to_excel(directory + '/result.xlsx', index=False)

