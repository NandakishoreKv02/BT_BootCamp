# Lab 2: Medication Inventory Manager - Tasks

## Task 1: Medication Data Structure
Create `create_medication(name, quantity, reorder_level)`:
- Return a dictionary with keys: "name", "quantity", "reorder_level"

## Task 2: Add to Inventory
Create `add_to_inventory(inventory, medication)`:
- Append medication dict to inventory list
- No return value needed

## Task 3: Search Functionality
Create `find_medication(inventory, name)`:
- Loop through inventory
- Return index if name matches (case-insensitive)
- Return -1 if not found

## Task 4: Stock Updates
Create `update_stock(inventory, name, change)`:
- Find the medication using find_medication
- If found, add change to quantity (can be negative for dispensing)
- Return True if successful, False if not found

## Task 5: Low Stock Detection
Create `get_low_stock_items(inventory)`:
- Create empty list for results
- Loop through inventory
- If quantity < reorder_level, append to results
- Return the list

## Task 6: Display Formatting
Create `display_inventory(inventory)`:
- Print header with column names
- Loop through inventory and print each medication
- Use f-strings for alignment
- Mark low stock items with [LOW STOCK]
