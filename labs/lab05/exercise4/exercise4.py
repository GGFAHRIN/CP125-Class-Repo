
def filter_query_times(times):
    mean_time = sum(times) / len(times)
    for time in times:
        before_variance = (time - mean_time)
    variance = (before_variance ** 2) / len(times)
    std_dev_time = variance ** 0.5
    upper_limit = mean_time + std_dev_time
    

    filtered_times = [time for time in times if time <= upper_limit]
    filtered_times.sort()
    return filtered_times
# Test
query_times = [45, 52, 48, 180, 51, 47, 50, 12]
result = filter_query_times(query_times)
print(f"Filtered Times: {result}")  
# Expected: [45, 47, 48, 50, 51, 52]