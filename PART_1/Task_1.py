numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

a = numbers[:4]
b = numbers[5:]

c = len(numbers)
d = sum(a+b)

average = d/c
numbers[4] = average

print("Измененный список:", numbers)
