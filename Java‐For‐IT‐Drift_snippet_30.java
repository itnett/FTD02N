import java.io.File;
import javax.mail.*;
import javax.mail.internet.*;

public class DiskSpaceMonitor {
    public static void main(String[] args) {
        File disk = new File("/");

        long freeSpace = disk.getFreeSpace();
        long totalSpace = disk.getTotalSpace();
        long usedSpace = totalSpace - freeSpace;
        double usedPercentage = (double) usedSpace / totalSpace * 100;

        if (usedPercentage > 90) {
            sendEmailAlert(usedPercentage);
        }
    }

    private static void sendEmailAlert(double usedPercentage) {
        // Dummy email sending logic
        System.out.println("Sending email alert: Disk usage is " + usedPercentage + "%");
    }
}