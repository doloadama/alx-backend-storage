-- 6. Add bonus
-- t adds a new correction for a student
DELIMITER $$
CREATE PROCEDURE addBonus(
    IN user_id INT,
    IN project_name VARCHAR(255),
    IN score FLOAT)
BEGIN
    DECLARE project_id INT;
    IF (SELECT COUNT(*) FROM projects WHERE name = project_name) = 0 
    THEN
        INSERT INTO projectS (name) VALUES (project_name);
    END IF;
    SET project_id = (SELECT id FROM projects WHERE name = project_name LIMIT 1);
    INSERT INTO corrections (user_id, project_id, score) VALUES (project_id, user_id, score);
END;
$$
DELIMITER ;