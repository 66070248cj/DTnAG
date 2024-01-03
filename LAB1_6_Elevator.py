"""."""
class Elevator:
    def __init__(self, max_floor): 
        self.current_floor = 1 #ชั้นปัจจุบัน
        self.max_floor = max_floor #ชั้นสูงสุด
    
    def go_to_floor(self, floor): #ชั้นที่จะไป
        self.current_floor = floor
    
    def report_current_floor(self):
        return self.current_floor

def main():
    maxx = int(input())
    eleva = Elevator(maxx)
    while True:
        floor = input()
        if floor == "Done":
            break
        if 1 <= int(floor) <= maxx:
            eleva.go_to_floor(int(floor))
        else:
            print("Invalid Floor!")
    print(eleva.report_current_floor())
main()
