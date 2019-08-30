count_negative_evaluations = int(input())
negative_evaluations = 0
total_score = 0
total_tasks = 0
task_name = None

while True:
    current_line = input()

    if current_line == 'Enough':
        print(f'Average score: {total_score/total_tasks:.2f}')
        print(f'Number of problems: {total_tasks}')
        print(f'Last problem: {task_name}')
        break
    else:
        task_name = current_line

    current_evaluation = float(input())
    total_score += current_evaluation
    total_tasks += 1

    if current_evaluation <= 4:
        negative_evaluations += 1

    if negative_evaluations == count_negative_evaluations:
        print(f'You need a break, {count_negative_evaluations} poor grades.')
        break