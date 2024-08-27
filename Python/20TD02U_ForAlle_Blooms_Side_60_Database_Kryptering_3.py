python
import time

# Mål tid for innsats av ukryptert data
start_time = time.time()
cursor.execute("INSERT INTO brukere (id, navn, personnummer) VALUES (2, 'Per Hansen', '11223344556')")
conn.commit()
ukryptert_tidsbruk = time.time() - start_time

# Mål tid for innsats av kryptert data
start_time = time.time()
cursor.execute(kryptert_sql, (3, 'Lise Olsen', '55667788990', 'hemmelignøkkel'))
conn.commit()
kryptert_tidsbruk = time.time() - start_time

print(f"Ukryptert tid: {ukryptert_tidsbruk} sekunder")
print(f"Kryptert tid: {kryptert_tidsbruk} sekunder")