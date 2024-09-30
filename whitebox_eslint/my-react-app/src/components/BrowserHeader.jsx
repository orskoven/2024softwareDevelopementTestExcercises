import React, { useState, useEffect } from 'react';
import { FaArrowLeft, FaArrowRight, FaRedo, FaHome, FaMoon, FaSun } from 'react-icons/fa';
import AddressBar from './AddressBar';
import './BrowserHeader.css';

function BrowserHeader() {
  const [darkMode, setDarkMode] = useState(false);

  useEffect(() => {
    if (darkMode) {
      document.body.classList.add('dark');
    } else {
      document.body.classList.remove('dark');
    }
  }, [darkMode]);

  const toggleDarkMode = () => setDarkMode(!darkMode);

  return (
    <div className="browser-header">
      <div className="navigation-buttons">
        <button className="nav-button"><FaArrowLeft /></button>
        <button className="nav-button"><FaArrowRight /></button>
        <button className="nav-button"><FaRedo /></button>
        <button className="nav-button home-button"><FaHome /></button>
      </div>
      <AddressBar />
      <button className="nav-button theme-toggle" onClick={toggleDarkMode}>
        {darkMode ? <FaSun /> : <FaMoon />}
      </button>
    </div>
  );
}

export default BrowserHeader;