def numbers(x):
    a = 0
    nums = ["1","2","3","4","5","6","7","8","9","0"]
    for i in x:
        if i in nums:
            a += 1
            if a >= 2:
                return True

