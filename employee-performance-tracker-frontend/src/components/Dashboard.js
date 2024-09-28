// src/components/Dashboard.js
import React, { useEffect, useState } from 'react';
import axiosInstance from '../api/axios'; // Using the axios instance
import '../styles/Dashboard.css'; // Importing styles

const Dashboard = () => {
    const [users, setUsers] = useState([]);
    const [services, setServices] = useState([]);
    const [goals, setGoals] = useState([]);
    const [errorMessage, setErrorMessage] = useState('');
    const [isLoading, setIsLoading] = useState(true);

    useEffect(() => {
        const fetchData = async () => {
            try {
                // Fetching data from the API using axiosInstance
                const userResponse = await axiosInstance.get('/users/');
                setUsers(userResponse.data);

                const serviceResponse = await axiosInstance.get('/services/');
                setServices(serviceResponse.data);

                const goalResponse = await axiosInstance.get('/goals/');
                setGoals(goalResponse.data);
            } catch (error) {
                setErrorMessage('Failed to load data. Please try again.');
                console.error(error);
            } finally {
                setIsLoading(false);
            }
        };

        fetchData();
    }, []);

    if (isLoading) {
        return <div className="dashboard-loading">Loading...</div>;
    }

    if (errorMessage) {
        return <div className="dashboard-error">{errorMessage}</div>;
    }

    return (
        <div className="dashboard-container">
            <h2>Dashboard</h2>

            <div className="dashboard-section">
                <h3>Users</h3>
                <ul>
                    {users.map((user) => (
                        <li key={user.id}>
                            {user.username} ({user.role})
                        </li>
                    ))}
                </ul>
            </div>

            <div className="dashboard-section">
                <h3>Services</h3>
                <ul>
                    {services.map((service) => (
                        <li key={service.id}>
                            {service.name} (Managed by: {service.manager.username})
                        </li>
                    ))}
                </ul>
            </div>

            <div className="dashboard-section">
                <h3>Goals</h3>
                <ul>
                    {goals.map((goal) => (
                        <li key={goal.id}>
                            {goal.description} - {goal.status} (Assigned to: {goal.employee.username})
                        </li>
                    ))}
                </ul>
            </div>
        </div>
    );
};

export default Dashboard;
