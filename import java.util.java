import java.util.Scanner;

// Bank Account Class
class BankAccount {

    double balance = 1000;

    // Deposit Method
    void deposit(double amount) {
        balance = balance + amount;
        System.out.println("Amount Deposited Successfully.");
    }

    // Withdraw Method
    void withdraw(double amount) {

        if (amount <= balance) {
            balance = balance - amount;
            System.out.println("Please collect your cash.");
        } 
        else {
            System.out.println("Insufficient Balance.");
        }
    }

    // Check Balance Method
    void checkBalance() {
        System.out.println("Current Balance: " + balance);
    }
}

// ATM Main Class
public class ATM {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        BankAccount user = new BankAccount();

        int choice;

        do {

            System.out.println("\n===== ATM MENU =====");
            System.out.println("1. Deposit");
            System.out.println("2. Withdraw");
            System.out.println("3. Check Balance");
            System.out.println("4. Exit");

            System.out.print("Enter your choice: ");
            choice = sc.nextInt();

            if (choice == 1) {

                System.out.print("Enter deposit amount: ");
                double amount = sc.nextDouble();

                if (amount > 0) {
                    user.deposit(amount);
                } 
                else {
                    System.out.println("Invalid Amount.");
                }

            } 
            else if (choice == 2) {

                System.out.print("Enter withdraw amount: ");
                double amount = sc.nextDouble();

                if (amount > 0) {
                    user.withdraw(amount);
                } 
                else {
                    System.out.println("Invalid Amount.");
                }

            } 
            else if (choice == 3) {

                user.checkBalance();

            } 
            else if (choice == 4) {

                System.out.println("Thank You for Using ATM.");

            } 
            else {

                System.out.println("Invalid Choice.");

            }

        } while (choice != 4);

        sc.close();
    }
}