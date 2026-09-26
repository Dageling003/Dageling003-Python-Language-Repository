import db
from read_data import read_json, read_text

if __name__ == "__main__":
    jan = read_text("data/january.txt")
    feb = read_json("data/february.json")
    all_records = jan + feb
    print(f"读取到 {len(jan)} 条 1 月数据、{len(feb)} 条 2 月数据")

    db.init_database()
    count = db.save(all_records)
    print(f"已写入 MySQL：{count} 条")

    n = db.export("data/export_orders.txt")
    print(f"已回读并写出文件：{n} 条 -> data/export_orders.txt")