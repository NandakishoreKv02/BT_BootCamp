from cache import Cache
import sys

class Program:
    @staticmethod
    def main(args):
        if len(args)==0:
            print("Enter the maximum capacity: ")
            value=input()
        else:
            value=args[0]
            
        Cache.set_max_capacity(value)

        print("MAX_CAPACITY is " + str(Cache.get_max_capacity()))

        print("MAX_CAPACITY is " + str(Cache.get_max_capacity()))

        print("MAX_CAPACITY is " + str(Cache.get_max_capacity()))

        input()


if __name__ == "__main__":
    Program.main(sys.argv[1:])
