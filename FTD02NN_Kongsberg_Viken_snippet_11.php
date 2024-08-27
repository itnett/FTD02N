$sql = "SELECT * FROM Kunder";
   $result = $conn->query($sql);

   if ($result->num_rows > 0) {
       while($row = $result->fetch_assoc()) {
           echo "ID: " . $row["KundeID"]. " - Navn: " . $row["Navn"]. " - Adresse: " . $row["Adresse"]. "<br>";
       }
   } else {
       echo "0 results";
   }
   $conn->close();