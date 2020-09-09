import React from 'react';

import axios from 'axios';

const baseUrl = 'http://localhost:8000';

export async function saveUser (userData) {
  try {
    console.log(userData);
    const formData =new FormData()

    formData.append('username', userData.username)
    formData.append('first_name', userData.first_name)
    formData.append('last_name', userData.last_name)
    formData.append('email', userData.email)
    formData.append('phone_number', userData.phone_number)
    formData.append('password', userData.password)
    const response = await axios({
      url: `${baseUrl}/users/signup/`,
      method: 'POST',
      data: formData,
    })

    return response
  } catch(error) {
    console.log(error);
  }
}


