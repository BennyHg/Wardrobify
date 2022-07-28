import { BrowserRouter, Routes, Route } from 'react-router-dom';
import MainPage from './MainPage';
import Nav from './Nav';
import React from 'react';
import ShoesForm from './ShoesForm';
import ShoesList from './ShoesList';

function App() {
  return (
    <BrowserRouter>
      <Nav />
      <div className="container">
        <Routes>
        <Route path="shoes">
            <Route path="new" element={<ShoesForm />} />
            <Route path="" element={<ShoesList />} />
          </Route>
          <Route path="/" element={<MainPage />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
