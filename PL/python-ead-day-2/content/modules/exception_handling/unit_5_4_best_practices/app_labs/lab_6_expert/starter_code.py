def filter_stream_eafp(streaming_data):
    """
    TODO:
    Use try-except to convert each item to float and sum them.
    Ignore items that fail conversion.
    """
    # WRITE CODE HERE
    pass

def filter_stream_lbyl(streaming_data):
    """
    TODO:
    Use 'if' checks to verify if an item can be a number before converting.
    Handle both numeric types and strings that look like numbers.
    """
    # WRITE CODE HERE
    pass

def main():
    data = [10.5, "20", "invalid", None, 5]
    print(f"EAFP Sum: {filter_stream_eafp(data)}")
    print(f"LBYL Sum: {filter_stream_lbyl(data)}")

if __name__ == "__main__":
    main()
