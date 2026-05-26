import java.util.Scanner;

public class StudentGradeCalculator {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        // Taking marks input
        System.out.print("Enter marks for Subject 1: ");
        int sub1 = sc.nextInt();

        System.out.print("Enter marks for Subject 2: ");
        int sub2 = sc.nextInt();

        System.out.print("Enter marks for Subject 3: ");
        int sub3 = sc.nextInt();

        System.out.print("Enter marks for Subject 4: ");
        int sub4 = sc.nextInt();

        System.out.print("Enter marks for Subject 5: ");
        int sub5 = sc.nextInt();

        // Calculating total
        int total = sub1 + sub2 + sub3 + sub4 + sub5;

        // Calculating average percentage
        double average = total / 5.0;

        // Grade calculation
        String grade;

        if (average >= 90) {
            grade = "A+";
        } 
        else if (average >= 80) {
            grade = "A";
        } 
        else if (average >= 70) {
            grade = "B";
        } 
        else if (average >= 60) {
            grade = "C";
        } 
        else if (average >= 50) {
            grade = "D";
        } 
        else {
            grade = "Fail";
        }

        // Displaying result
        System.out.println("\n----- Result -----");
        System.out.println("Total Marks = " + total);
        System.out.println("Average Percentage = " + average);
        System.out.println("Grade = " + grade);

        sc.close();
    }
}