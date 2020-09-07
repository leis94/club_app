import React from 'react';

import './styles/TripInfo.css';


class TripInfo extends React.Component {
  render() {
    return (
      <>
        <section class="card trip-info-section" >
          <a href=""><img src="./assets/icono-atras-50.png" alt=""/></a>
          <h1>Datos de tu viaje</h1>
          <div class="datos-viaje">
            <p>Origen</p>
            <h3>Datos de origen</h3>
            <p>Destino</p>
            <h3>Datos del destino</h3>
            <p>Duración del viaje</p>
            <h3>30 minutos</h3>
            <p>Costo del viaje</p>
            <h3>$10.000</h3>
          </div>
          <input class="button" type="button" value="Confirmar viaje"/>
        </section>
      </>
    );
  }
}

export default TripInfo;