-- creates a stored procedure ComputeAverageScoreForUser
-- that computes and stores the average score for a student

DELIMITER $$
 CREATE PROCEDURE
        ComputeAverageScoreForUser(IN user_id INT)
  BEGIN
        DECLARE user_avg FLOAT;

                -- Calculate the average score for the user
                SELECT AVG(score) INTO user_avg
                  FROM corrections
                 WHERE user_id = corrections.user_id;
 
         -- Update the average score for the user
         UPDATE users
            SET average_score = user_avg
          WHERE id = user_id;
   END;
$$
DELIMITER ;
