import React, { useState } from 'react';
import axios from 'axios';

const InputForm = ({ setResponseData }) => {
  const [jsonData, setJsonData] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async () => {
    setError('');
    try {
      const parsedData = JSON.parse(jsonData);
      const res = await axios.post('https://bajajfinserv-f90c.onrender.com/bfhl', parsedData);  // Change to your Flask backend URL
      setResponseData(res.data);
    } catch (err) {
      setError('Invalid JSON format');
    }
  };

  return (
    <div>
      <h2>Enter JSON Input:</h2>
      <textarea
        value={jsonData}
        onChange={(e) => setJsonData(e.target.value)}
        rows="6"
        cols="50"
        placeholder='{"data": ["A", "C", "z"]}'
      />
      <br />
      <button onClick={handleSubmit}>Submit</button>
      {error && <p style={{ color: 'red' }}>{error}</p>}
    </div>
  );
};

export default InputForm;
