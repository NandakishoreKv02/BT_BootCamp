hourly_slots = [f"{str(i).zfill(2)}:00" for i in range(24)]

morning_shift = hourly_slots[:12]
afternoon_shift = hourly_slots[12:]
express_line = hourly_slots[::3]
last_three = hourly_slots[-3:]

print(f"Morning Len: {len(morning_shift)}")
print(f"Express: {express_line}")
print(f"Last 3: {last_three}")
