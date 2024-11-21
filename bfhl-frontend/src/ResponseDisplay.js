import React, { useState } from 'react';

const ResponseDisplay = ({ responseData }) => {
  const [selectedOption, setSelectedOption] = useState([]);

  const handleChange = (event) => {
    const { options } = event.target;
    const selectedValues = [];
    for (let i = 0, l = options.length; i < l; i++) {
      if (options[i].selected) {
        selectedValues.push(options[i].value);
      }
    }
    setSelectedOption(selectedValues);
  };

  const renderResponse = () => {
    if (responseData) {
      const response = {};
      if (selectedOption.includes('Alphabets')) {
        response.alphabets = responseData.alphabets;
      }
      if (selectedOption.includes('Numbers')) {
        response.numbers = responseData.numbers;
      }
      if (selectedOption.includes('Highest lowercase alphabet')) {
        response.highest_lowercase_alphabet = responseData.highest_lowercase_alphabet;
      }
      return (
        <div>
          <h3>Filtered Response:</h3>
          <pre>{JSON.stringify(response, null, 2)}</pre>
        </div>
      );
    }
    return null;
  };

  return (
    <div>
      <h3>Select Data to Display:</h3>
      <select multiple={true} onChange={handleChange}>
        <option value="Alphabets">Alphabets</option>
        <option value="Numbers">Numbers</option>
        <option value="Highest lowercase alphabet">Highest lowercase alphabet</option>
      </select>
      {renderResponse()}
    </div>
  );
};

export default ResponseDisplay;
