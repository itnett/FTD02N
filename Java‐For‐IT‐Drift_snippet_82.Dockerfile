# Bruk en offisiell OpenJDK runtime som base image
   FROM openjdk:11-jre-slim

   # Sett arbeidskatalogen i containeren
   WORKDIR /app

   # Kopier jar-filen til containeren
   COPY target/myapp.jar myapp.jar

   # Kjør applikasjonen
   ENTRYPOINT ["java", "-jar", "myapp.jar"]