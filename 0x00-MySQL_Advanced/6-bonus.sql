-- Write a SQL script that creates a stored procedure AddBonus
-- that adds a new correction for a student.

DELIMITER //

CREATE PROCEDURE AddBonus(
    IN user_id INTEGER,
    IN project_name VARCHAR(255),
    IN score INTEGER
)
BEGIN
    DECLARE project_id INT;

    -- Check if the project exists, if not, insert it
    SELECT id INTO project_id FROM projects WHERE name = project_name LIMIT 1;
    IF project_id IS NULL THEN
        INSERT INTO projects (name) VALUES (project_name);
        SET project_id = LAST_INSERT_ID();
    END IF;

    -- Insert the correction if project_id is found
    IF project_id IS NOT NULL THEN
        INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project_id, score);
    ELSE
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Project ID could not be determined for the new correction';
    END IF;
END

//

DELIMITER ;
