# continous dischrge analysis
def longest_discharge_streak(voltages):
    if not voltages:
        return 0, None, None

    max_length = 1
    current_length = 1
    
    start_idx = 0
    end_idx = 0
    
    curr_start_idx = 0

    for i in range(1, len(voltages)):
        if voltages[i] < voltages[i - 1]:
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
                start_idx = curr_start_idx
                end_idx = i - 1
            
            curr_start_idx = i
            current_length = 1

    if current_length > max_length:
        max_length = current_length
        start_idx = curr_start_idx
        end_idx = len(voltages) - 1

    return max_length, voltages[start_idx], voltages[end_idx]

voltages = [12.6, 12.5, 12.5, 12.3, 12.1, 11.9, 12.0, 11.8, 11.6, 11.5, 11.5, 11.2]

length, start_val, end_val = longest_discharge_streak(voltages)

print(f"Longest continuous drop: {length} minutes")
print(f"Started at: {start_val} V Ended at: {end_val} V")