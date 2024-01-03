"""."""
def main():
    """."""
    laongdao_data = convert_string_to_tuples(input())
    listdata = list(laongdao_data)
    newlist = []
    newlist.append(listdata[1])
    newlist.append(listdata[0])
    print(tuple(newlist))

def convert_string_to_tuples(text_in):
    """."""
    values = text_in.strip('()').split(', ')
    return tuple(map(float, values))
main()

###input: (6, 8)
### swap and make it tuple (.2f, .2f)
###output: (8.0, 6.0)