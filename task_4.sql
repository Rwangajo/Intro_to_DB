-- Script to print the full description of the 'books' table.
-- The database name (e.g., alx_book_store) will be passed as an argument to the mysql command.
-- This script avoids using DESCRIBE or EXPLAIN statements.

SELECT
    COLUMN_NAME,
    COLUMN_TYPE,
    IS_NULLABLE,
    COLUMN_KEY,
    COLUMN_DEFAULT,
    EXTRA
FROM
    INFORMATION_SCHEMA.COLUMNS
WHERE
    TABLE_SCHEMA = DATABASE() AND TABLE_NAME = 'books';
