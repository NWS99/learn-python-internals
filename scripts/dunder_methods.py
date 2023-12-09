"""
In this module I try to implement basic classes with heavy use of dunder methods.
The Goal is to:
- understand the basic behavior
- get to know the build in Data Models

Reference: https://docs.python.org/3/reference/datamodel.html
"""

from typing import List


class Mark():

    def __init__(self, subject: str, value: int):

        self.subject = subject
        self.value = value

    def __repr__(self):

        name_mapping = {
            1: 'A',
            2: 'B',
            3: 'C',
            4: 'D',
            5: 'E',
            6: 'F'
        }

        return f"{self.subject}: {name_mapping[self.value]}"


class Mark_Report():

    def __init__(self):

        self.grades: List[Mark] = []

    def __getitem__(self, position):

        return self.grades[position]

    def __len__(self):

        return len(self.grades)

    def __iadd__(self, element: Mark):

        self.grades.append(element)
        return self


    #TODO: implement further __methods__
    
    # def __get__(self, instance, owner=None):
    # def __set__(self, instnace, value)
    # def __new__(cls)
    
    # TODO: try to implement a singleton behavior and to have a proper mark report behavior and output

    def __repr__(self):

        return "\n".join(f"{mark.subject}: {mark.value}"
                         for mark in self.grades)


half_year = Mark_Report()
half_year += (Mark('math', 1))
half_year += (Mark("german", 3))

print(half_year)
