def process_batch(batch_list, index, key):
    """
    TODO:
    1. Try to access batch_list[index][key].
    2. Catch LookupError (covering Index/Key errors).
    3. Return (None, f"Lookup Failed: {str(e)}") on error.
    4. Return (value, "Success") on success.
    """
    # WRITE CODE HERE
    pass

def main():
    data = [{"id": 1, "val": 10}, {"id": 2, "val": 20}]
    
    # Valid
    print(process_batch(data, 0, "val")) 
    # Invalid Index
    print(process_batch(data, 5, "val"))
    # Invalid Key
    print(process_batch(data, 0, "typo"))

if __name__ == "__main__":
    main()
