CREATE TABLE SHIPS(
	ShipID int NOT NULL PRIMARY KEY,
	ShipName varchar(255) NOT NULL,
	OwnerId int NOT NULL,
	RecordDATE DATE NOT NULL,
	RecordedPId int NOT NULL,
	TypeID int NOT NULL
);

CREATE TABLE OWNERS(
	OwnerID int UNIQUE NOT NULL,
	OwnerNAME varchar(255) NOT NULL,
	OwnerLNAME varchar(255) NOT NULL
);

CREATE TABLE HISTORY(
	RecID int NOT NULL,
	ShipId int NOT NULL,
	CurrentLoc varchar(255) NOT NULL,
	Destination varchar(255) NOT NULL,
	DepartDATE DATE NOT NULL,
	ArriveDATE DATE
);

CREATE TABLE PRESIDENTIALS(
	PID int UNIQUE,
	PNAME varchar(255) NOT NULL,
	SEAOCEANLAKE varchar(255) NOT NULL,
	City varchar(255) NOT NULL
);

CREATE TABLE TYPESS(
	TypeID int UNIQUE,
	TypeName varchar(255) NOT NULL,
	HullLEN float NOT NULL,
	Tonnage float NOT NULL
);

ALTER TABLE TYPESS ADD CONSTRAINT pkey
PRIMARY KEY (TypeID);
ALTER TABLE TYPESS ADD CONSTRAINT limitlen
CHECK (HullLEN < 300);

ALTER TABLE SHIPS ADD CONSTRAINT ownerid
FOREIGN KEY (OwnerID) REFERENCES OWNERS(OwnerID);
ALTER TABLE SHIPS ADD CONSTRAINT rpid
FOREIGN KEY (RecordedPId) REFERENCES PRESIDENTIALS(PID);
ALTER TABLE SHIPS ADD CONSTRAINT TypeID
FOREIGN KEY (TypeID) REFERENCES TYPESS(TypeID);

ALTER TABLE HISTORY ADD CONSTRAINT shipid
FOREIGN KEY (ShipId) REFERENCES SHIPS(ShipID) ON DELETE CASCADE;

ALTER TABLE OWNERS ADD CONSTRAINT prkey
PRIMARY KEY (OwnerID);

ALTER TABLE PRESIDENTIALS ADD CONSTRAINT ppkey
PRIMARY KEY (PID);

CREATE SEQUENCE seqtypess
INCREMENT BY 1
START WITH 1
MAXVALUE 300
MINVALUE 1
NO CYCLE;

CREATE SEQUENCE presseq
INCREMENT BY 1
START WITH 1
MAXVALUE 300
MINVALUE 1
NO CYCLE;

CREATE SEQUENCE shipseq
MINVALUE 1
MAXVALUE 300
INCREMENT BY 1;

CREATE SEQUENCE ownerseq
MINVALUE 1
MAXVALUE 300
INCREMENT BY 1;

CREATE SEQUENCE hisrecseq
MINVALUE 1
NO MAXVALUE
INCREMENT BY 1;

INSERT INTO OWNERS(OwnerID,OwnerNAME,OwnerLNAME)
VALUES (nextval('ownerseq'),('Ali'),('Tuncu'));
INSERT INTO OWNERS(OwnerID,OwnerNAME,OwnerLNAME)
VALUES (nextval('ownerseq'),('Orhan'),('Kandemir'));
INSERT INTO OWNERS(OwnerID,OwnerNAME,OwnerLNAME)
VALUES (nextval('ownerseq'),('David'),('Velt'));
INSERT INTO OWNERS(OwnerID,OwnerNAME,OwnerLNAME)
VALUES (nextval('ownerseq'),('Aslan'),('Akbulut'));
INSERT INTO OWNERS(OwnerID,OwnerNAME,OwnerLNAME)
VALUES (nextval('ownerseq'),('Sinem'),('Akpinar'));
INSERT INTO OWNERS(OwnerID,OwnerNAME,OwnerLNAME)
VALUES (nextval('ownerseq'),('Mike'),('Depp'));
INSERT INTO OWNERS(OwnerID,OwnerNAME,OwnerLNAME)
VALUES (nextval('ownerseq'),('Yilmaz'),('Canankatan'));
INSERT INTO OWNERS(OwnerID,OwnerNAME,OwnerLNAME)
VALUES (nextval('ownerseq'),('Muhammad'),('Mokaev'));
INSERT INTO OWNERS(OwnerID,OwnerNAME,OwnerLNAME)
VALUES (nextval('ownerseq'),('Yaren'),('Aksel'));
INSERT INTO OWNERS(OwnerID,OwnerNAME,OwnerLNAME)
VALUES (nextval('ownerseq'),('Sinan'),('Demir'));

INSERT INTO PRESIDENTIALS(PID,PNAME,SEAOCEANLAKE,City)
VALUES (nextval('presseq'),('Fethiye'),('Akdeniz'),('Antalya'));
INSERT INTO PRESIDENTIALS(PID,PNAME,SEAOCEANLAKE,City)
VALUES (nextval('presseq'),('Karacan'),('Akdeniz'),('Mersin'));
INSERT INTO PRESIDENTIALS(PID,PNAME,SEAOCEANLAKE,City)
VALUES (nextval('presseq'),('Canakkale'),('Ege'),('Canakkale'));
INSERT INTO PRESIDENTIALS(PID,PNAME,SEAOCEANLAKE,City)
VALUES (nextval('presseq'),('Finike'),('Karadeniz'),('Istanbul'));
INSERT INTO PRESIDENTIALS(PID,PNAME,SEAOCEANLAKE,City)
VALUES (nextval('presseq'),('Ayvalik'),('Ege'),('Izmir'));
INSERT INTO PRESIDENTIALS(PID,PNAME,SEAOCEANLAKE,City)
VALUES (nextval('presseq'),('Bartin'),('Karadeniz'),('Bartin'));
INSERT INTO PRESIDENTIALS(PID,PNAME,SEAOCEANLAKE,City)
VALUES (nextval('presseq'),('Haydarpasa'),('Marmara'),('Istanbul'));
INSERT INTO PRESIDENTIALS(PID,PNAME,SEAOCEANLAKE,City)
VALUES (nextval('presseq'),('Horpa'),('Ege'),('Aydin'));
INSERT INTO PRESIDENTIALS(PID,PNAME,SEAOCEANLAKE,City)
VALUES (nextval('presseq'),('Karakoy'),('Marmara'),('Istanbul'));
INSERT INTO PRESIDENTIALS(PID,PNAME,SEAOCEANLAKE,City)
VALUES (nextval('presseq'),('Ordu'),('Karadeniz'),('Ordu'));

INSERT INTO TYPESS(TypeID,TypeName,HullLEN,Tonnage)
VALUES (nextval('seqtypess'),('Handysize'),107,2050);
INSERT INTO TYPESS(TypeID,TypeName,HullLEN,Tonnage)
VALUES (nextval('seqtypess'),('Supramax'),150,5000);
INSERT INTO TYPESS(TypeID,TypeName,HullLEN,Tonnage)
VALUES (nextval('seqtypess'),('Capesize'),220,10000);
INSERT INTO TYPESS(TypeID,TypeName,HullLEN,Tonnage)
VALUES (nextval('seqtypess'),('VLOC'),200,8000);
INSERT INTO TYPESS(TypeID,TypeName,HullLEN,Tonnage)
VALUES (nextval('seqtypess'),('Aframax'),245,12000);
INSERT INTO TYPESS(TypeID,TypeName,HullLEN,Tonnage)
VALUES (nextval('seqtypess'),('VLCC'),299,20000);
INSERT INTO TYPESS(TypeID,TypeName,HullLEN,Tonnage)
VALUES (nextval('seqtypess'),('Handysize'),100,2000);
INSERT INTO TYPESS(TypeID,TypeName,HullLEN,Tonnage)
VALUES (nextval('seqtypess'),('Capesize'),230,11000);
INSERT INTO TYPESS(TypeID,TypeName,HullLEN,Tonnage)
VALUES (nextval('seqtypess'),('VLOC'),210,7500);
INSERT INTO TYPESS(TypeID,TypeName,HullLEN,Tonnage)
VALUES (nextval('seqtypess'),('Aframax'),235,10500);

INSERT INTO SHIPS(ShipID,ShipName,OwnerId,RecordDATE,RecordedPId,TypeID)
VALUES (nextval('shipseq'),('Turgut'),2,'2019-01-01',3,1);
INSERT INTO SHIPS(ShipID,ShipName,OwnerId,RecordDATE,RecordedPId,TypeID)
VALUES (nextval('shipseq'),('Kamlo'),2,'2019-01-01',3,1);
INSERT INTO SHIPS(ShipID,ShipName,OwnerId,RecordDATE,RecordedPId,TypeID)
VALUES (nextval('shipseq'),('Shirakami'),3,'2018-02-12',5,2);
INSERT INTO SHIPS(ShipID,ShipName,OwnerId,RecordDATE,RecordedPId,TypeID)
VALUES (nextval('shipseq'),('Taytanik'),1,'2019-05-04',1,3);
INSERT INTO SHIPS(ShipID,ShipName,OwnerId,RecordDATE,RecordedPId,TypeID)
VALUES (nextval('shipseq'),('Dadga'),4,'2017-06-11',2,4);
INSERT INTO SHIPS(ShipID,ShipName,OwnerId,RecordDATE,RecordedPId,TypeID)
VALUES (nextval('shipseq'),('Barbaros'),5,'2013-04-07',7,5);
INSERT INTO SHIPS(ShipID,ShipName,OwnerId,RecordDATE,RecordedPId,TypeID)
VALUES (nextval('shipseq'),('Canopus'),6,'2015-04-24',8,6);
INSERT INTO SHIPS(ShipID,ShipName,OwnerId,RecordDATE,RecordedPId,TypeID)
VALUES (nextval('shipseq'),('Bouvet'),8,'2017-02-24',4,7);
INSERT INTO SHIPS(ShipID,ShipName,OwnerId,RecordDATE,RecordedPId,TypeID)
VALUES (nextval('shipseq'),('Albion'),7,'2016-04-13',6,8);
INSERT INTO SHIPS(ShipID,ShipName,OwnerId,RecordDATE,RecordedPId,TypeID)
VALUES (nextval('shipseq'),('Saphir'),9,'2020-02-02',9,9);
INSERT INTO SHIPS(ShipID,ShipName,OwnerId,RecordDATE,RecordedPId,TypeID)
VALUES (nextval('shipseq'),('Goliat'),10,'2019-04-05',10,10);

INSERT INTO HISTORY(RecID,ShipId,CurrentLoc,Destination,DepartDATE,ArriveDATE)
VALUES (nextval('hisrecseq'),6,('Canakkale'),('Antalya'),'2014-02-05','2015-03-06');
INSERT INTO HISTORY(RecID,ShipId,CurrentLoc,Destination,DepartDATE,ArriveDATE)
VALUES (nextval('hisrecseq'),7,('Mersin'),('Antalya'),'2015-12-13','2016-01-02');
INSERT INTO HISTORY(RecID,ShipId,CurrentLoc,Destination,DepartDATE,ArriveDATE)
VALUES (nextval('hisrecseq'),9,('Istanbul'),('Aydin'),'2017-03-11','2017-12-12');
INSERT INTO HISTORY(RecID,ShipId,CurrentLoc,Destination,DepartDATE,ArriveDATE)
VALUES (nextval('hisrecseq'),8,('Istanbul'),('Ordu'),'2018-04-05','2018-04-16');
INSERT INTO HISTORY(RecID,ShipId,CurrentLoc,Destination,DepartDATE,ArriveDATE)
VALUES (nextval('hisrecseq'),5,('Bartin'),('Izmir'),'2019-04-07','2019-05-01');
INSERT INTO HISTORY(RecID,ShipId,CurrentLoc,Destination,DepartDATE,ArriveDATE)
VALUES (nextval('hisrecseq'),3,('Izmir'),('Mersin'),'2020-08-08','2020-08-19');
INSERT INTO HISTORY(RecID,ShipId,CurrentLoc,Destination,DepartDATE,ArriveDATE)
VALUES (nextval('hisrecseq'),2,('Ordu'),('Istanbul'),'2020-12-08',NULL);
INSERT INTO HISTORY(RecID,ShipId,CurrentLoc,Destination,DepartDATE,ArriveDATE)
VALUES (nextval('hisrecseq'),10,('Istanbul'),('Canakkale'),'2020-12-08','2020-12-09');
INSERT INTO HISTORY(RecID,ShipId,CurrentLoc,Destination,DepartDATE,ArriveDATE)
VALUES (nextval('hisrecseq'),11,('Aydin'),('Mersin'),'2020-11-29',NULL);
INSERT INTO HISTORY(RecID,ShipId,CurrentLoc,Destination,DepartDATE,ArriveDATE)
VALUES (nextval('hisrecseq'),1,('Antalya'),('Canakkale'),'2020-12-13',NULL);