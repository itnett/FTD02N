import java.io.File;

   public class DiskSpaceMonitor {
       public static void main(String[] args) {
           File disk = new File("/");

           long freeSpace = disk.getFreeSpace();
           long totalSpace = disk.getTotalSpace();
           long usedSpace = totalSpace - freeSpace;
           double usedPercentage = (double) usedSpace / totalSpace * 100;

           System.out.printf("Diskbruk: %.2f%%\n", usedPercentage);

           if (usedPercentage > 90) {
               System.out.println("Advarsel: Diskbruk overstiger 90%");
           }
       }
   }