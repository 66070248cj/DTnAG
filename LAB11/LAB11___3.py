"""bubble"""
import json
def main(data_list, last):
    """main"""
    issorted = False
    current = 0
    time = 0
    while current <= last and not issorted:
        walker = last
        issorted = True
        while walker > current:
            if data_list[walker] < data_list[walker-1]:
                issorted = False
                temp = data_list[walker]
                data_list[walker] = data_list[walker-1]
                data_list[walker-1] = temp
            walker -= 1
            time += 1
        current += 1
        print(data_list)
    print("Comparison times: {}".format(time))
main(json.loads(input()), int(input()))
