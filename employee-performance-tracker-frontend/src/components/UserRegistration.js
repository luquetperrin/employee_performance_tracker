// src/components/UserRegistration.js
import React, { useState } from 'react';
import axiosInstance from '../api/axios'; // Use axiosInstance
import '../styles/UserForm.css'; // Adjust the import path based on your folder structure

const UserRegistration = () => {
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [role, setRole] = useState('');
    const [errorMessage, setErrorMessage] = useState('');
    const [isLoading, setIsLoading] = useState(false);
    const [successMessage, setSuccessMessage] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        setIsLoading(true);
        setErrorMessage('');
        setSuccessMessage('');

        try {
            // Use the response variable
            const response = await axiosInstance.post('/register/', {
                username,
                email,
                password,
                role,
            });

            // Log the response data (optional)
            console.log('Registration successful:', response.data);

            setSuccessMessage('Registration successful! You can now log in.');
            setUsername('');
            setEmail('');
            setPassword('');
            setRole('');
        } catch (error) {
            setErrorMessage('Registration failed. Please try again.');
            console.error('Registration error:', error);
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <div className="user-registration-container">
            <form onSubmit={handleSubmit} className="user-registration-form">
                <h2>Register</h2>
                {errorMessage && <div className="error-message">{errorMessage}</div>}
                {successMessage && <div className="success-message">{successMessage}</div>}
                <input
                    type="text"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    placeholder="Username"
                    required
                />
                <input
                    type="email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    placeholder="Email"
                    required
                />
                <input
                    type="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    placeholder="Password"
                    required
                />
                <input
                    type="text"
                    value={role}
                    onChange={(e) => setRole(e.target.value)}
                    placeholder="Role"
                    required
                />
                <button type="submit" disabled={isLoading}>
                    {isLoading ? 'Registering...' : 'Register'}
                </button>
            </form>
        </div>
    );
};

export default UserRegistration;
