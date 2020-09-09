import React from 'react';

import axios from 'axios';

const baseUrl = 'aqui-va-la-url';

export async function saveUser (userData) {
  try {
    console.log(userData);
    const formData =new FormData()

    formData.append('userName', userData.userName)
    formData.append('firstName', userData.firstName)
    formData.append('lastName', userData.lastName)
    formData.append('email', userData.email)
    formData.append('tel', userData.tel)
    formData.append('password', userData.password)
    const response = await axios({
      url: `${baseUrl}/user`,
      method: 'POST',
      data: formData,
    })

    return response
  } catch(error) {
    console.log(error);
  }
}


