# The following line imports the Vendor class from the module vendor inside the swap_meet package.
from swap_meet.vendor import Vendor


def test_vendor_has_inventory():
    vendor = Vendor()
    assert len(vendor.inventory) == 0

def test_different_vendors_inventories_are_siloed():
    vendor1 = Vendor()
    vendor2 = Vendor()
    vendor1.add("item1")
    assert vendor1.inventory == ["item1"]
    assert vendor2.inventory == []
    
    
def test_vendor_takes_optional_inventory():
    inventory = ["a", "b", "c"]
    vendor = Vendor(inventory=inventory)
    assert len(vendor.inventory) == 3
    assert "a" in inventory
    assert "b" in inventory
    assert "c" in inventory


def test_adding_to_inventory():
    vendor = Vendor()
    item = "new item"

    result = vendor.add(item)

    assert len(vendor.inventory) == 1
    assert item in vendor.inventory
    assert result == item


def test_removing_from_inventory_returns_item():
    item = "item to remove"
    vendor = Vendor(
        inventory=["a", "b", "c", item]
    )

    result = vendor.remove(item)

    assert len(vendor.inventory) == 3
    assert item not in vendor.inventory
    assert result == item


def test_removing_not_found_is_false():
    item = "item to remove"
    vendor = Vendor(
        inventory=["a", "b", "c"]
    )

    result = vendor.remove(item)

    assert len(vendor.inventory) == 3
    assert not result
