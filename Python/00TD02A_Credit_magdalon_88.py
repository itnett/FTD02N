python
import shutil

maks_diskbruk_prosent = 90

while True:
    total, brukt, ledig = shutil.disk_usage("/")
    brukt_prosent = brukt / total * 100

    if brukt_prosent > maks_diskbruk_prosent:
        print(f"Advarsel: Diskbruk på {brukt_prosent:.1f}%")
    else:
        print(f"Diskbruk: {brukt_prosent:.1f}%")

    # Vent i 60 sekunder før neste sjekk
    time.sleep(60)