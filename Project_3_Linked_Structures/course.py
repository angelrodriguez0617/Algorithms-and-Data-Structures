class Course:
    """Class with course number, course name, course credit hours, and course grade"""
    def __init__(self, crs_num=0, nme="", hrs=0.0, grde=0.0):
        if not isinstance(crs_num, int):
            raise ValueError()
        if not isinstance(nme, str):
            raise ValueError
        if not isinstance(hrs, float):
            raise ValueError()
        if not isinstance(grde, float):
            raise ValueError()
        if grde < 0 or grde > 4.0:
            raise ValueError()
        if crs_num < 0 or hrs < 0:
            raise ValueError()
        self.course_num = crs_num
        self.hours = hrs
        self.nam = nme
        self._grade = grde
        self.next = None

    def number(self):
        """Returns course number"""
        return self.course_num

    def name(self):
        """Returns course name"""
        return self.nam

    def credit_hr(self):
        """Returns course;s credit hours"""
        return self.hours

    def grade(self):
        """Returns course's grade"""
        return self._grade

    def __str__(self):
        return "cs" + str(self.course_num) + " " + self.nam + " Grade:" + str(self._grade) \
               + " Credit Hours: " + str(self.hours)
