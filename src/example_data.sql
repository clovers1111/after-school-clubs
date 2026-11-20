-- Update this table as we create new tables and test data

DROP TABLE IF EXISTS Person;

CREATE TABLE IF NOT EXISTS Person(
    ID INT PRIMARY KEY AUTO_INCREMENT,
    firstName VARCHAR(20) NOT NULL,
    lastName VARCHAR(60) NOT NULL,
    address INT NOT NULL
);

INSERT INTO Person (firstName, lastName, address) VALUES ('first test', 'last test', 12);