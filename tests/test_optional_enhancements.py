import pytest
from swap_meet.item import Item
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_items_have_expected_default_age():
    item = Item()
    clothing = Clothing()
    decor = Decor()
    electronics = Electronics()
    assert item.age == Item.DEFAULT_ITEM_AGE 
    assert clothing.age == Item.DEFAULT_ITEM_AGE 
    assert decor.age == Item.DEFAULT_ITEM_AGE 
    assert electronics.age == Item.DEFAULT_ITEM_AGE 

def test_items_can_be_assigned_age():
    item = Item(age = 1)
    clothing = Clothing(age = 1)
    decor = Decor(age = 1)
    electronics = Electronics(age = 1)
    assert item.age == 1 
    assert clothing.age == 1
    assert decor.age == 1
    assert electronics.age == 1
    


def test_get_newest_by_category():
    item_a = Clothing(age=0)
    item_b = Decor(age=2)
    item_c = Clothing(age=3)
    item_d = Decor(age=1)
    item_e = Clothing(age=2)
    tai = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

    newest_clothing_item = tai.get_newest_by_category("Clothing")
    newest_decor_item = tai.get_newest_by_category("Decor")

    assert newest_clothing_item.category == "Clothing"
    assert newest_clothing_item.age == pytest.approx(0.0)
    assert newest_decor_item.category == "Decor"
    assert newest_decor_item.age == pytest.approx(1.0)


def test_newest_by_category_no_matches_is_none():
    item_a = Decor(age=2)
    item_b = Decor(age=2)
    item_c = Decor(age=2)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    newest_item = tai.get_newest_by_category("Electronics")

    assert newest_item is None


def test_swap_newest_by_category():
    item_a = Decor(age=2)
    item_b = Electronics(age=1)
    item_c = Decor(age=1)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(age=2)
    item_e = Decor(age=3)
    item_f = Clothing(age=1)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    result = tai.swap_newest_by_category(
        other=jesse,
        my_priority="Clothing",
        their_priority="Decor"
    )

    assert result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c not in tai.inventory
    assert item_f in tai.inventory
    assert item_d in jesse.inventory
    assert item_e in jesse.inventory
    assert item_f not in jesse.inventory
    assert item_c in jesse.inventory


def test_swap_newest_by_category_no_inventory_is_false():
    tai = Vendor(
        inventory=[]
    )

    item_a = Decor(age=2)
    item_b = Electronics(age=1)
    item_c = Decor(age=1)
    jesse = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    result = tai.swap_newest_by_category(
        other=jesse,
        my_priority="Clothing",
        their_priority="Decor"
    )

    assert not result
    assert len(tai.inventory) == 0
    assert len(jesse.inventory) == 3
    assert item_a in jesse.inventory
    assert item_b in jesse.inventory
    assert item_c in jesse.inventory


def test_swap_newest_by_category_no_other_inventory_is_false():
    item_a = Decor(age=2)
    item_b = Electronics(age=1)
    item_c = Decor(age=1)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    jesse = Vendor(
        inventory=[]
    )

    result = tai.swap_best_by_category(
        other=jesse,
        my_priority="Decor",
        their_priority="Clothing"
    )

    assert not result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 0
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory


def test_swap_newest_by_category_no_match_is_false():
    item_a = Decor(age=2)
    item_b = Electronics(age=1)
    item_c = Decor(age=1)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(age=2)
    item_e = Decor(age=3)
    item_f = Clothing(age=1)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    result = tai.swap_newest_by_category(
        other=jesse,
        my_priority="Clothing",
        their_priority="Clothing"
    )

    assert not result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory
    assert item_d in jesse.inventory
    assert item_e in jesse.inventory
    assert item_f in jesse.inventory


def test_swap_newest_by_category_no_other_match_is_false():
    item_a = Decor()
    item_b = Electronics()
    item_c = Decor()
    tai = Vendor(
        inventory=[item_c, item_b, item_a]
    )

    item_d = Clothing()
    item_e = Decor()
    item_f = Clothing()
    jesse = Vendor(
        inventory=[item_f, item_e, item_d]
    )

    result = tai.swap_newest_by_category(
        other=jesse,
        my_priority="Electronics",
        their_priority="Decor"
    )

    assert not result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory
    assert item_d in jesse.inventory
    assert item_e in jesse.inventory
    assert item_f in jesse.inventory
