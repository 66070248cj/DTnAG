"""SeatNumber selectionSort"""
import json
def check(first, second):
    """check"""
    if first[0] == second[0]:
        return int(first[1:]) < int(second[1:])
    else:
        return ord(first[0]) < ord(second[0])

def main(data_list, last):
    """main"""
    current = 0
    time = 0
    while current < last:
        small = current
        walker = current + 1
        while walker <= last:
            if check(data_list[walker], data_list[small]):
                small = walker
            walker += 1
            time += 1
        data_list[current], data_list[small] = data_list[small], data_list[current]
        current += 1
        print(data_list)
    print("Comparison times:", time)
main(json.loads(input()), int(input()))
