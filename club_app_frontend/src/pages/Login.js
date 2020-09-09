import React from 'react';
import { Link } from 'react-router-dom';
import backBtn from '../assets/images/icono-atras-50.png';
import { loginUser } from '../services/index';
import './styles/Login.css';

class SignUp extends React.Component {
  data;
  state = {};
  handleChange = (e) => {
    this.setState({
      [e.target.name]: e.target.value,
    });
  };

  handleClick = (e) => {
    console.log('Button was clicked');
  };

  handleSubmit = (e) => {
    e.preventDefault();
    this.data = this.state;
    loginUser(this.data);
  };
  render() {
    return (
      <>
        <section className='card login-section'>
          <Link to='/'>
            <img src={backBtn} alt='' />
          </Link>
          <h1>Login</h1>
          <form onSubmit={(e) => this.handleSubmit(e)}>
            <input
              onChange={(e) => this.handleChange(e)}
              className='input'
              type='email'
              value={this.state.email}
              name='email'
              placeholder='Email'
            />
            <input
              onChange={(e) => this.handleChange(e)}
              className='input'
              type='password'
              name='password'
              value={this.state.password}
              placeholder='Password'
            />
            <button className="button" type='submit' onClick={this.handleClick}>
              Ingresar
            </button>
          </form>
          <p>
            Ingresa con{' '}
            <a href='http://'>
              <b>Facebook</b>
            </a>{' '}
            o{' '}
            <a href='http://'>
              <b>Google</b>
            </a>
          </p>
          <p>
            ¿No tienes cuenta? Regístrate
            <Link to='/signup'>
              <b>aquí</b>
            </Link>
          </p>
        </section>
      </>
    );
  }
}

export default SignUp;
