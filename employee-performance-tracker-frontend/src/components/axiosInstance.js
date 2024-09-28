// src/components/UserForm.js
import React, { useState, useEffect } from 'react';
import axiosInstance from '../api/axios'; // Use axiosInstance
import '../styles/UserForm.css';

const UserForm = ({ userId, onClose }) => {
    const [username, setUsername] = useState('');
    const [role, setRole] = useState('');
    const [password, setPassword] = useState('');
    const [errorMessage, setErrorMessage] = useState('');
    const [isLoading, setIsLoading] = useState(false);

    useEffect(() => {
        const fetchUser = async () => {
            if (userId) {
                try {
                    const response = await axiosInstance.get(`/users/${userId}/`);
                    setUsername(response.data.username);
                    setRole(response.data.role);
                } catch (error) {
                    setErrorMessage('Failed to load user data. Please try again.');
                }
            }
        };

        fetchUser();
    }, [userId]);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setErrorMessage('');
        setIsLoading(true);

        const userData = {
            username,
            role,
            ...(password && { password }),
        };

        try {
            if (userId) {
                await axiosInstance.put(`/users/${userId}/`, userData);
                alert('User updated successfully!');
            } else {
                await axiosInstance.post('/users/', userData);
                alert('User created successfully!');
            }

            setUsername('');
            setRole('');
            setPassword('');
            onClose(); // Close the form after submission
        } catch (error) {
            setErrorMessage('Failed to save user data. Please try again.');
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <div className="user-form-container">
            <form onSubmit={handleSubmit} className="user-form">
                <h2>{userId ? 'Edit User' : 'Create User'}</h2>
                {errorMessage && <div className="error-message">{errorMessage}</div>}
                <input
                    type="text"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    placeholder="Username"
                    required
                />
                <input
                    type="text"
                    value={role}
                    onChange={(e) => setRole(e.target.value)}
                    placeholder="Role"
                    required
                />
                <input
                    type="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    placeholder="Password (optional)"
                />
                <button type="submit" disabled={isLoading}>
                    {isLoading ? 'Saving...' : (userId ? 'Update User' : 'Create User')}
                </button>
            </form>
        </div>
    );
};

export default UserForm;
