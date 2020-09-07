import React from 'react';

import './styles/Landing.css';

import clubLogo from '../assets/images/logo1.png';
import { Footer } from '../components/Footer';
import { Link } from 'react-router-dom';

class Landing extends React.Component {
  render() {
    return (
      <>
        <section className="landing-section">
          <main>
            <img className="logo-club1" src={ clubLogo } alt="logo club"/>
            <h1 className="welcome">Seguridad y tranquilidad en tus viajes</h1>
            <Link to="/login">
              <button>Login</button>
            </Link>
            <p>¿No tienes cuenta? Regístrate <Link className="register" to="/signup">aquí</Link></p>
          </main>
          <Footer />
        </section>
      </>
    );
  }
}

export default Landing;