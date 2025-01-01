def sort_rgb(arr):
    low, mid, high = 0, 0, len(arr) - 1
    
    while mid <= high:
        if arr[mid] == 'B':
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 'G':
            mid += 1
        else:  # arr[mid] == 'R'
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr

# Example
input_rgb = ['R', 'G', 'B', 'G', 'G', 'R', 'B', 'B', 'G']
output_rgb = sort_rgb(input_rgb)
print(output_rgb)