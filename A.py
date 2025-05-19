data = [12, 9, 30, "A", "M", 99, 82, "J", "N", "B"]

letters = sorted([x for x in data if isinstance(x, str)])
numbers = sorted([x for x in data if isinstance(x, int)])

result = letters + numbers
print("A:", result)