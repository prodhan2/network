package Soket;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.net.Socket;
import java.util.Scanner;

public class Client {
    public static void main(String[] args) {
        try {
            Socket socket = new Socket("127.0.0.1", 8000);
            System.out.println("Connected to the server on port 8000...");

            DataInputStream dis = new DataInputStream(socket.getInputStream());
            DataOutputStream dos = new DataOutputStream(socket.getOutputStream());
            Scanner scanner = new Scanner(System.in);

            while (true) {
                System.out.print("Enter message for the server (Hi, Time, OK, Exit): ");
                String message = scanner.nextLine();
                dos.writeUTF(message);

                if (message.equalsIgnoreCase("OK")) {
                    for (int i = 0; i < 9; i++) {
                        String serverResponse = dis.readUTF();
                        System.out.println("Server: " + serverResponse);
                    }
                }

                String serverResponse = dis.readUTF();
                System.out.println("Server: " + serverResponse);

                if (serverResponse.equalsIgnoreCase("Bye")) {
                    break;
                }
            }

            scanner.close();
            dis.close();
            dos.close();
            socket.close();
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
