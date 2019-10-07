class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    @classmethod
    def friend(cls, origin, friend_name):
        return cls(friend_name, origin.school)


class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary


anna = WorkingStudent('Anna', 'UMASS', 20.00)
friend = WorkingStudent.friend(anna, 'Zhang')
print(friend.name)
print(friend.school)


def my_method(arg1, arg2):
    return arg1 + arg2


my_method(5, 6)


def my_long_method(arg1, arg2, arg3, arg4):
    return arg1 + arg2 + arg3 + arg4


def my_list_method(list_arg):
    return sum(list_arg)


def addition_simplified(*args):
    return sum(args)


addition_simplified(3, 5, 7, 9)


##


def what_are_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)


what_are_kwargs(12, 34, 56, name='Jose', location='UK')
