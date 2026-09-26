class Record:
    """一条销售记录：日期、订单 id、销售额、省份"""

    def __init__(self, date: str, order_id: str, money: int, province: str):
        self.date = date
        self.order_id = order_id
        self.money = money
        self.province = province

    def __str__(self) -> str:
        return f"{self.date},{self.order_id},{self.money},{self.province}"