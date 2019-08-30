number = float(input())
input_metric = input()
output_metric = input()
out_number = 0

if input_metric == 'mm' and output_metric == 'mm':
    out_number = number

if input_metric == 'mm' and output_metric == 'cm':
    out_number = number / 10

if input_metric == 'mm' and output_metric == 'm':
    out_number = number / 1000

if input_metric == 'cm' and output_metric == 'mm':
    out_number = number * 10

if input_metric == 'cm' and output_metric == 'cm':
    out_number = number

if input_metric == 'cm' and output_metric == 'm':
    out_number = number / 100

if input_metric == 'm' and output_metric == 'mm':
    out_number = number * 1000

if input_metric == 'm' and output_metric == 'cm':
    out_number = number * 100

if input_metric == 'm' and output_metric == 'm':
    out_number = number

print(f'{out_number:.3f}')