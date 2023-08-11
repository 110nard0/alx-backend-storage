-- creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for a student

DELIMITER $$
 CREATE PROCEDURE
        ComputeAverageWeightedScoreForUser(IN user_id INT)
  BEGIN
        DECLARE total_score FLOAT;
        DECLARE total_weight INT;
        DECLARE user_avg FLOAT;

                -- Calculate the average weighted score for the user
                SELECT SUM(c.score * p.weight), SUM(p.weight)
                  INTO total_score, total_weight
                  FROM corrections AS c
                  JOIN projects AS p
                    ON c.project_id = p.id
                 WHERE c.user_id = user_id;

                   SET user_avg = total_score / total_weight;

                UPDATE users
                   SET average_score = user_avg
                 WHERE id = user_id;
   END;
$$
DELIMITER ;
