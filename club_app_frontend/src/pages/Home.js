import React from 'react';

import './styles/Home.css';

import { Header } from '../components/Header';
import { Footer } from '../components/Footer';

class Home extends React.Component {
  render() {
    return (
      <>
        <section className="home-section">
          <Header />
          <div id="mapa"></div>
          <main className="home-main">
            <div className="main-avatar"></div>
            <div className="main-info">
              <h3>Hola Nombre</h3>
              <p>¿Vas a viajar?</p>
            </div>
          </main>
          <Footer />
        </section>
      </>
    );
  }
}

export default Home;