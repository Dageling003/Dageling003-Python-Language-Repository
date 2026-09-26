import json
from models import Record


def read_text(path: str) -> list[Record]:
    """读取普通文本：一行一条，逗号分隔（日期、订单 id、销售额、省份）"""
    records: list[Record] = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            date, order_id, money, province = line.split(",")
            records.append(Record(date, order_id, int(money), province))
    return records


def read_json(path: str) -> list[Record]:
    """读取 JSON 数据，字段名与文本数据保持一致"""
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    return [
        Record(d["date"], d["order_id"], d["money"], d["province"])
        for d in data
    ]