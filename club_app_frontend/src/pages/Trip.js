import React from 'react';

import './styles/Trip.css';

import { Header } from '../components/Header';
import { Footer } from '../components/Footer';

class Trip extends React.Component {
  data = [];
  state={};
  handleChange = e => {
    // console.log({ name: e.target.name, value: e.target.value });
    this.setState({
      [e.target.name]: e.target.value
    });
  };

  handleClick = e => {
    console.log('Button was clicked');
  };

  handleSubmit = e => {
    e.preventDefault();
    this.data.push(this.state);
    console.log(this.data);
  };

  render() {
    return (
      <>
        <section className="trip-section">
          <Header />
          <div id="mapa"></div>
          <main className="trip-main main-info">
            <form className="trip-form" onSubmit={this.handleSubmit}>
              <input onChange={this.handleChange} className="input-trip" type="text" name="origin" id="" placeholder="¿Dónde estás?" value={this.state.origin}/>
              <input onChange={this.handleChange} className="input-trip" type="text" name="destination" id="" placeholder="¿A dónde vas?" value={this.state.destination}/>
              <input onClick={this.handleClick} className="button-trip" type="submit" value="Viajar"/>
            </form>
          </main>
          <Footer />
        </section>
      </>
    );
  }
}

export default Trip;