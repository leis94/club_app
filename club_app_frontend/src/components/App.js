import React from 'react';
import { BrowserRouter, Switch, Route, Redirect } from 'react-router-dom';

import Landing from '../pages/Landing';
// import Home from '../pages/Home';
import Login from '../pages/Login';
import SignUp from '../pages/SignUp';
import NotFound from '../pages/NotFound';
// import Trip from '../pages/Trip';
import Dashboard from '../pages/Dashboard';

function App() {
  return (
    <BrowserRouter>
        <Switch>
          <Route exact path="/" component={Landing} />
          <Route exact path="/login" component={Login} />
          <Route exact path="/signup" component={SignUp} />
          {/* <Route exact path="/home" component={Home} /> */}
          {/* <Route exact path="/trip" component={Trip} /> */}
          <Route exact path="/dashboard" name="dashboard" component={Dashboard} />
          <Route component={NotFound} />
          <Redirect to="/" />
        </Switch>
    </BrowserRouter>
  );
}

export default App;