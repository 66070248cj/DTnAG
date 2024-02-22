"""selectionSort"""
import json
def main(data_list, last):
    """main"""
    current = 0
    time = 0
    while current < last:
        small = current
        walker = current + 1
        while walker <= last:
            if data_list[walker] < data_list[small]:
                small = walker
            walker += 1
            time += 1
        data_list[current], data_list[small] = data_list[small], data_list[current]
        current += 1
        print(data_list)
    print("Comparison times:", time)
main(json.loads(input()), int(input()))