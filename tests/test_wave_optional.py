import pytest
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics


def test_get_newest_item():
    item_a = Clothing(age=2.0)
    item_b = Decor(age=2.0)
    item_c = Clothing(age=4.0)
    item_d = Decor(age=5.0)
    item_e = Clothing(age=3.0)
    amari = Vendor(inventory=[item_a, item_b, item_c, item_d, item_e])

    newest_item = amari.get_newest_item(amari.inventory)

    assert newest_item.category == "Clothing"
    assert newest_item.age == pytest.approx(2.0)


def test_swap_by_newest():
    item_a = Decor(age=2.0)
    item_b = Electronics(age=4.0)
    item_c = Decor(age=4.0)
    tai = Vendor(inventory=[item_a, item_b, item_c])

    item_d = Clothing(age=2.0)
    item_e = Decor(age=4.0)
    item_f = Clothing(age=4.0)
    jesse = Vendor(inventory=[item_d, item_e, item_f])

    result = tai.swap_by_newest(jesse)

    assert result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert item_d in tai.inventory
    assert item_b in tai.inventory
    assert item_a not in tai.inventory
    assert item_c in tai.inventory

    assert item_a in jesse.inventory
    assert item_e in jesse.inventory
    assert item_d not in jesse.inventory
    assert item_f in jesse.inventory
