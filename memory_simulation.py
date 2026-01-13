memory = [None] * 10  # Simulated memory blocks

def allocate(process, size):
    for i in range(len(memory) - size + 1):
        if all(block is None for block in memory[i:i+size]):
            for j in range(i, i+size):
                memory[j] = process
            print(f"Allocated {size} blocks to {process}")
            return
    print(f"Not enough memory for {process}")

def deallocate(process):
    for i in range(len(memory)):
        if memory[i] == process:
            memory[i] = None
    print(f"Deallocated memory from {process}")

def show_memory():
    print("Memory State:", memory)

# Simulation
show_memory()
allocate("Process A", 3)
show_memory()
allocate("Process B", 4)
show_memory()
deallocate("Process A")
show_memory()
