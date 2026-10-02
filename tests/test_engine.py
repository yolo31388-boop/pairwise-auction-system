"""拍卖测试"""
import pytest, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from src.engine import AuctionSystem, AuctionItem

class TestBid:
    def test_increment_scales(self):
        asys = AuctionSystem()
        asys.items = {"a1": AuctionItem("a1","s","p1",100,100,9999999999,[])}
        asys.bid("p1", "a1", 200)
        assert asys.items["a1"].current_price >= 105, "加价幅度固定"

class TestDeposit:
    def test_refund_on_fail(self):
        asys = AuctionSystem()
        asys.deposits = {"p1": 100}
        assert asys.refund_deposit("p1", "a1"), "保证金不退"
