distance_apart = []
similarity = 0

def load_data(filename):
    left = []
    right = []
    with open(filename) as f:
        content = f.readlines()
        for row in content:
            row = row.strip().split()
            left.append(int(row[0]))
            right.append(int(row[1]))
    return left, right

left, right = load_data('data.txt')

while len(left) > 0:
    min_left = min(left)
    min_right = min(right)
    distance_apart.append(abs(min_left - min_right))
    left.remove(min_left)
    right.remove(min_right)

print(f'Part A: {sum(distance_apart)}')

left, right = load_data('data.txt')

for num in left:
    right_count = right.count(num)
    similarity += num * right_count

print(f'Part B: {similarity}')