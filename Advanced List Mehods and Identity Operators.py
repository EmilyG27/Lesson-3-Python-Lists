# Task 1
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

print("Alice both submitted the assignments and attended the class") if "Alice" in submitted and "Alice" in attended else print("Alice did not submit the assignments and/or attend the class")
print("Bob both submitted the assignments and attended the class") if "Bob" in submitted and "Bob" in attended else print("Bob did not submit the assignments and/or attend the class")
print("Charlie both submitted the assignments and attended the class") if "Charlie" in submitted and "Charlie" in attended else print("Charlie did not submit the assignments and/or attend the class")
print("David both submitted the assignments and attended the class") if "David" in submitted and "David" in attended else print("David did not submit the assignments and/or attend the class")

# Task 2
print(submitted is attended)

# Task 3
attended.remove("Eve")
attended.remove("Frank")
print(attended)
