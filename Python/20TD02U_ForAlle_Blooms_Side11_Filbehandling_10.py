python
import os

filstørrelse = os.path.getsize('eksempel.txt')
sist_endret = os.path.getmtime('eksempel.txt')

print(f'Filstørrelse: {filstørrelse} bytes')
print(f'Sist endret: {sist_endret}')