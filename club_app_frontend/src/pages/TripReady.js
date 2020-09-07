import React from 'react';

import './styles/TripReady.css';

import { Header } from '../components/Header';
import { Footer } from '../components/Footer';

class Home extends React.Component {
  render() {
    return (
      <>
        <section>
          <Header />
          <div id="mapa"></div>
          <main>
            <div class="origen-destino">
              <div class="origen">
                <p>Origen</p>
                <h3>Datos de origen</h3>
              </div>
              <div class="destino">
                <p>Destino</p>
                <h3>Datos del destino</h3>
              </div>
            </div>
            <div class="duracion-precio">
              <div class="duracion">
                <p>Duración del viaje</p>
                <h3>30 minutos</h3>
              </div>
              <div class="precio">
                <p>Costo del viaje</p>
                <h3>$10.000</h3>
              </div>
            </div>
          </main>
          <Footer />
        </section>
      </>
    );
  }
}

export default Home;