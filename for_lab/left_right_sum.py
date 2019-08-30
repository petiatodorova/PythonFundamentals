n = int(input())
left_sum = 0
right_sum = 0

for num in range(1, n + 1):
    current_num = int(input())
    left_sum += current_num

for num in range(n + 1, 2 * n + 1):
    current_num = int(input())
    right_sum += current_num

if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
else:
    print(f'No, diff = {abs(left_sum - right_sum)}')