// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Login from './components/Login';
import Dashboard from './components/Dashboard';
import ManagerDashboard from './components/ManagerDashboard';
import UserRegistration from './components/UserRegistration';
import PrivateRoute from './components/PrivateRoute'; // For authenticated routes

const App = () => {
    return (
        <Router>
            <div>
                {/* Switch will go through the routes in the order they are defined */}
                <Switch>
                    {/* Public Route - Login */}
                    <Route exact path="/" component={Login} />

                    {/* Public Route - User Registration */}
                    <Route path="/register" component={UserRegistration} />

                    {/* Private Routes - Accessible only if logged in */}
                    <PrivateRoute path="/dashboard" component={Dashboard} />
                    <PrivateRoute path="/manager-dashboard" component={ManagerDashboard} />
                </Switch>
            </div>
        </Router>
    );
};

export default App;
