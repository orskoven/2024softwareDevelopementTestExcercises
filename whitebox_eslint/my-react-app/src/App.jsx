import React from 'react';
import BrowserHeader from './components/BrowserHeader';
import BrowserContent from './components/BrowserContent';
import './App.css'; // We'll define global styles here

function App() {
  return (
    <div className="app-container">
      <BrowserHeader />
      <BrowserContent />
    </div>
  );
}

export default App;