-- Computes and store the average weighted
-- score for a student.

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE average FLOAT;

    SET average := (
        SELECT SUM(c.score * p.weight) / SUM(p.weight)
        FROM corrections as c
        INNER JOIN projects as p
        ON c.project_id = p.id
        WHERE c.user_id = user_id
    );

    UPDATE users
    SET average_score = average
    WHERE id = user_id;
END $$
DELIMITER ;
