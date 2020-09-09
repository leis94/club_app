import React from 'react';
import { Link } from 'react-router-dom';
import backBtn from '../assets/images/icono-atras-50.png';
import { createUser } from '../services/index';
import './styles/SignUp.css';

class SignUp extends React.Component {
  data;
  state = {};
  handleChange = (e) => {
    // console.log({ name: e.target.name, value: e.target.value });
    this.setState({
      [e.target.name]: e.target.value,
    });
  };

  handleClick = (e) => {
    
  };

  handleSubmit = (e) => {
    e.preventDefault();
    this.data = this.state;
    createUser(this.data);
    // console.log(this.data);
  };

  render() {
    return (
      <>
        <section className='card signup-section'>
          <Link to='/'>
            <img src={backBtn} alt='' />
          </Link>
          <h1>Registro</h1>
          <form onSubmit={this.handleSubmit}>
            <input
              onChange={this.handleChange}
              className='input'
              type='text'
              name='username'
              // id=""
              placeholder='Nombre de usuario'
              value={this.state.username}
            />
            <input
              onChange={this.handleChange}
              className='input'
              type='text'
              name='first_name'
              // id=""
              placeholder='Nombres'
              value={this.state.first_name}
            />
            <input
              onChange={this.handleChange}
              className='input'
              type='text'
              name='last_name'
              // id=""
              placeholder='Tu nombre completo'
              value={this.state.last_name}
            />
            <input
              onChange={this.handleChange}
              className='input'
              type='email'
              name='email'
              // id=""
              placeholder='Tu email'
              value={this.state.email}
            />
            <input
              onChange={this.handleChange}
              className='input'
              type='tel'
              name='phone_number'
              // id=""
              placeholder='Número de celular'
              value={this.state.phone_number}
            />
            <input
              onChange={this.handleChange}
              className='input'
              type='password'
              name='password'
              // id=""
              placeholder='Password'
              value={this.state.password}
            />
            <button className="button" type='submit' onClick={this.handleClick}>
              Registrarse
            </button>
          </form>
          <p>
            Regístrate con{' '}
            <a href='http://'>
              <b>Facebook</b>
            </a>{' '}
            o{' '}
            <a href='http://'>
              <b>Google</b>
            </a>
          </p>
          <p>
            ¿Ya tienes cuenta? Ingresa
            <Link to='/login'>
              <b>aquí</b>
            </Link>
          </p>
        </section>
      </>
    );
  }
}

export default SignUp;
