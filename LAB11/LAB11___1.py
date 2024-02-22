"""insertionSort"""
import json
def main(data_list, last):
    """main"""
    current = 1
    time = 0
    while current <= last:
        hold = data_list[current]
        walker = current - 1
        while walker >= 0:
            time += 1
            if hold < data_list[walker]:
                data_list[walker], data_list[walker+1] = data_list[walker+1], data_list[walker]
                walker -= 1
            else:
                break
        data_list[walker + 1] = hold
        current += 1
        print(data_list)
    print("Comparison times: {}".format(time))
main(json.loads(input()), int(input()))
