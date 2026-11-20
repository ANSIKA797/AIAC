"""Task 1 (Source): Python Student class."""


class Student:
    def __init__(self, name: str, roll_no: int, gpa: float):
        self.name = name
        self.roll_no = roll_no
        self.gpa = gpa

    def display(self) -> str:
        return f"Student(name={self.name}, roll={self.roll_no}, gpa={self.gpa:.2f})"


if __name__ == "__main__":
    s = Student("Adagiri Ansika", 23, 9.35)
    print(s.display())
