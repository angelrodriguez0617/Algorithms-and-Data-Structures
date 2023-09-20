import courselist
from courselist import CourseList
from course import Course
import random

def main():
    mycourses = CourseList()
    with open("C:\\users\\angel\\downloads\\data.txt", "r") as f:
        lines = f.readlines()
        print("Current List: (" + str(len(lines)) + ")")
        for l in lines:
            items = l.split(",")
            mycourses.insert(Course(int(items[0]), items[1], float(items[2]), float(items[3])))

    mycourses.print_list()
    print()
    print("Cumulative GPA: ", round(mycourses.calculate_gpa(), 3))


main()