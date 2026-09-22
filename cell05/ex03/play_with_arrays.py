original_array = [2, 618, 23, 48, 48, 22, -12, -2]
new_array = {x + 2 for x in original_array if x > 5}

print(f"Original array: {original_array}")
print(f"New array: {new_array}")