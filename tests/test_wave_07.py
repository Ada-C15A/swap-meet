import pytest
import datetime

from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_find_newest_item():
    item_a = Clothing(condition=4, age=datetime.datetime(2021, 2, 1))
    item_b = Decor(condition=4, age=datetime.datetime(2021, 3, 1))
    item_c = Clothing(condition=4, age=datetime.datetime(2021, 4, 1))
    item_d = Decor(condition=4, age=datetime.datetime(2021, 5, 1))
    item_e = Clothing(condition=4, age=datetime.datetime(2021, 6, 1))
    tai = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

    newest_item = tai.find_newest_item()

    assert newest_item == item_e

def test_find_newest_item_returns_none_if_no_items():
    tai = Vendor(
        inventory=[]
    )

    newest_item = tai.find_newest_item()

    assert newest_item == None

def test_swap_by_newest():
    item_a = Clothing(condition=4, age=datetime.datetime(2021, 2, 1))
    item_b = Decor(condition=4, age=datetime.datetime(2021, 3, 1))
    item_c = Clothing(condition=4, age=datetime.datetime(2021, 4, 1))
    item_d = Decor(condition=4, age=datetime.datetime(2021, 5, 1))
    item_e = Clothing(condition=4, age=datetime.datetime(2021, 6, 1))
    tai = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )
    item_f = Electronics(condition=4, age=datetime.datetime(2021, 4, 1))
    item_g = Decor(condition=4, age=datetime.datetime(2021, 3, 1))
    item_h = Decor(condition=4, age=datetime.datetime(2021, 8, 1))
    item_i = Electronics(condition=4, age=datetime.datetime(2021, 1, 1))
    item_j = Clothing(condition=4, age=datetime.datetime(2021, 6, 1))
    other_vendor = Vendor(
        inventory=[item_f, item_g, item_h, item_i, item_j]
    )

    tai.swap_by_newest(other_vendor)

    assert item_e in other_vendor.inventory
    assert item_h in tai.inventory
def test_swap_by_newest_does_not_change_anything_if_vendor_has_no_inventory():
    item_a = Clothing(condition=4, age=datetime.datetime(2021, 2, 1))
    item_b = Decor(condition=4, age=datetime.datetime(2021, 3, 1))
    item_c = Clothing(condition=4, age=datetime.datetime(2021, 4, 1))
    item_d = Decor(condition=4, age=datetime.datetime(2021, 5, 1))
    item_e = Clothing(condition=4, age=datetime.datetime(2021, 6, 1))
    tai = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )
    other_vendor = Vendor(
        inventory=[]
    )

    tai.swap_by_newest(other_vendor)

    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory
    assert item_d in tai.inventory
    assert item_e in tai.inventory
    assert len(other_vendor.inventory) == 0