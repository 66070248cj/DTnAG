"""."""
class ArrayStack:
    """."""
    def __init__(self):
        self.size = 0
        self.data = [] #กำหนด attribute

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
            self.data.append(input_data)
            self.size += 1

    def pop(self): #data on top stack, (delete from stack)
        """."""
        if self.is_empty() == True: #check underflow
            print("Underflow: Cannot pop data from an empty list")
            return None
        else:
            data_pop = self.data[-1]
            self.data.pop()
            self.size -= 1
            return  data_pop

    def is_empty(self): #return boolean
        """."""
        if self.size == 0:
            return True
        else:
            return False

    def get_stack_top(self): #data on top stack
        """."""
        if self.size == 0:
            print("Underflow: Cannot get stack top from an empty list")
            return None
        else:
            return self.data[-1]

    def get_size(self):
        """."""
        return self.size

    def print_stack(self):
        """."""
        return print(self.data)

def is_parentheses_mathching():
    """."""
    stack = ArrayStack()
    exp = input()
    parent1 = 0
    parent2 = 0
    for i in exp:
        if i == "(":
            stack.push(i)
            parent1 += 1
        elif i == ")":
            stack.pop()
            parent2 += 1
    if stack.is_empty() and parent1 == parent2:
        print("Parentheses in", exp, "are matched")
        print(True)
    else:
        print("Parentheses in", exp, "are unmatched")
        print(False)
is_parentheses_mathching()
