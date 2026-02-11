print("=== Data Stats Calculator ===")

numbers = input("Enter numbers separated by commas: ")

data = numbers.split(",")
data = [int(n) for n in data]

total = sum(data)
count = len(data)
average = total / count
minimum = min(data)
maximum = max(data)
