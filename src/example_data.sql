-- Update this table as we create new tables and test data
DROP TABLE IF EXISTS Event;
DROP TABLE IF EXISTS Advisor;
DROP TABLE IF EXISTS Membership;
DROP TABLE IF EXISTS Club;
DROP TABLE IF EXISTS Student;
DROP TABLE IF EXISTS Faculty;
DROP TABLE IF EXISTS Person;
DROP TABLE IF EXISTS Location;


CREATE TABLE Location (
    ID       INT          PRIMARY KEY AUTO_INCREMENT,
    location VARCHAR(100) NOT NULL,
    roomNum  VARCHAR(10) NOT NULL, -- Needs to be not null to enforce uniqueness
    CONSTRAINT room_and_location UNIQUE (location, roomNum)
);

CREATE TABLE IF NOT EXISTS Person(
    ID        INT         PRIMARY KEY AUTO_INCREMENT,
    firstName VARCHAR(20) NOT NULL,
    lastName  VARCHAR(60) NOT NULL,
    address   INT,
    FOREIGN KEY (address) REFERENCES Location(ID)
    ON DELETE SET NULL
    ON UPDATE CASCADE
);

CREATE TABLE Faculty(
    ID         INT PRIMARY KEY,
    department VARCHAR(50) NOT NULL,
    FOREIGN KEY (ID) REFERENCES Person(ID)
    ON DELETE CASCADE
);

CREATE TABLE Student (
    ID    INT     PRIMARY KEY,
    grade TINYINT NOT NULL,
    FOREIGN KEY (ID) REFERENCES Person(ID)
    ON DELETE CASCADE
);

CREATE TABLE Club(
    clubName       VARCHAR(60) PRIMARY KEY
);

CREATE TABLE Membership(
    studentID INT         NOT NULL,
    clubName  VARCHAR(60) NOT NULL,
    startDate DATE        NOT NULL,
    endDate   DATE        NOT NULL,
    PRIMARY KEY (studentID, clubName, startDate, endDate),
    FOREIGN KEY (studentID) REFERENCES Student(ID),
    FOREIGN KEY (clubName)  REFERENCES Club(clubName)
);

CREATE TABLE Advisor(
    facultyID INT         NOT NULL,
    clubName  VARCHAR(60) NOT NULL,
    startDate DATE        NOT NULL,
    endDate   DATE        NOT NULL,
    PRIMARY KEY (facultyID, clubName, startDate, endDate),
    FOREIGN KEY (facultyID) REFERENCES Faculty(ID),
    FOREIGN KEY (clubName)  REFERENCES Club(clubName)
);

CREATE TABLE Event(
    clubName    VARCHAR(60) NOT NULL,
    startTime   DATETIME    NOT NULL,
    endTime     DATETIME    NOT NULL,
    eventType   VARCHAR(30) NOT NULL,
    description VARCHAR(50),
    locationID  INT         NOT NULL,
    PRIMARY KEY (clubName, startTime),
    FOREIGN KEY (clubName)   REFERENCES Club(clubName),
    FOREIGN KEY (locationID) REFERENCES Location(ID)
);