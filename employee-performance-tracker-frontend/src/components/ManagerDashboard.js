// src/components/ManagerDashboard.js
import React, { useEffect, useState } from 'react';
import axiosInstance from '../api/axios'; // Using the axios instance
import UserForm from './UserForm'; // Import the UserForm component for adding users
import '../styles/ManagerDashboard.css'; // Importing styles

const ManagerDashboard = () => {
    const [services, setServices] = useState([]);
    const [isFormVisible, setIsFormVisible] = useState(false); // State to toggle user form visibility
    const [errorMessage, setErrorMessage] = useState('');
    const [isLoading, setIsLoading] = useState(true);

    useEffect(() => {
        const fetchServices = async () => {
            try {
                const serviceResponse = await axiosInstance.get('/services/');
                setServices(serviceResponse.data);
            } catch (error) {
                setErrorMessage('Failed to load services. Please try again.');
                console.error(error);
            } finally {
                setIsLoading(false);
            }
        };

        fetchServices();
    }, []);

    const handleToggleForm = () => {
        setIsFormVisible(!isFormVisible); // Toggle the visibility of the UserForm
    };

    if (isLoading) {
        return <div className="dashboard-loading">Loading...</div>;
    }

    if (errorMessage) {
        return <div className="dashboard-error">{errorMessage}</div>;
    }

    return (
        <div className="manager-dashboard-container">
            <h2>Manager Dashboard</h2>

            <div className="manager-dashboard-section">
                <h3>Managed Services</h3>
                <ul>
                    {services.map((service) => (
                        <li key={service.id}>
                            {service.name} (Managed by: {service.manager.username})
                        </li>
                    ))}
                </ul>
            </div>

            {/* Toggle UserForm component when Add User button is clicked */}
            <button onClick={handleToggleForm} className="add-user-button">
                {isFormVisible ? 'Cancel' : 'Add User'}
            </button>

            {/* Display UserForm if isFormVisible is true */}
            {isFormVisible && <UserForm />}
        </div>
    );
};

export default ManagerDashboard;
