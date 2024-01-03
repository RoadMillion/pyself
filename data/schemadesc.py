import pandas as pd
import pymysql

# 数据库连接配置，请根据实际情况进行修改
db_config = {
    "host": "106.15.237.250",
    "port": 3306,
    "user": "root",
    "passwd": "yzs123456",
    "db": "yzs_part_system",
    "charset": "utf8"
}

# 建立数据库连接
conn = pymysql.connect(**db_config)


# 获取数据库中所有表的名称
def get_tables(conn):
    tables = pd.read_sql("SHOW TABLES", conn)
    return tables.iloc[:, 0].tolist()


# 获取表和字段的描述信息
def get_table_description(table, conn):
    description = pd.read_sql(f"""
    select
        column_name 字段code,column_comment 字段名称
    from
        information_schema.columns 
    where
        table_schema = (
            select
                database()
        ) 
        and table_name = (
            '{table}'
        )   
        and column_name not in ('id', 'def_flag', 'update_by', 'update_time')
    order by
        ordinal_position

""", conn)
    description['Table'] = get_table_name(table)
    return description


def get_table_name(table):
    tab_comment = pd.read_sql(f"""    select
        table_comment
    from
        information_schema.tables   
    where
        table_schema = (
            select
                database()
        )   
        AND table_name = '{table}'
    order by
        create_time desc
    """, conn)
    return tab_comment.iloc[0, 0]

# 主执行函数
def export_db_schema_to_excel():
    all_tables_desc = pd.DataFrame()
    with conn:
        tables = get_tables(conn)
        for table in tables:
            if table.startswith("yzs_"):
                description = get_table_description(table, conn)
                all_tables_desc = all_tables_desc.append(description, ignore_index=True)

    all_tables_desc.to_excel('database_schema.xlsx', index=False)



# 执行脚本
export_db_schema_to_excel()
