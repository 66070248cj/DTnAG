"""ProbHash Hashing"""
class Student:
    """."""
    def __init__(self, std_id, name, gpa):
        """input"""
        self.std_id = std_id
        self.name = name
        self.gpa = gpa

    def get_std_id(self):
        """."""
        return self.std_id

    def get_name(self):
        """."""
        return self.name

    def get_gpa(self):
        """."""
        return "%0.2f" %self.gpa

    def print_detail(self):
        """."""
        print("ID:", self.get_std_id())
        print("Name:", self.get_name())
        print("GPA:", self.get_gpa())

class ProbHash:
    """."""
    def __init__(self, size):
        """creat table"""
        self.hash_table = size*[None]
        self.size = size

    def hash(self, key):
        """."""
        return key%self.size

    def rehash(self, hkey):
        """."""
        return (hkey+1)%self.size

    def insert_data(self, student):
        """."""
        index = self.hash(student.get_std_id())
        if self.hash_table[index] is None:
            self.hash_table[index] = student
            print("Insert %d at index %d" % (student.get_std_id(), index))
        else:
            next_index = self.rehash(index)
            while next_index != index and self.hash_table[next_index] is not None:
                next_index = self.rehash(next_index)
            if next_index == index:
                print("The list is full. %d could not be inserted." % student.get_std_id())
            else:
                self.hash_table[next_index] = student
                print("Insert %d at index %d" % (student.get_std_id(), next_index))

    def search_data(self, std_id):
        """."""
        index = self.hash(std_id)
        if self.hash_table[index] is not None and self.hash_table[index].get_std_id() == std_id:
            print("Found %d at index %d" % (std_id, index))
            return self.hash_table[index]
        else:
            next_index = self.rehash(index)
            while next_index != index:
                if self.hash_table[next_index] is not None \
                    and self.hash_table[next_index].get_std_id() == std_id:
                    print("Found %d at index %d" % (std_id, next_index))
                    return self.hash_table[next_index]
                next_index = self.rehash(next_index)
            print("%d does not exist." % std_id)
            return None

def main():
    """."""
    import json
    size = int(input())
    hashtable = ProbHash(size)
    while True:
        finish = input()
        if finish == "Done":
            break
        condition, data = finish.split(" = ")
        if condition == "I":
            std_in = json.loads(data)
            std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
            hashtable.insert_data(std)
        elif condition == "S":
            print("------")
            student = hashtable.search_data(int(data))
            if student is not None:
                student.print_detail()
            print("------")
        else:
            print("Invalid Condition!")
main()
