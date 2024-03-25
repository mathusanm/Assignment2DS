import winsound  # For playing sound effects (Windows)
import time      # For adding slight delay for sound effect

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort both halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left_half, right_half):
    merged = []
    i = j = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            merged.append(left_half[i])
            i += 1
        else:
            merged.append(right_half[j])
            j += 1
            # Play sound effect for swap
            play_sound_effect()
    while i < len(left_half):
        merged.append(left_half[i])
        i += 1
    while j < len(right_half):
        merged.append(right_half[j])
        j += 1

    return merged

def play_sound_effect():
    frequency = 1000  # Set frequency to 1000 Hertz
    duration = 100    # Set duration to 100 milliseconds
    winsound.Beep(frequency, duration)
    time.sleep(0.1)   # Add slight delay for sound effect

# Test the implementation
if __name__ == "__main__":
    arr = [11, 1, 30, 2, 51, 6, 29, 7, 67, 15, 118, 4, 89, 23]
    print("Original Array:", arr)
    sorted_arr = merge_sort(arr)
    print("Sorted Array:", sorted_arr)