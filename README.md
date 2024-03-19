### README.md

This code implements a Flask API for managing user favorites of locations. It includes endpoints for adding a favorite location, retrieving favorites by user ID, and deleting a favorite by user ID, city name, and state. The code utilizes SQLAlchemy for database interactions and dotenv for environment variable configuration.

#### Setup

1. Ensure you have Python installed.
2. Ensure that the current device has the correct security group rules to access the database
3. Install the required packages.
4. Create a `.env` file with the following format:
   ```
   URI=your_database_uri_here
   ```
5. Run the Flask application using `python orm.py`.

#### Endpoints

1. **POST /favourites**: Add a favorite location with user ID, city name, state, country, longitude, and latitude.
2. **GET /favourites**: Retrieve favorites by user ID.
3. **DELETE /deletecity**: Delete a favorite by user ID, city name, and state.

#### Error Handling

- If a favorite is not found, a 404 error is returned.
- If there are missing parameters or a server error occurs, appropriate error responses are provided.
