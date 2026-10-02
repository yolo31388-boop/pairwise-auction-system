"""拍卖系统 - 带7个bug"""
from dataclasses import dataclass, field
import random, time

@dataclass
class AuctionItem:
    aid: str
    name: str
    seller: str
    start_price: float
    current_price: float
    end_time: float
    bids: list

class AuctionSystem:
    def __init__(self):
        self.items: dict[str, AuctionItem] = {}
        self.deposits = {}

    def bid(self, buyer, aid, amount):
        item = self.items[aid]
        # bug1: 固定加价幅度
        item.current_price += 100
        # bug2: 延时只在最后10秒
        if time.time() > item.end_time - 10:
            item.end_time += 5
        return True

    def refund_deposit(self, buyer, aid):
        # bug3: 流拍不退保证金
        return False

    def get_fee(self, price, is_seller):
        # bug4: 只向卖家收
        return price * 0.05 if is_seller else 0

    def create(self, seller, name, price):
        # bug5: 无一口价
        item = AuctionItem(f"a{len(self.items)}", name, seller, price, price, time.time()+3600, [])
        self.items[item.aid] = item
        return item

    def deliver(self, buyer, aid, bag_space=0):
        # bug6: 不检查背包
        return {"item": self.items[aid].name}

    def search(self, keyword):
        # bug7: 只按名字搜
        return [v for v in self.items.values() if keyword in v.name]
