cmmand = """CREATE TABLE favourites (
    id SERIAL PRIMARY KEY,
    user_id VARCHAR(255),
    cityname VARCHAR(255),
    state VARCHAR(255),
    country VARCHAR(255),
    longitude DECIMAL(9,6),
    latitude DECIMAL(9,6)
);"""