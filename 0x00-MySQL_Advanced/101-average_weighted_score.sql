-- creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and store the average weighted score for all students

   DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER ||
 CREATE PROCEDURE
        ComputeAverageWeightedScoreForUsers()
  BEGIN
        DECLARE done INT DEFAULT FALSE;
        DECLARE user_id INT;
        DECLARE cur CURSOR
            FOR SELECT id FROM users;
        DECLARE CONTINUE HANDLER
            FOR NOT FOUND
            SET done = TRUE;

           OPEN cur;

           -- start loop and fetch id for each user
     read_loop: LOOP
                FETCH cur INTO user_id;
                   IF done THEN
                      LEAVE read_loop;
                  END IF;

                -- Calculate and update user's average weighted score
                UPDATE users AS u
                   SET average_score = (
                       SELECT SUM(c.score * p.weight) / SUM(p.weight)
                         FROM corrections AS c
                         JOIN projects AS p
                           ON c.project_id = p.id
                        WHERE c.user_id = user_id)
                 WHERE u.id = user_id;

            -- end loop and close cursor
            END LOOP;
          CLOSE cur;
   END||
DELIMITER ;
