def add_time(start, duration, starting_day=None):
    # Split start time and get period (AM/PM)
    time_part, period = start.split()     # e.g, '3:00','PM'
    start_hour, start_min = map(int, time_part.split(":"))
    dur_hour, dur_min = map(int, duration.split(":"))
    period = period.upper()

    # Add minutes and handle overflow to hours
    total_min = start_min + dur_min
    extra_hour, final_min = divmod(total_min, 60)

    # Convert start hour to 24-hour format
    start24 = (start_hour % 12) + (12 if period == "PM" else 0)
    total_hour24 = start24 + dur_hour + extra_hour
    days_passed = total_hour24 // 24
    final24 = total_hour24 % 24

    # Convert back to 12-hour format
    final_period = "AM" if final24 < 12 else "PM"
    final_hour12 = final24 % 12
    if final_hour12 == 0:
        final_hour12 = 12

    # Build time string
    new_time = f"{final_hour12}:{final_min:02d} {final_period}"

    # Add weekday if provided
    if starting_day:
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

        start_idx = weekdays.index(starting_day.strip().capitalize())
        new_day = weekdays[(start_idx + days_passed) % 7]
        new_time += f", {new_day}"

    if days_passed == 1:
        new_time += " (next day)"
    elif days_passed > 1:
        new_time += f" ({days_passed} days later)"

    return new_time
