# 4 ВАРИАНТ

class Course:
    def __init__(self, title, credits):
        self.title = title
        self.credits = credits

    def get_course_info(self):
        return f"Course: {self.title}, Credits: {self.credits}"


class OnlineCourse(Course):
    def __init__(self, title, credits):
        super().__init__(title, credits)
        self.type = True

    def start_video_lecture(self):
        if self.type:
            return "Включить видео курс"


class OfflineCourse(Course):
    def __init__(self, title, credits):
        super().__init__(title, credits)
        self.type = False

    def schedule_classroom(self):
        if not self.type:
            return "Срочно вернитесь в класс"


class OutputOnlineCourse(OnlineCourse):
    def get_course_info(self):
        return f"Online {super().get_course_info()}"


class OutputOfflineCourse(OfflineCourse):
    def get_course_info(self):
        return f"Offline {super().get_course_info()}"

online_course = OutputOnlineCourse("Python Basics", 3)
offline_course = OutputOfflineCourse("Math 101", 5)

print(online_course.get_course_info())  
print(offline_course.get_course_info())  
print(online_course.start_video_lecture())  
print(offline_course.schedule_classroom())  

