import java.util.Scanner;

public class AlphabetCheck {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a character: ");
        char ch = sc.next().charAt(0); // Read a character

        if ((ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z'))
            System.out.println("It is an alphabet");
        else
            System.out.println("It is not an alphabet");
        sc.close();
    }
}
