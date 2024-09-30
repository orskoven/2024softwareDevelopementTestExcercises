import React from 'react';
import './BrowserContent.css';

function BrowserContent() {
  return (
    <div className="browser-content">
      <iframe
        src="https://www.example.com"
        title="Browser Content"
        frameBorder="0"
      ></iframe>
    </div>
  );
}

export default BrowserContent;