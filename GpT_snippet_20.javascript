function CanvasAssignments() {
  const [kursId, setKursId] = useState("");
  const [oppgaver, setOppgaver] = useState([]);

  const fetchAssignments = async () => {
    const response = await axios.get(`/api/oppgaver?kurs_id=${kursId}`);
    setOppgaver(response.data);
  };

  return (
    <div>
      <h1>Canvas Oppgaver</h1>
      <input
        type="text"
        value={kursId}
        onChange={(e) => setKursId(e.target.value)}
        placeholder="Skriv kurs ID her"
      />
      <button onClick={fetchAssignments}>Hent Oppgaver</button>
      <ul>
        {oppgaver.map((oppgave, index) => (
          <li key={index}>{oppgave.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default CanvasAssignments;