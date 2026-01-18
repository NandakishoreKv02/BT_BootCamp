class Thermometer:
    """Measures Temperature."""
    def read(self) -> str:
        return "98.6 F"

class Oximeter:
    """Measures Oxygen Saturation."""
    def read(self) -> str:
        return "98%"

def get_reading(device) -> str:
    """Calls read() on the device."""
    return device.read()

if __name__ == "__main__":
    t = Thermometer()
    o = Oximeter()
    print(f"Thermometer: {get_reading(t)}")
    print(f"Oximeter: {get_reading(o)}")
