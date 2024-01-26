import React, { useState } from 'react';
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Link
} from 'react-router-dom';
import './App.css';

function App() {
  const [isMenuOpen, setMenuOpen] = useState(false);

  const toggleMenu = () => {
    setMenuOpen(!isMenuOpen);
  };

  return (
    <Router>
      <div className="App">
        <header className="App-header">
          <div className="Menu-icon" onClick={toggleMenu}>
            ☰
          </div>
          <h1>Cheapest Item Finder</h1>
        </header>
        <div className={`Menu-slider ${isMenuOpen ? 'show' : ''}`}>
          <ul>
            <li onClick={toggleMenu}>
              <Link to="/" className="menu-link">Home</Link>
            </li>
            <li>Account</li> {/* Update this similarly when you have a route */}
          </ul>
        </div>

        <Routes>
          <Route path="/" element={
            <div className="Search-area">
              <input type="text" placeholder="Search for an item..." className="Search-input"/>
              <button className="Search-button">Search</button>
            </div>
          } />
          {/* Add more Route components here as your app grows */}
        </Routes>

        <footer className="App-footer">
          <p>© 2023 Cheapest Item Finder</p>
        </footer>
      </div>
    </Router>
  );
}

export default App;
