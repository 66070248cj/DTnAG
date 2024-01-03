"""is_even"""
def is_even():
    """is_even"""
    numk = str(input())
    list_even = ["0", "2", "4", "6", "8"]
    if numk[-1] in list_even:
        print(True)
    else:
        print(False)
is_even()

###input: 22
### if num is even return True / Do not use modulo(%), math import
###output True