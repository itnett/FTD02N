import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [sporsmal, setSporsmal] = useState("");
  const [svar, setSvar] = useState("");

  const sendSporsmal = async () => {
    const response = await axios.post('/api/svar', { sporsmal: sporsmal });
    setSvar(response.data.svar);
  };

  return (
    <div>
      <h1>Yrkesrettet Kommunikasjon Assistent</h1>
      <input
        type="text"
        value={sporsmal}
        onChange={(e) => setSporsmal(e.target.value)}
        placeholder="Skriv ditt spørsmål her"
      />
      <button onClick={sendSporsmal}>Send</button>
      <p>{svar}</p>
    </div>
  );
}

export default App;