"""Student Groups"""
class ArrayStack:
    """."""
    def __init__(self, group):
        """."""
        self.size = 0
        self.student = []
        self.group = [[] for i in range(group)]

    def push(self, input_data):
        """."""
        try:
            if input_data.isdigit():
                input_data = int(input_data)
            elif input_data.replace(".", "", 1).isdigit():
                input_data = float(input_data)
        except (TypeError, ValueError, ArithmeticError, AttributeError):
            pass
        finally:
            self.student.append(input_data)
            self.size += 1

    def pop(self):
        """."""
        if self.is_empty() == True:
            print("Underflow: Cannot pop data from an empty list")
            return None
        else:
            data_pop = self.student[-1]
            self.student.pop()
            self.size -= 1
            return  data_pop

    def is_empty(self):
        """."""
        if self.size == 0:
            return True
        else:
            return False

    def get_stack_top(self):
        """."""
        if self.size == 0:
            print("Underflow: Cannot get stack top from an empty list")
            return None
        else:
            return self.student[-1]

    def get_size(self):
        """."""
        return self.size

    def print_group(self):
        """."""
        while len(self.student) != 0:
            for i in self.group:
                if len(self.student) == 0:
                    break
                i.append(self.student.pop())
        for i in range(len(self.group)):
            arr = self.group[i]
            print("Group %d:" %(i+1), end=" ")
            print(*arr, sep=", ")

def main():
    """."""
    group = int(input())
    members = int(input())
    school = ArrayStack(group)
    for _ in range(members):
        school.push(input())
    school.print_group()
main()
