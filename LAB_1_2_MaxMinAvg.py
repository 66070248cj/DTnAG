"""."""
def labmxmnavg():
    """."""
    import json
    my_list = json.loads(input())
    num_mx = 0
    num_mn = my_list[0]
    for i in my_list:
        if i >= num_mx:
            num_mx = i
        if i <= num_mn:
            num_mn = i
    avg = sum(my_list)/len(my_list)
    ###
    numcheck = [num_mx, num_mn, avg]
    num_ans = []
    for num in numcheck:
        check = isinstance(num, float)
        if check == True:
            num = "%.2f" %num
            num_ans.append(float(num))
        else:
            num_ans.append(num)
    print(tuple(num_ans))
labmxmnavg()

###input: [22, 54, 7, 87, 12, 9, 63, 55, 48]
###find (max, min, avg(.2f))
###output: (87, 7, 39.67)