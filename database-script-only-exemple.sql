-- Create table for Django's built-in User model
CREATE TABLE auth_user (
    id SERIAL PRIMARY KEY,
    password VARCHAR(128) NOT NULL,
    last_login TIMESTAMP WITH TIME ZONE,
    is_superuser BOOLEAN NOT NULL,
    username VARCHAR(150) NOT NULL UNIQUE,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    email VARCHAR(254) NOT NULL UNIQUE,
    is_staff BOOLEAN NOT NULL,
    is_active BOOLEAN NOT NULL,
    date_joined TIMESTAMP WITH TIME ZONE NOT NULL
);

-- Create table for Nutritionist model
CREATE TABLE nutritionist (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL UNIQUE,
    phone VARCHAR(15) NOT NULL,
    registration_number VARCHAR(20) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES auth_user (id) ON DELETE CASCADE
);

-- Create table for UserProfile model
CREATE TABLE user_profile (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL UNIQUE,
    phone VARCHAR(15) NOT NULL,
    nutritionist_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES auth_user (id) ON DELETE CASCADE,
    FOREIGN KEY (nutritionist_id) REFERENCES nutritionist (id) ON DELETE SET NULL
);
