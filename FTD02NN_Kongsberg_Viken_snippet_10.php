$conn = new mysqli('localhost', 'brukernavn', 'passord', 'database');
   if ($conn->connect_error) {
       die("Connection failed: " . $conn->connect_error);
   }