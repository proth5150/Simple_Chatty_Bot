# put your python code here


year_to_check = int(input())


if year_to_check % 4 == 0 and year_to_check % 100 != 0:
    print("Leap")
elif year_to_check % 400 == 0:
    print("Leap")
else:
    print("Ordinary")