-- The script updates the score of Bob to 10 in the table second_table
DELETE FROM second_table WHERE score <= 5 ORDER BY score DESC
