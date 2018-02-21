case = int(input())

preset = [1, 5, 10]

if case < 3:
    print(preset[case])
else:
    print(int(pow(case, 3)))
