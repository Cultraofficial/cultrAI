import gc  # Import garbage collection module

# Clear local variables and run garbage collection safely
def clear_memory():
    # Clear only specific variables if needed
    for name in dir():
        if not name.startswith('_'):
            del globals()[name]

    # Run garbage collection
    gc.collect()
    print("Memory cleared successfully.")

# Run memory clearing
clear_memory()
