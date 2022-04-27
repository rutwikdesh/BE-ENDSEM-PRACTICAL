import java.util.*;

public class Diffie_Hellman {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter Prime Number P");
        int p = sc.nextInt();
        System.out.println("Enter primitive root of " + p);
        int g = sc.nextInt();
        System.out.println("Choose Private Key (Alice)");
        int a = sc.nextInt();
        System.out.println("Choose Private Key (BOB)");
        int b = sc.nextInt();

        int A = (int) Math.pow(g, a) % p;
        int B = (int) Math.pow(g, b) % p;

        System.out.println("Public Key (Alice) : " + A);
        System.out.println("Public Key (BOB) : " + B);

        int S_A = (int) Math.pow(B, a) % p;
        int S_B = (int) Math.pow(A, b) % p;

        if (S_A == S_B) {
            System.out.println("ALice and Bob can communicate with each other!!!");
            System.out.println("They share a secret no = " + S_A);
        }

        else {
            System.out.println("ALice and Bob cannot communicate with each other!!!");
        }

        sc.close();
    }
}
