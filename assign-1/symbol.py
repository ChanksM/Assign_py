def symbols(x):
    sym = "~!@#$%^&*()_-+=}{|[]\?/:;'<>,."
    o = 0
    for i in x:
        if i in sym:
            o += 1
            if o >= 1:
                 return False

            
