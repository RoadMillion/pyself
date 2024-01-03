import pandas as pd

# 读取 Excel 文件
file_path = '../files/etc异常统计.xlsx'
df = pd.read_excel(file_path)

# 使用 pivot_table 转换数据
result = df.pivot_table(index=['日期', '港口'], columns='hasPrice', values='数量', aggfunc='sum', fill_value=0).reset_index()

# 重命名列
result.columns.name = None
result.rename(columns={'有价格': '有价格的数量', '无价格': '无价格的数量'}, inplace=True)

# 输出结果
print(result)

# 如果需要将结果保存到新的 Excel 文件
output_file = 'output.xlsx'
result.to_excel(output_file, index=False)
