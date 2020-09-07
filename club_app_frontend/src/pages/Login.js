import React from 'react';

import backBtn from '../assets/images/icono-atras-50.png';

import { Link } from 'react-router-dom';

import './styles/Login.css';


class SignUp extends React.Component {
  render() {
    return (
      <>
        <section className="card login-section" >
          <Link to="/"><img src={ backBtn } alt=""/></Link>
          <h1>Login</h1>
          <form action="">
            <input className="input" type="text" name="Usuario" id="" placeholder="Nombre de usuario"/>
            <input className="input" type="password" name="" id="" placeholder="Password"/>
            <input className="button" type="button" value="Login" />
          </form>
          <p>Ingresa con <a href="http://"><b>Facebook</b></a>  o <a href="http://"><b>Google</b></a></p>
          <p>¿No tienes cuenta? Regístrate<Link to="/signup"><b>aquí</b></Link></p>
        </section>
      </>
    );
  }
}

export default SignUp;