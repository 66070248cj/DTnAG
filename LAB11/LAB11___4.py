"""insertionSeat"""
import json
def check(first, second):
    """check"""
    if first[0] == second[0]:
        return int(first[1:]) < int(second[1:])
    else:
        return ord(first[0]) < ord(second[0])

def main(data_list, last):
    """main"""
    current = 1
    time = 0
    while current <= last:
        hold = data_list[current]
        walker = current - 1
        while walker >= 0:
            time += 1
            if check(hold, data_list[walker]):
                data_list[walker], data_list[walker+1] = data_list[walker+1], data_list[walker]
                walker -= 1
            else:
                break
        data_list[walker + 1] = hold
        current += 1
        print(data_list)
    print("Comparison times: {}".format(time))
main(json.loads(input()), int(input()))