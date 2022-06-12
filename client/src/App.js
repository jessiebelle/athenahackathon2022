import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Footer from './components/Footer';
import Header from './components/Header';
import CreateCV from './pages/CreateCV';
import HomePage from './pages/HomePage';
import PreviewCV from './pages/PreviewCV';

function App() {
  return (
    <div
      style={{
        margin: '20px',
      }}
    >
      <Router>
        <main className="py-3">
          <Routes>
            {/* <Route path="/" element={<HomePage />} />
            <Route path="/createCV" element={<CreateCV />} /> */}
            <Route path="/" element={<PreviewCV />} />
          </Routes>
        </main>
      </Router>
    </div>
  );
}

export default App;
