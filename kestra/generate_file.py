for i in [100, 500 , 1000]:
    filename = f"input_dag_{i}.txt"

    # Open the file in write mode
    with open(filename, 'w') as file:
        # Loop from 1 to 1000
        for i in range(1, i):
            # Write the current counter value to the file followed by a newline
            file.write(f"{i}\n")