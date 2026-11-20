// Task 1 (Translated): Equivalent Java Student class
public class Student {
    private String name;
    private int rollNo;
    private double gpa;

    public Student(String name, int rollNo, double gpa) {
        this.name = name;
        this.rollNo = rollNo;
        this.gpa = gpa;
    }

    public String display() {
        return String.format("Student(name=%s, roll=%d, gpa=%.2f)", name, rollNo, gpa);
    }

    public static void main(String[] args) {
        Student s = new Student("Adagiri Ansika", 23, 9.35);
        System.out.println(s.display());
    }
}
