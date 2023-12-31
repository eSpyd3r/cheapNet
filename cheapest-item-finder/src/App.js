import React from 'react';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Cheapest Item Finder</h1>
      </header>
      <div className="Search-area">
        <input type="text" placeholder="Search for an item..." className="Search-input"/>
        <button className="Search-button">Search</button>
      </div>
      <footer className="App-footer">
        <p>© 2023 Cheapest Item Finder</p>
      </footer>
    </div>
  );
}

export default App;
