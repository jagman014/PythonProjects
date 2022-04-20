# Example

class Course:
    def __init__(self, title, teacher):
        self.title = title
        self.teacher = teacher
        self.meetings = []
        self.students = []

    def add_meeting(self, new_meeting):
        self.meetings.append(new_meeting)

    def add_student(self, new_student):
        self.students.append(new_student)

    def all_meetings(self):
        return 'Meeting at:\n' + '\n'.join('\t' + meeting
                                           for meeting in self.meetings)


class OnlineCourse(Course):
    def __init__(self, title, teacher, url):
        super().__init__(title, teacher)
        self.url = url

    @staticmethod
    def get_username(student):
        return student.lower()

    def all_usernames(self):
        return {student: self.get_username(student)
                for student in self.students}


c_1 = Course('Python', 'Reuven')
c_1.add_meeting('2018-May-10 10:00')
c_1.add_meeting('2018-May-12 10:00')

c_1.add_student('Alice')
c_1.add_student('Bob')

print(c_1.all_meetings())

c_2 = OnlineCourse('Online Python', 'Reuven', 'https://lerner.co.il')
c_2.add_meeting('2018-May-10 10:00')
c_2.add_meeting('2018-May-12 10:00')

c_2.add_student('Alice')
c_2.add_student('Bob')

print(c_2.all_usernames())

# OnlineCourse 'is-a' Course, it inherits from it's superclass
print(OnlineCourse.__bases__)
print(Course.__bases__)
