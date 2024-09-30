import React, { useState } from 'react';
import './AddressBar.css';

function AddressBar() {
  const [url, setUrl] = useState('https://www.example.com');

  const handleInputChange = (e) => {
    setUrl(e.target.value);
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      // Handle URL navigation logic here
      alert(`Navigating to: ${url}`);
    }
  };

  return (
    <input
      type="text"
      className="address-bar"
      value={url}
      onChange={handleInputChange}
      onKeyPress={handleKeyPress}
    />
  );
}

export default AddressBar;