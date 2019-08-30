world_record = float(input())
distance = float(input())
time_for_one_meter = float(input())

count_delay = distance // 15
ivans_time = distance * time_for_one_meter + count_delay * 12.5

if ivans_time < world_record:
    print(f'Yes, he succeeded! The new world record is {ivans_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {(ivans_time - world_record):.2f} seconds slower.')
