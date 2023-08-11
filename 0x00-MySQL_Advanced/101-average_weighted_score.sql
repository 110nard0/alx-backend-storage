-- creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and store the average weighted score for all students
-- that computes and store the average weighted score for a student

DELIMITER $$
 CREATE PROCEDURE
        ComputeAverageWeightedScoreForUsers
  BEGIN
        DECLARE user_id INT;
        DECLARE total_score FLOAT;
        DECLARE total_weight INT;
        DECLARE user_avg FLOAT;

        DECLARE cur CURSOR
            FOR SELECT id FROM users;

           OPEN cur;

        read_loop: LOOP
          FETCH cur INTO user_id;
             IF user_id IS NULL THEN
          LEAVE read_loop;
            END IF;

                -- Calculate the average weighted score for the user
                SELECT SUM(c.score * p.weight), SUM(p.weight)
                  INTO total_score, total_weight
                  FROM corrections AS c
                  JOIN projects AS p
                    ON c.project_id = p.id
                 WHERE c.user_id = user_id;

                   SET user_avg = total_score / total_weight;

                -- Update user's average score
                UPDATE users
                   SET average_score = user_avg
                 WHERE id = user_id;

            END LOOP;
          CLOSE cur;
   END;
$$
DELIMITER ;
