def merge_sort_algorithm(array):
    """
    Sorts an array using the merge sort algorithm.
    
    Args:
    array (list): The list of elements to be sorted.
    
    Returns:
    list: The sorted list of elements.
    
    Description:
    The function sorts the given list using the merge sort algorithm. It first checks if the list has one or no elements, 
    in which case it is already sorted and can be returned immediately. Otherwise, it divides the list into two halves, 
    recursively sorts each half, and then merges the sorted halves back together.
    """
    # Base case: if the list is empty or has one element, it is already sorted
    if len(array) <= 1:
        return array

    # Find the middle point to divide the array into two halves
    middle_point = len(array) // 2
    left_part = array[:middle_point]
    right_part = array[middle_point:]

    # Recursively sort both halves
    merge_sort_algorithm(left_part)
    merge_sort_algorithm(right_part)

    # Initialize pointers for left_part, right_part, and the main array
    left_array_index = 0
    right_array_index = 0
    sorted_index = 0

    # Merge the sorted halves back into the main array
    while left_array_index < len(left_part) and right_array_index < len(right_part):
        if left_part[left_array_index] < right_part[right_array_index]:
            array[sorted_index] = left_part[left_array_index]
            left_array_index += 1
        else:
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1
        sorted_index += 1

    # Copy any remaining elements of left_part, if any
    while left_array_index < len(left_part):
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1

    # Copy any remaining elements of right_part, if any
    while right_array_index < len(right_part):
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_index += 1

    return array

if __name__ == '__main__':
    import random
    # Generate a list of 10 random numbers between 0 and 100
    numbers = [random.randint(0, 100) for _ in range(10)]
    print('Unsorted list:')
    print(numbers)
    
    # Sort the list using the merge_sort_algorithm function
    sorted_numbers = merge_sort_algorithm(numbers)
    print('Sorted list:')
    print(sorted_numbers)
