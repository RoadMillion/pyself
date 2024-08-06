from datetime import datetime, date
import json
import pymysql
import pymysql.cursors

# 数据库配置
DB_CONFIG = {
    "host": "rm-uf6102o3n4q57xk8d.mysql.rds.aliyuncs.com",
    "user": "yzs_meta",
    "password": "AEQMzygUQfve2KbIZc",
    "db": "yzs_meta_data",
    "charset": "utf8mb4",
    "cursorclass": pymysql.cursors.DictCursor,
}

# 要导出的表列表
TABLES = ["meta_category", "meta_category_label", "meta_entity", "meta_page", "meta_view"]



def escape_value(value):
    print(f"{value}{type(value)}")
    """根据数据类型转义值"""
    if isinstance(value, str):
        escaped_value = value.replace("'", "''")
        return f"'{escaped_value}'"
    elif isinstance(value, datetime):
        # 转换 datetime 为 "YYYY-MM-DD HH:MM:SS" 格式
        return f"'{value.strftime('%Y-%m-%d %H:%M:%S')}'"
    elif isinstance(value, date):
        # 转换 date 为 "YYYY-MM-DD" 格式，这里也可以根据需要添加时间
        return f"'{value.strftime('%Y-%m-%d')}'"
    elif value is None:
        return "NULL"
    elif isinstance(value, dict) or isinstance(value, list):
        # 将字典或列表转换为JSON字符串，并转义单引号
        json_str = json.dumps(value).replace("'", "''")
        return f"'{json_str}'"
    else:
        return str(value)


def generate_insert_statements(table_name, cursor):
    """为指定表生成INSERT语句"""
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    if not rows:
        return

    columns = ', '.join(rows[0].keys())
    values = []

    for row in rows:
        row_values = [escape_value(item) for item in row.values()]
        values.append(f"({', '.join(row_values)})")

    insert_statement = f"INSERT INTO {table_name} ({columns}) VALUES {', '.join(values)};"
    return insert_statement


def export_tables():
    """导出指定表的数据为INSERT语句"""
    connection = pymysql.connect(**DB_CONFIG)
    try:
        with connection.cursor() as cursor:
            for table in TABLES:
                insert_statement = generate_insert_statements(table, cursor)
                if insert_statement:
                    print(insert_statement)
                else:
                    print(f"-- {table}为空，没有数据导出")
    finally:
        connection.close()


if __name__ == "__main__":
    export_tables()
