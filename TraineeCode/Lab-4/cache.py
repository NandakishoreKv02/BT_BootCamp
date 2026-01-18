class Cache:
    _MAX_CAPACITY = 0

    """
    Static method to get the maximum capacity of the cache
    """
    @staticmethod
    def set_max_capacity(value):
        Cache._MAX_CAPACITY=value
        
    @staticmethod
    def get_max_capacity():
        print("Returning MAX_CAPACITY")
        return Cache._MAX_CAPACITY
