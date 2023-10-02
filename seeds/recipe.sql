/*

USER STORIES 

As a food lover,
So I can stay organised and decide what to cook,
I'd like to keep a list of all my recipes with their names.

As a food lover,
So I can stay organised and decide what to cook,
I'd like to keep the average cooking time (in minutes) for each recipe.

As a food lover,
So I can stay organised and decide what to cook,
I'd like to give a rating to each of the recipes (from 1 to 5).


NOUNS - recipe, name, cooking time, rating

DESIGN

recipe
id | name | cooking_time | rating

*/

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS recipes;
DROP SEQUENCE IF EXISTS recipes_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS recipes_id_seq;
CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    cooking_time INTEGER,
    rating INTEGER
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO recipes (name, cooking_time, rating) VALUES ('Pizza', 30, 5);
INSERT INTO recipes (name, cooking_time, rating) VALUES ('Cheesecake', 60, 4);
INSERT INTO recipes (name, cooking_time, rating) VALUES ('Lasagna', 45, 3);
INSERT INTO recipes (name, cooking_time, rating) VALUES ('Pasta', 20, 2);
INSERT INTO recipes (name, cooking_time, rating) VALUES ('Burger', 15, 3);