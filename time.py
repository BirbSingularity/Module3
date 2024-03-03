current_time = int(input("Enter the current time (0-23): "))
wait_hours = int(input("Enter the number of hours to wait: "))
alarm_time = lambda current, wait: (current + wait) % 24

print(f"The alarm will go off at: {alarm_time(current_time, wait_hours):02d}:00")
