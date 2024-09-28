// src/components/PrivateRoute.js
import React from 'react';
import { Route, Redirect } from 'react-router-dom';

// A component to guard routes that require authentication
const PrivateRoute = ({ component: Component, ...rest }) => {
    const isAuthenticated = !!localStorage.getItem('token'); // Check if the user has a token

    return (
        <Route
            {...rest}
            render={(props) =>
                isAuthenticated ? <Component {...props} /> : <Redirect to="/" />
            }
        />
    );
};

export default PrivateRoute;
