-- creates user
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- grant access
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
