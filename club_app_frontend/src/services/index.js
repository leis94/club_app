const baseUrl = 'http://localhost:8000';

export async function createUser(userData) {
  try {
    const response = await fetch(`${baseUrl}/users/signup/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(userData),
    });
    console.log('saveUser -> response', response);
    return response;
  } catch (error) {
    console.log(error);
  }
}

export async function loginUser(user) {
  try {
    const response = await fetch(`${baseUrl}/users/login/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(user),
    });
    const data = await response.json();
    console.log('loginUser -> data', data);
    return data;
  } catch (error) {
    console.log(error);
  }
}
