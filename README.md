
# Employee Performance Tracker

**A comprehensive solution for tracking and evaluating employee performance within the Well Performance service.**

## Architecture

### 1. Frontend (React.js)

#### User Interface (UI)

- **Forms for Goal Setting:**
  - **Description**: Forms where employees can enter their goals, including descriptions and target dates.
  - **Components**: Input fields for goal description, target date, and status (e.g., not started, in progress, completed).
  - **Validation**: Ensures that input data is complete and formatted correctly.

- **Dashboards for Performance Tracking:**
  - **Description**: Displays a summary of goals and performance metrics.
  - **Components**: Graphs and charts showing progress towards goals, performance statistics, and a list of goals with their statuses.
  - **Features**: Interactive elements like filters and sorting options to view specific data or time periods.

#### Interaction

- **User Actions:**
  - **Input Data**: Users enter or update information in forms (e.g., new goals, performance updates).
  - **View Information**: Users can view their goals, performance metrics, and reports through the dashboard.

- **State Management:**
  - **Local State**: Manages temporary UI state within components (e.g., form inputs).
  - **Global State**: Uses context or state management libraries (e.g., Redux) to handle data shared across components (e.g., user profile, goal lists).

- **API Calls:**
  - **HTTP Requests:**
    - **GET Requests**: Fetch data from backend API endpoints. For example, retrieving the list of goals or performance metrics.
    - **POST Requests**: Send data to the backend. For example, submitting a new goal or updating performance metrics.

  - **Endpoints:**
    - `/api/goals`: To manage goals.
    - `/api/performance`: To manage performance updates.
    - `/api/users`: To manage user information.
    - `/api/login`: For user authentication.

### 2. Backend (Django)

#### API Endpoints

- **Handling Requests:**
  - **GET Requests**: Process requests to retrieve data. For example, fetching goals or performance metrics based on query parameters.
  - **POST Requests**: Handle requests to create or update data. For example, submitting a new goal or performance update.

- **API Routing:**
  - **URLs and Views**: Django routes incoming requests to appropriate views based on URL patterns (e.g., `/api/goals` maps to a view function that processes goal-related requests).
  - **Serializers**: Convert data between Django models and JSON format for API responses.

#### Application Logic

- **Business Logic:**
  - **Data Processing**: Validates and processes incoming data (e.g., goal creation, performance updates).
  - **Metrics Calculation**: Computes performance metrics and progress based on the data.

- **Error Handling:**
  - **Validation Errors**: Returns appropriate error messages if data is invalid.
  - **Server Errors**: Handles unexpected issues and returns error responses.

### 3. Database (PostgreSQL or MySQL)

#### Data Storage

- **Tables:**
  - `Users`: Stores user information (e.g., user_id, name, email, role).
  - `Goals`: Stores goal details (e.g., goal_id, description, target_date, status, employee_id).
  - `Performance`: Stores performance updates (e.g., performance_id, update_date, performance_update, employee_id, goal_id).
  - `Services`: Stores service information if applicable.

#### Queries

- **Data Retrieval:**
  - **Select Queries**: Retrieve data from the database based on criteria (e.g., goals for a specific employee).
  - **Aggregation Queries**: Compute metrics or summaries (e.g., average performance score).

- **Data Manipulation:**
  - **Insert Queries**: Add new records (e.g., a new goal or performance update).
  - **Update Queries**: Modify existing records (e.g., updating the status of a goal).
  - **Delete Queries**: Remove records if needed.

## Data Flow

1. **Frontend to Backend:**
   - **Request Creation**: When a user interacts with the UI (e.g., submitting a form), the frontend sends an HTTP request to a specific API endpoint.
   - **Data Transmission**: Includes request data in the body or query parameters, depending on the request type (e.g., GET, POST).

2. **Backend to Database:**
   - **Query Execution**: The backend processes incoming requests and interacts with the database to retrieve or update data.
   - **Data Handling**: Uses Django’s ORM to perform operations on the database.

3. **Database to Backend:**
   - **Data Retrieval**: The database returns the requested data to the backend.
   - **Processing**: The backend processes the data (e.g., calculates metrics, formats responses).

4. **Backend to Frontend:**
   - **Response Creation**: The backend sends a response back to the frontend, which includes data or status information.
   - **UI Update**: The frontend updates the user interface based on the received data (e.g., displaying updated goals, performance metrics).

## APIs and Methods

### API Routes:

- **/api/goals**
  - **GET**:
    - **Description**: Retrieves a list of goals set by a specific employee or for a specific service.
    - **Response**: JSON array of goals, including goal details such as description, target date, and status.
  - **POST**:
    - **Description**: Creates a new goal for an employee or service.
    - **Response**: JSON object with the created goal’s details.

- **/api/performance**
  - **GET**:
    - **Description**: Retrieves performance metrics for a specific employee or service.
    - **Response**: JSON object with performance metrics.
  - **POST**:
    - **Description**: Submits a performance update for an employee.
    - **Response**: JSON object with the updated performance data.

## Data Model

### Data Model Overview

#### Entities:

- **User**:
  - `user_id` (Primary Key)
  - `name`
  - `email`
  - `role` (e.g., employee, manager, director)
  - `password_hash` (for authentication)

- **Goal**:
  - `goal_id` (Primary Key)
  - `description`
  - `target_date`
  - `status` (e.g., not started, in progress, completed)
  - `employee_id` (Foreign Key referencing User)
  - `service_id` (Foreign Key referencing Service)

- **Performance**:
  - `performance_id` (Primary Key)
  - `update_date`
  - `performance_update`
  - `employee_id` (Foreign Key referencing User)
  - `goal_id` (Foreign Key referencing Goal)

#### Relationships:

- **User (1) --- (M) Goal**: An employee can have multiple goals.
- **Goal (M) --- (1) Service**: A goal is associated with a specific service.
- **User (1) --- (M) Performance**: An employee can have multiple performance updates.
- **Performance (M) --- (1) Goal**: A performance update is related to a specific goal.

## User Stories

- **User Story 1: Goal Creation**:
  - Employees can enter a goal description, set a target date, and select a status.
- **User Story 2: Manager Dashboard**:
  - Managers can view the goals and performance of employees under their supervision.
- **User Story 3: Performance Update Submission**:
  - Employees can submit performance updates.
- **User Story 4: Goal Status Tracking**:
  - Employees can track the status of their goals.
- **User Story 5: Executive Overview**:
  - Executives can view service-wide performance metrics.

## Mockups

- **Login Page**: Fields for username, password, and login button.
- **Employee Dashboard**: Summary of goals, progress bars, and performance updates.
- **Manager Dashboard**: List of employees and performance tracking.
- **Executive Overview**: Aggregated performance metrics and charts.

## Conclusion

The Employee Performance Tracker provides an intuitive platform for tracking and evaluating employee performance within the Well Performance service, ensuring a seamless and efficient user experience.
