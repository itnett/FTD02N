python
    VC_per_enhet = 33000  # Variable kostnader per enhet
    P = 55000  # Pris per enhet

    DB_per_enhet = P - VC_per_enhet
    NPE = FTK / DB_per_enhet
    print(f"Nullpunkt i antall enheter (NPE): {NPE}")