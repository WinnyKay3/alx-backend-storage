-- Average score

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(
    IN _user_id INT
)
BEGIN
    UPDATE users
    SET average_score = (
        SELECT AVG(score) 
        FROM corrections
        WHERE corrections.user_id = _user_id
    )
    WHERE id = _user_id;
END //
DELIMITER ;
