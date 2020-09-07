import React from "react";
import { compose, withProps, lifecycle } from "recompose";
import { withGoogleMap, GoogleMap, DirectionsRenderer } from "react-google-maps";

import './styles/Map.css';

const Map = compose(
  withProps({
    loadingElement: <div style={{ height: `700px` }} />,
    containerElement: <div style={{ height: `500px` }} />,
    mapElement: <div style={{ height: `50%`, width: `360px` }} />,
  }),
  withGoogleMap,
  lifecycle({
    componentDidMount() {
      const DirectionsService = new window.google.maps.DirectionsService();
      const DistanceService = new window.google.maps.DistanceMatrixService();

      DirectionsService.route({
        origin: new window.google.maps.LatLng(this.props.origin.lat, this.props.origin.lng),
        destination: new window.google.maps.LatLng(this.props.destination.lat, this.props.destination.lng),
        travelMode: window.google.maps.TravelMode.DRIVING,
      }, (result, status) => {
        if (status === window.google.maps.DirectionsStatus.OK) {
          this.setState({
            directions: result,
          });
        } else {
          console.error(`error fetching directions ${result}`);
        }
      });

      DistanceService.getDistanceMatrix({
        origins: [new window.google.maps.LatLng(this.props.origin.lat, this.props.origin.lng)],
        destinations: [new window.google.maps.LatLng(this.props.destination.lat, this.props.destination.lng)],
        travelMode: window.google.maps.TravelMode.DRIVING,
        avoidHighways: false,
        avoidTolls: false,
        unitSystem: window.google.maps.UnitSystem.METRIC
      },
        (result, status) => {
          this.setState({
            originAddresses: result.originAddresses,
            destinationAddresses: result.destinationAddresses,
            distance: result.rows[0].elements[0].distance.text,
            duration: result.rows[0].elements[0].duration.text,
          })
        }
      );
    }
  })
)((props) =>
  <div className="map">
    <GoogleMap
      defaultZoom={8}
      defaultCenter={{ lat: 4.624335, lng: -74.063644 }}
    >
      {props.directions && <DirectionsRenderer directions={props.directions} />}
    </GoogleMap>
    <div className="sub-information">
      <h2 className="titulo">Datos del Viaje: {props.description}</h2>
      <div className="datos-viaje">
        <div>
          <div>
            <p>Distancia:</p>
            <h3><strong>{props.distance}</strong></h3>
          </div>
          <div>
            <p>Origen:</p>
            <h3><strong>{props.originValue} </strong></h3>
          </div>
        </div>
        <div>
          <div>
            <p>Tiempo de viaje:</p>
            <h3><strong>{props.duration}</strong></h3>
          </div>
          <div>
            <p>Destino:</p>
            <h3><strong>{props.destinationValue}</strong></h3>
          </div>
        </div>
      </div>
    </div>
  </div>
)

export default Map;