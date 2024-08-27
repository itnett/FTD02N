import java.io.BufferedReader;
import java.io.File;
import java.io.FileWriter;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Date;
import java.util.List;
import java.util.ArrayList;

public class IntelligentScan {
    private static final String LOGFILE = "scan_results.log";
    
    public static void main(String[] args) {
        if (args.length != 1) {
            System.out.println("Usage: java IntelligentScan <target>");
            System.exit(1);
        }

        String target = args[0];
        try {
            new IntelligentScan().scan(target);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void scan(String target) throws IOException {
        log("Start scanning " + target);

        // Step 1: ARP scan to check if the target is up (least disruptive)
        log("Step 1: Performing ARP scan to check if the target is up");
        runCommand(new String[]{"nmap", "-sn", "-PR", target});

        // Step 2: DNS query to check for open services (very stealthy)
        log("Step 2: Performing DNS query to check for open services");
        runCommand(new String[]{"dig", target});

        // Step 3: Passive OS fingerprinting (completely passive)
        log("Step 3: Performing Passive OS fingerprinting");
        Process p0fProcess = new ProcessBuilder("p0f", "-i", "any", "-p").start();
        try { Thread.sleep(60000); } catch (InterruptedException e) { e.printStackTrace(); }
        p0fProcess.destroy();

        // Step 4: SYN scan for open ports (still stealthy)
        log("Step 4: Performing SYN scan for open ports");
        runCommand(new String[]{"nmap", "-sS", target, "-oN", "syn_scan.txt"});

        List<String> openPorts = parseOpenPorts("syn_scan.txt");
        if (openPorts.isEmpty()) {
            log("No open ports found with SYN scan. Exiting.");
            System.exit(1);
        }
        String openPortsStr = String.join(",", openPorts);
        log("Open ports found: " + openPortsStr);

        // Step 5: Version detection on open ports
        log("Step 5: Performing version detection on open ports");
        runCommand(new String[]{"nmap", "-sV", "-p", openPortsStr, target, "-oN", "version_detection.txt"});

        // Step 6: OS detection (slightly more intrusive)
        log("Step 6: Performing OS detection");
        runCommand(new String[]{"nmap", "-O", target, "-oN", "os_detection.txt"});

        // Step 7: TCP Connect scan on ports that did not respond to SYN scan (more intrusive)
        log("Step 7: Performing TCP Connect scan on ports that did not respond to SYN scan");
        runCommand(new String[]{"nmap", "-sT", "-p", openPortsStr, target, "-oN", "tcp_connect_scan.txt"});

        // Step 8: UDP scan on common ports
        log("Step 8: Performing UDP scan on common ports");
        runCommand(new String[]{"nmap", "-sU", "--top-ports", "20", target, "-oN", "udp_scan.txt"});

        // Step 9: Perform FIN, Xmas, and Null scans (even more intrusive)
        log("Step 9: Performing FIN, Xmas, and Null scans");
        runCommand(new String[]{"nmap", "-sF", "-p", openPortsStr, target, "-oN", "fin_scan.txt"});
        runCommand(new String[]{"nmap", "-sX", "-p", openPortsStr, target, "-oN", "xmas_scan.txt"});
        runCommand(new String[]{"nmap", "-sN", "-p", openPortsStr, target, "-oN", "null_scan.txt"});

        // Step 10: Perform ACK scan to map out firewall rules
        log("Step 10: Performing ACK scan to map out firewall rules");
        runCommand(new String[]{"nmap", "-sA", "-p", openPortsStr, target, "-oN", "ack_scan.txt"});

        // Step 11: Idle scan to further probe stealthily
        log("Step 11: Performing Idle scan to further probe stealthily");
        runCommand(new String[]{"nmap", "-sI", "<zombie_host>", target, "-oN", "idle_scan.txt"});

        // Step 12: Use Hping for more granular control
        log("Step 12: Using Hping for more granular control");
        runCommand(new String[]{"hping3", "-S", target, "-p", openPortsStr, "-c", "1"});
        runCommand(new String[]{"hping3", "-F", target, "-p", openPortsStr, "-c", "1"});
        runCommand(new String[]{"hping3", "-UPF", target, "-p", openPortsStr, "-c", "1"});

        // Step 13: Masscan for fast scanning of large networks
        log("Step 13: Using Masscan for fast scanning of large networks");
        runCommand(new String[]{"masscan", "-p" + openPortsStr, target, "--rate=1000"});

        // Step 14: Netcat for banner grabbing and deeper probing
        log("Step 14: Using Netcat for banner grabbing and deeper probing");
        for (String port : openPorts) {
            runCommand(new String[]{"nc", "-vz", target, port});
        }

        log("Scanning completed for " + target);
    }

    private List<String> parseOpenPorts(String filename) throws IOException {
        List<String> openPorts = new ArrayList<>();
        try (BufferedReader reader = new BufferedReader(new InputStreamReader(new java.io.FileInputStream(filename)))) {
            String line;
            while ((line = reader.readLine()) != null) {
                if (line.contains("/open/")) {
                    openPorts.add(line.split("/")[0].trim());
                }
            }
        }
        return openPorts;
    }

    private void runCommand(String[] command) throws IOException {
        log("Running command: " + String.join(" ", command));
        ProcessBuilder pb = new ProcessBuilder(command);
        pb.redirectErrorStream(true);
        Process process = pb.start();
        try (BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()))) {
            String line;
            while ((line = reader.readLine()) != null) {
                log(line);
            }
        }
    }

    private void log(String message) {
        String timestamp = new Date().toString();
        String logMessage = "[" + timestamp + "] " + message;
        System.out.println(logMessage);
        try (FileWriter fw = new FileWriter(new File(LOGFILE), true)) {
            fw.write(logMessage + "\n");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}