
count = int(input(''))
all_numbers = []

for _ in range(count):
    all_numbers.append(float(input('')))

print(f'max: {"%.3f" % max(all_numbers)}')
print(f'min: {"%.3f" % min(all_numbers)}')
print(f'avg: {"%.3f" % float(sum(all_numbers)/count)}')
# "%.2f" % a

