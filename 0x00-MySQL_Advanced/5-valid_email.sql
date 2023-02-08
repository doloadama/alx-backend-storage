-- 5. Email validation to sent
-- a SQL script that creates a
-- trigger that resets the attribute
-- valid_email only when the email
-- has been changed.
DELIMITER $$
CREATE trigger decrease_item
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    IF OLD.email != NEW.email THEN
        SET NEW.email = 0;
    END IF;
END $$
DELIMITER ;