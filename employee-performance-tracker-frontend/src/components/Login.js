// src/components/Login.js
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom'; // Import useNavigate for redirection
import axiosInstance from '../api/axios'; // Import the axios instance
import '../styles/Login.css'; // Importing styles

const Login = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [errorMessage, setErrorMessage] = useState('');
    const [isLoading, setIsLoading] = useState(false);
    const navigate = useNavigate(); // Initialize useNavigate for redirection

    const handleSubmit = async (e) => {
        e.preventDefault();
        setErrorMessage('');
        setIsLoading(true);

        try {
            const response = await axiosInstance.post('/login/', {
                username,
                password,
            });

            // Store token in localStorage
            localStorage.setItem('token', response.data.token);

            // Redirect to dashboard based on user role
            navigate('/dashboard'); // Redirect to the dashboard after successful login
        } catch (error) {
            setErrorMessage('Login failed. Please check your credentials and try again.');
            console.error(error);
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <div className="login-container">
            <form onSubmit={handleSubmit} className="login-form">
                <h2>Login</h2>
                {errorMessage && <div className="error-message">{errorMessage}</div>}
                <input
                    type="text"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    placeholder="Username"
                    required
                />
                <input
                    type="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    placeholder="Password"
                    required
                />
                <button type="submit" disabled={isLoading}>
                    {isLoading ? 'Logging in...' : 'Login'}
                </button>
            </form>
        </div>
    );
};

export default Login;
