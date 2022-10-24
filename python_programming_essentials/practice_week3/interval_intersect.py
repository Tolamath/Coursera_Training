def interval_intersect(lower_num1, upper_num1, lower_num2, upper_num2):
    return (lower_num2 <= upper_num1) and (lower_num1 <= upper_num2)
print("Enter your numbers: ")
first_num, second_num, third_num, fourth_num = map(int, input().split())
print(interval_intersect(first_num, second_num, third_num, fourth_num))
