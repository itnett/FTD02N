public class Server {
    private String ipAddress;
    private int port;

    public Server(String ipAddress, int port) {
        this.ipAddress = ipAddress;
        this.port = port;
    }

    public void start() {
        System.out.println("Server starting at " + ipAddress + ":" + port);
    }
}

public class Main {
    public static void main(String[] args) {
        Server server = new Server("192.168.1.1", 8080);
        server.start();
    }
}