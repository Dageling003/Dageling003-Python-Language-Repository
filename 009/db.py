from pymysql import Connection

from models import Record

DB_NAME = "py_sql"


def get_conn(select_db: bool = True) -> Connection:
    """构建数据库连接（复用时只改这一处）"""
    conn = Connection(
        host="localhost",
        port=3306,
        user="root",
        # 注意这里记得改！！！不然没法正常运行
        # password="你的mysql密码",
        autocommit=True,          # 自动提交，免去手动 commit
        charset="utf8mb4",        # 不加中文容易变问号（pymysql 不识别 utf-8 连字符写法）
    )
    if select_db:
        conn.select_db(DB_NAME)
    return conn


def init_database() -> None:
    """建库 + 建表，IF NOT EXISTS 保证可以重复执行"""
    conn = get_conn(select_db=False)
    cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME} CHARSET utf8mb4")
    conn.select_db(DB_NAME)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders(
            order_date DATE,
            order_id   VARCHAR(20),
            money      INT,
            province   VARCHAR(20)
        )
    """)
    conn.close()


def save(records: list[Record]) -> int:
    """把 Record 列表批量写入 MySQL，返回写入条数"""
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("TRUNCATE TABLE orders")   # 反复运行不会重复插入
    sql = "INSERT INTO orders(order_date, order_id, money, province) VALUES (%s, %s, %s, %s)"
    rows = [(r.date, r.order_id, r.money, r.province) for r in records]
    cursor.executemany(sql, rows)             # 批量插入，比 for 循环 execute 快
    conn.close()
    return len(rows)


def export(path: str) -> int:
    """从 MySQL 回读数据，再反向写出为文件，返回写出条数"""
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders ORDER BY order_date")
    rows = cursor.fetchall()                  # 嵌套元组：外层一行，内层是一个字段
    with open(path, "w", encoding="utf-8") as f:
        for row in rows:
            f.write(",".join(str(x) for x in row) + "\n")
    conn.close()
    return len(rows)