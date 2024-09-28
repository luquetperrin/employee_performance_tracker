import requests
import pandas as pd

# Define the API endpoint
api_url = 'http://127.0.0.1:8000/api/users/'

# Make a GET request to the API
response = requests.get(api_url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    users = response.json()
    
    # Create a DataFrame from the user data
    df = pd.DataFrame(users)
    
    # Display the DataFrame as a table
    print(df.to_string(index=False))
else:
    print(f"Failed to retrieve users. Status code: {response.status_code}")
