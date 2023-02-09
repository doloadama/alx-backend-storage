-- Creates a stored procedure ComputeAverageWeightedScoreForUsers that
-- computes and store the average weighted score for all students.

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
    ALTER TABLE users ADD weighted_score_sum INT NOT NULL;
    ALTER TABLE users ADD weight_sum INT NOT NULL;

    UPDATE users
        SET weighted_score_sum = (
            SELECT SUM(corrections.score * projects.weight)
            FROM corrections
                JOIN projects
                    ON corrections.project_id = projects.id
            WHERE corrections.user_id = users.id
            );

    UPDATE users
        SET weight_sum = (
            SELECT SUM(projects.weight)
                FROM corrections
                    JOIN projects
                        ON corrections.project_id = projects.id
                WHERE corrections.user_id = users.id
            );

    UPDATE users
        SET users.average_score = users.weighted_score_sum / users.weight_sum;
    ALTER TABLE users
        DROP COLUMN weighted_score_sum;
    ALTER TABLE users
        DROP COLUMN weight_sum;
END $$
DELIMITER ;