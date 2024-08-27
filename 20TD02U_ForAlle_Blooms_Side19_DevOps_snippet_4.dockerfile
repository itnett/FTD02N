# Start med en base image
FROM openjdk:11-jre-slim

# Sett arbeidskatalogen
WORKDIR /app

# Kopier JAR-filen
COPY target/myapp.jar myapp.jar

# Kjør applikasjonen
ENTRYPOINT ["java", "-jar", "myapp.jar"]