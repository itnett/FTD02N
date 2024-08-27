FROM python:3.8-slim

   # Angi miljøvariabler
   ENV DB_HOST=db.example.com
   ENV DB_USER=admin
   ENV DB_PASSWORD=secret

   # Kopier og installer app
   COPY . /app
   WORKDIR /app
   RUN pip install -r requirements.txt

   CMD ["python", "app.py"]