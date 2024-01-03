import pandas as pd

import pymysql
from tqdm import tqdm

# 数据库连接配置，请根据实际情况进行修改
db_config = {
    "host": "10.0.19.165",
    "port": 13306,
    "user": "parking_lot_dev",
    "passwd": "H5iTz1ywMdunlc9zEL",
    "db": "parking_lot_dev",
    "charset": "utf8"
}

def add_spot(floor_id, spot_number):
    cursor = conn.cursor()
    sql = (f"insert into yt_spot(create_by, name,type,is_chargeable,parking_lot_id,status,location_id,arrangement) " +
           f"values('1', '{spot_number}', 'FULL', 'NO',4,'idle',{floor_id},'parallel')")
    cursor.execute(sql)
    # get id
    spot_id = cursor.lastrowid
    conn.commit()

# 建立数据库连接
conn = pymysql.connect(**db_config)
# 一个方法连接数据库并执行查询语句
def get_floor_all():
    cursor = conn.cursor()
    sql = f"select id,name from yt_location"
    cursor.execute(sql)
    name_id_map = {}
    for item in cursor.fetchall():
        name_id_map[item[1]] = item[0]
    return name_id_map

def generate_and_print_codes(file_path):
    name_id_map = get_floor_all()
    # Load the Excel file
    data = pd.read_excel(file_path)

    # Iterate through each row in the DataFrame
    for index, row in data.iterrows():
        floor_number = row['楼层号']  # Get the floor number
        floor_name = row['楼层名']
        floor_id = name_id_map[floor_name]
        # Iterate through each column except the first two (楼层名 and 楼层号)
        for col in data.columns[2:]:
            # Check if the cell is not NaN
            if not pd.isna(row[col]):
                ids = list(range(1, int(row[col]) + 1))
                for unit_number in tqdm(range(1, len(ids)), desc=f"{floor_number}-{col}-batches"):
                    fnumber = floor_number
                    if floor_number == 9:
                        fnumber = ''
                    code = f"{fnumber}{col}-{unit_number:02d}"
                    add_spot(floor_id, code)

generate_and_print_codes('../files/floor_import.xlsx')


