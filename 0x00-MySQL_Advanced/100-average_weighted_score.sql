DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN p_user_id INT)
BEGIN
  DECLARE v_weight INT DEFAULT 0;
  DECLARE v_score INT DEFAULT 0;
  DECLARE v_average INT DEFAULT 0;

  SELECT SUM(weight) INTO v_weight
  FROM corrections c
  JOIN projects p ON c.project_id = p.id
  WHERE c.user_id = p_user_id;

  SELECT SUM(score * weight) INTO v_score
  FROM corrections c
  JOIN projects p ON c.project_id = p.id
  WHERE c.user_id = p_user_id;

  SET v_average = v_score / v_weight;

  UPDATE users
  SET average_score = v_average
  WHERE id = p_user_id;
END$$

DELIMITER ;
