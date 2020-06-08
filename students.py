class student:
    def __init__(self, name, major, gpa, is_on):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on = is_on
    #def __del__(self):
     #   print(self.name, 'deleted')
    def __len__(self):
        return len(self.name)
    def on_honor_roll(self):
        if self.gpa > 3.6:
            return True
        else:
            return False





