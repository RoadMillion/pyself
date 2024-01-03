import pandas as pd


def split_excel_file(file_path, output_dir, batch_size):
    # 读取Excel文件
    df = pd.read_excel(file_path, engine='openpyxl')

    # 获取标题（前两行）
    header = df.iloc[:1]

    # 计算拆分的文件数量
    num_files = (len(df) - 2) // batch_size + 1

    # 按批次拆分文件
    for i in range(num_files):
        start_row = 1 + i * batch_size
        end_row = 1 + (i + 1) * batch_size
        temp_df = df.iloc[start_row:end_row]
        output_file = f"{output_dir}/1split_{i + 1}.xlsx"

        # 保存标题和当前批次的数据到新的Excel文件
        with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
            pd.concat([header, temp_df]).to_excel(writer, index=False)


# 用法示例：
input_file = "../files/aaa.xlsx"  # 输入文件路径
output_directory = "../files"  # 输出文件夹路径
split_size = 400  # 每个拆分文件的行数（不包括标题）

split_excel_file(input_file, output_directory, split_size)
