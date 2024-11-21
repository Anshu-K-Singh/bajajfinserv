import React, { useState } from 'react';
import InputForm from './InputForm';
import ResponseDisplay from './ResponseDisplay';

function App() {
  const [responseData, setResponseData] = useState(null);

  return (
    <div className="App">
      <h1>Your Roll Number: ABCD123</h1>
      <InputForm setResponseData={setResponseData} />
      {responseData && <ResponseDisplay responseData={responseData} />}
    </div>
  );
}

export default App;
