-- 1. In and not out
-- Create a table users
CREATE TABLE IF NOT EXIST users (
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM ('US', 'CO', 'TN') NOT NULL,
    PRIMARY KEY (id)
);