def distinct_sorted_list(lst):
    return sorted(set(lst))


# Example usage
a = [4,1,2,3,3,1,3,4,5,1,7]
print(distinct_sorted_list(a))
# Output: [1, 2, 3, 4, 5, 7]
