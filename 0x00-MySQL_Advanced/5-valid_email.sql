-- creates a trigger that resets the valid_email attribute when email changes

DELIMITER //

CREATE TRIGGER reset_valid_email
BEFORE  UPDATE ON users
   FOR    EACH ROW
 BEGIN
            IF NEW.email <> OLD.email THEN
                IF OLD.valid_email = 0 THEN
                      SET NEW.valid_email = 1;
            ELSEIF OLD.valid_email = 1 THEN
                      SET NEW.valid_email = 0;
               END IF;
           END IF;
 END//

DELIMTER ;
