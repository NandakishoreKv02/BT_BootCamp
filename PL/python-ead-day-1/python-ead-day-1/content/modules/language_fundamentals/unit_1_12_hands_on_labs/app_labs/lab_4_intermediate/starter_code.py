"""Lab 4 Starter - TODO: Implement read_results, calculate_statistics, detect_trend, generate_report"""
def read_results(filename):
    try:
        with open(filename, 'r') as f:
            return [float(line.strip()) for line in f if line.strip()]
    except:
        return []

def calculate_statistics(values):
    if not values:
        return {"average": 0, "min": 0, "max": 0}
    return {
        "average": sum(values) / len(values),
        "min": min(values),
        "max": max(values)
    }

def detect_trend(values):
    if len(values) < 2:
        return "Stable"
    if values[-1] < values[0]:
        return "Improving"
    elif values[-1] > values[0]:
        return "Worsening"
    return "Stable"

def generate_report(results, stats, trend):
    print(f"Results: {results}")
    print(f"Statistics: {stats}")
    print(f"Trend: {trend}")
