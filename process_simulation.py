from collections import deque

process_queue = deque(["Process A", "Process B", "Process C"])

print("CPU Process Scheduling Simulation\n")

while process_queue:
    process = process_queue.popleft()
    print(f"Executing {process}")

print("\nAll processes have been executed.")
