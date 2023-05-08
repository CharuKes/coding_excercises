def zero_plentiful(a):
    counter = 0
    num_zeros = 0
    for i in a:
        if i == 0:
            num_zeros += 1
        else:
            if num_zeros >= 4:
                counter += 1
            num_zeros = 0
    if num_zeros >= 4:
        counter += 1
    return(counter)