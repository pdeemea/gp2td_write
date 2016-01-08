CREATE WRITABLE EXTERNAL WEB TABLE
test_out3 (id integer, notes text)
EXECUTE '<path_to_the_file>'
FORMAT 'TEXT' (DELIMITER ',');
