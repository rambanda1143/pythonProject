def find_min_platforms(arr, dep):
    arr.sort()
    dep.sort()

    platform_needed = 0
    max_platforms = 0
    i, j = 0, 0

    while i < len(arr) and j < len(dep):
        if arr[i] <= dep[j]:
            platform_needed += 1
            max_platforms = max(max_platforms, platform_needed)
            i += 1
        else:
            platform_needed -= 1
            j += 1

    return max_platforms

# Example
arrival = ["9:00", "9:40", "9:50", "11:00", "15:00", "18:00"]
departure = ["9:10", "12:00", "11:20", "11:30", "19:00", "20:00"]
arrival = [int(t.replace(":", "")) for t in arrival]
departure = [int(t.replace(":", "")) for t in departure]
print(find_min_platforms(arrival, departure))