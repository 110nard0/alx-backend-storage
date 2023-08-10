-- creates a trigger that resets the valid_email attribute when email changes

-- Create the trigger
DELIMITER //

CREATE TRIGGER update_valid_email
BEFORE  UPDATE ON users
   FOR    EACH ROW
 BEGIN
            IF NEW.email <> OLD.email THEN
               SET NEW.valid_email = 0;
           END IF;
  END;
//

DELIMITER ;
