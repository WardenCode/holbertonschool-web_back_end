-- Creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and store the average weighted score for
-- all students.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;

DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    UPDATE users
    SET average_score = (
        SELECT SUM(p.weight * c.score) / SUM(p.weight)
        FROM corrections AS c
	RIGHT JOIN projects AS p
        ON c.project_id = p.id
	WHERE c.user_id = users.id
    );
END $$

DELIMITER ;
