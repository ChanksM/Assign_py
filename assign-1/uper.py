def upp(x):
    o = 0
    for i in x:
        if i.isupper():
            o += 1
            if o >= 2:     
                return True
