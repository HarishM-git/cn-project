# Read number of directions
n = int(input())

# Read the directions list
a = [input().strip() for _ in range(n)]

# Initialize variables
arr = a[:2]  # Initially place your legs on the first two tiles
final = 0  # To count the minimum number of moves
last_ch = None  # To track which direction was last changed (0 -> arr[0], 1 -> arr[1])

# Debug print to check initial arr
print(f"Initial arr: {arr}")

# Iterate over the remaining directions
for i in range(2, n):
    it = a[i]
    print(f"Processing {it}...")  # Debug: Show the direction being processed
    
    # If the direction is not in arr, it means we need to move a leg
    if it not in arr:
        print(f"'{it}' is not in arr, so modifying...")  # Debug: Show that modification will occur
        
        # We replace the least recently used direction
        if last_ch is None:
            arr[0] = it  # If no direction was changed yet, change arr[0]
            last_ch = 0  # Mark that arr[0] was changed
        elif last_ch == 0:
            arr[1] = it  # If arr[0] was last changed, change arr[1]
            last_ch = 1  # Mark that arr[1] was changed
        else:
            arr[0] = it  # If arr[1] was last changed, change arr[0]
            last_ch = 0  # Mark that arr[0] was changed
        
        final += 1  # Increment the count of moves
        print(f"arr updated to: {arr}")  # Debug: Show the updated arr

# Output the minimum number of moves
print(final)
