import { BrowserRouter, Routes, Route } from 'react-router-dom';
import MainPage from './MainPage';
import Nav from './Nav';
<<<<<<< HEAD
import React from 'react';
import ShoesForm from './ShoesForm';
import ShoesList from './ShoesList';
=======
import HatsList from './HatsList';
import HatForm from './HatForm';
>>>>>>> main

function App(props) {
  if (props.hats === undefined) {
    return null
  }
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
          <Route path="hats">
            <Route path="" element={<HatsList hats={props.hats} /> } />
            <Route path="new" element={<HatForm /> } />
          </Route>
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
