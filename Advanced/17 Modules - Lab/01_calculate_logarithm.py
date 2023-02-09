from math import log

number = int(input())
logarithm_base = input()
if logarithm_base.isdigit():
    print(f"{log(number,int(logarithm_base)):.2f}")
else:
    print(f"{log(number):.2f}")
