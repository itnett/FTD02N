function ITSecurityAdvice() {
  const [problem, setProblem] = useState("");
  const [advice, setAdvice] = useState("");

  const getAdvice = async () => {
    const response = await axios.post('/api/itsikkerhet', { problem: problem });
    setAdvice(response.data.råd);
  };

  return (
    <div>
      <h1>Få råd om IT-sikkerhet</h1>
      <input
        type="text"
        value={problem}
        onChange={(e) => setProblem(e.target.value)}
        placeholder="Beskriv problemet her"
      />
      <button onClick={getAdvice}>Få råd</button>
      <p>{advice}</p>
    </div>
  );
}

export default ITSecurityAdvice;