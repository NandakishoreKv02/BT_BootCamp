class MonitorRegistry(type):
    plugins = {}

    def __new__(mcs, name, bases, attrs):
        # TODO: Implement logic
        pass

class BaseMonitor:
    # TODO: Implement logic
    pass

class HeartMonitor:
    # TODO: Implement logic
    pass
if __name__ == '__main__':
    print(f'Registered Plugins: {list(MonitorRegistry.plugins.keys())}')