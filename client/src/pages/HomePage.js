import React from 'react';
import { Link } from 'react-router-dom';

function HomePage() {
  return (
    <div>
      <h1>Home</h1>
      <Link to={"/createcv"}>CreateCV</Link>
    </div>
  );
}

export default HomePage;
