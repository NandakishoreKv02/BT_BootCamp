"""
Lab 2: Medication Inventory Manager - Starter Code
"""

def create_medication(name, quantity, reorder_level):
    """Create a medication dictionary."""
    return {"name": name, "quantity": quantity, "reorder_level": reorder_level}


def add_to_inventory(inventory, medication):
    """Add medication to inventory list."""
    inventory.append(medication)


def find_medication(inventory, name):
    """Find medication by name, return index or -1."""
    for i, med in enumerate(inventory):
        if med["name"].lower() == name.lower():
            return i
    return -1


def update_stock(inventory, name, change):
    """Update medication quantity."""
    idx = find_medication(inventory, name)
    if idx != -1:
        inventory[idx]["quantity"] += change
        return True
    return False


def get_low_stock_items(inventory):
    """Return list of medications below reorder level."""
    low_stock = []
    for med in inventory:
        if med["quantity"] < med["reorder_level"]:
            low_stock.append(med)
    return low_stock


def display_inventory(inventory):
    """Display formatted inventory table."""
    print(f"{'Name':<20} {'Quantity':>10} {'Reorder':>10} {'Status':>15}")
    print("-" * 60)
    for med in inventory:
        status = "[LOW STOCK]" if med["quantity"] < med["reorder_level"] else ""
        print(f"{med['name']:<20} {med['quantity']:>10} {med['reorder_level']:>10} {status:>15}")


if __name__ == "__main__":
    # Test your functions here
    inventory = []
    pass
