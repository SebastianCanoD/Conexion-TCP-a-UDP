import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;

public class Problema1 {
    public static void main(String[] args) {
        try {
            DatagramSocket socket = new DatagramSocket();
            InetAddress address = InetAddress.getByName("localhost");
            byte[] buf = "Hola, servidor TCP".getBytes();

            DatagramPacket packet = new DatagramPacket(buf, buf.length, address, 65432);
            socket.send(packet);
            socket.close();
        } catch (Exception e) {
            e.printStackTrace();
}
}
}