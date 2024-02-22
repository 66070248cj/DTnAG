"""bubble"""
import json
def check(first, second):
    """check"""
    if first[0] == second[0]:
        return int(first[1:]) < int(second[1:])
    else:
        return ord(first[0]) < ord(second[0])

def main(data_list, last):
    """main"""
    issorted = False
    current = 0
    time = 0
    while current <= last and not issorted:
        walker = last
        issorted = True
        while walker > current:
            if check(data_list[walker], data_list[walker-1]):
                issorted = False
                data_list[walker], data_list[walker-1] = data_list[walker-1], data_list[walker]
            walker -= 1
            time += 1
        current += 1
        print(data_list)
    print("Comparison times: {}".format(time))
main(json.loads(input()), int(input()))
