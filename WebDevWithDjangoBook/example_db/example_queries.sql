-- SQL query examples
-- CREATE
DROP TABLE IF EXISTS book;
CREATE TABLE "book" (
     "title" TEXT
    ,"publisher" TEXT
    ,"author" TEXT
);

INSERT INTO book (
     title
    ,publisher
    ,author
)
VALUES (
     'The Sparrow Warrior'
    ,'Super Hero Publications'
    ,'Patric Javagal'
    )
    ,(
     'Ninja Warrior'
    ,'East Hill Publications'
    ,'Edward Smith'
    )
    ,(
     'The European History'
    ,'Northside Publications'
    ,'Eric Robbins'
    );

-- READ
SELECT
     title
    ,publisher
    ,author
FROM book;

SELECT *
FROM book;

SELECT
    author
FROM book
WHERE title = 'The Sparrow Warrior';

-- UPDATE
UPDATE book
SET publisher = 'Northside Publications'
where title = 'The Sparrow Warrior';

SELECT *
FROM book;

-- DELETE
DELETE FROM book
WHERE title = 'The Sparrow Warrior';

SELECT *
FROM book;
