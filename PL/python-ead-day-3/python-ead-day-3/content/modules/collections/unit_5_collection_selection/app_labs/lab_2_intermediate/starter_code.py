def get_latest_activities(raw_logs):
    latest = {}
    for log in raw_logs:
        user_id = log[0]
        latest[user_id] = log
    return latest

def format_sorted_report(activity_map):
    items = list(activity_map.values())
    items.sort() # Sorts by first element of tuple (user_id)
    return items
