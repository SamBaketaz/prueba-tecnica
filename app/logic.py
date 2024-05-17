class NumberSet:
    def __init__(self):
        self.number_set = set(range(1, 101))

    def extract(self, number):
        if number in self.number_set:
            self.number_set.remove(number)
            return None
        else:
            return number
    
    def find_missing_number(self):
        if len(self.number_set) == 1:
            return self.number_set.pop()
        else:
            return None
