import React from 'react';
import { Link } from 'react-router-dom';

import './styles/Header.css';
import clubLogo from '../assets/images/clon-uber-pin.png';

export const Header = () => {
  return (
    <>
      <div className="header">
        <img src={ clubLogo } alt="Logo Club" />
        <Link to="/">Logout</Link>
      </div>
    </>
  )
}

