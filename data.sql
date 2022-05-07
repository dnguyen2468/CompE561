CREATE TABLE userIndex (
  UserID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  AddressID INT,
  Email VARCHAR(255),
  FirstName VARCHAR(255),
  LastName VARCHAR(255),
  PW VARCHAR(255),
  Phone VARCHAR(255)
);
INSERT INTO userIndex
  (AddressID,Email,FirstName,LastName,PW,Phone)
VALUES
  (1,'monty_fees2@yahoo.com','Kevin','Huth','aeX0Eeghie','(608) 261-7950'),
  (2,'myra2009@hotmail.com','Elizabeth ','Travis','aim5Eiroo','(732) 207-4440'),
  (2,'madonna2012@hotmail.com','James ','Mooney','eita5Eocho','(732) 221-4251'),
  (3,'corene.hill8@gmail.com','Eric','Salley','weih7Ied6','(503) 975-0648'),
  (4,'gene1990@yahoo.com','Christin','Beckman','aiXeuS2chooM','(845) 750-3038');

CREATE TABLE billing (  
  BillingID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  OrderID INT,
  UserID INT,
  AddressID INT,
  NameFull VARCHAR(255),
  CardNum VARCHAR(255),
  ExpDate VARCHAR(255),
  CVV INT
);
INSERT INTO billing
  (OrderID,UserID,AddressID,NameFull,CardNum,ExpDate,CVV)
VALUES
  (1,1,1,'Kevin Huth','5212 0917 3304 9640','03/2020',996),
  (2,3,2,'James Mooney','4532 1639 9934 6690','10/2020',852),
  (3,2,2,'Elizabeth Travis','5191 3381 9182 0150','12/2023',326),
  (4,5,4,'Christin Beckman','4929 0847 7505 6553','07/2020',213);

CREATE TABLE userprofile ( 
  ProfileID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  UserID INT,
  BillingID VARCHAR(255),
  OrderID VARCHAR(255)
);
INSERT INTO userprofile
  (UserID,BillingID,OrderID)
VALUES
  (1,'1','1'),
  (2,'3','3'),
  (3,'2','2'),
  (4,NULL,NULL),
  (5,'4','4');
  
  CREATE TABLE address (
  AddressID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  Street VARCHAR(255),
  City VARCHAR(255),
  State VARCHAR(255),
  Country VARCHAR(255),
  Zipcode INT
);
INSERT INTO address
  (AddressID,Street,City,State,Country,Zipcode)
VALUES
  (1,'1815 Hudson Street','Wayne','New Jersey','USA',70477),
  (2,'3774 Arbor Court','Cheyenne','Wyoming','USA',82003),
  (3,'2780 Gateway Road','Garibaldi','Oregon','USA',97118),
  (4,'3644 Ward Road','Rye','New York','USA',10580);

CREATE TABLE userorder ( 
  OrderID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  ProductID INT,
  UserID INT,
  UPSLink VARCHAR(255)
);
INSERT INTO userorder
  (ProductID,UserID,UPSLink)
VALUES
  (3,1,'Order Processing'),
  (5,3,'Order Processing'),
  (6,2,'Order Processing'),
  (2,5,'Order Processing');
  
CREATE TABLE product ( 
  ProductID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  PName VARCHAR(255),
  PPrice FLOAT,
  PDescription VARCHAR(255),
  POwner VARCHAR(255),
  ImageLink VARCHAR(511),
  ArtType VARCHAR(255)
);
INSERT INTO product
  (PName,PPrice,PDescription,POwner,ImageLink,ArtType)
VALUES
  ('Eight, Lucky Number',5000.00,'Number 8 carries fortunate energy. In Feng Shui 8 is associated with wealth, success, and status.','Zaira Dzhaubaeva','https://i.etsystatic.com/21340843/r/il/18a76e/3632669674/il_1140xN.3632669674_trlp.jpg','P'),
  ('Ragnarok',633.77,'The magnificent battles and powerful characters of ancient Norse sagas come to life in this special Viking collection.','Oleg Peresvet','https://i.etsystatic.com/10239706/r/il/d16562/2394884149/il_1140xN.2394884149_220k.jpg','W'),
  ('Creature',5000.00,'This was created by the artist when her father died and her daughter was born. Inspired by life-changing events, she wanted to create a form made out of a primordial state.','Tomoko Konno','https://www.moonxmoon.com/wp/wp-content/uploads/2021/07/227409117_848754286043327_1711463090970714511_n.jpg','C'),
  ('American Indian',1000.00,'Sealed inside a solid oak wood frame, this genuine leather portrait shows an American Indian, a Bald Eagle, and a bison.','Jason Youngbuck','https://www.google.com/imgres?imgurl=https%3A%2F%2Fthumbs.worthpoint.com%2Fzoom%2Fimages1%2F1%2F0916%2F29%2Fjason-youngbuck-native-american_1_7651f88e02f796c5cbb92d3564fddd61.jpg&imgrefurl=https%3A%2F%2Fwww.worthpoint.com%2Fworthopedia%2Fjason-youngbuck-native-american-1832240154&tbnid=FyiDmcYCcwEgsM&vet=12ahUKEwjtu7bIyqb3AhVoCjQIHUhCDVIQMygMegUIARCOAw..i&docid=YC9PyH9Hfn0v3M&w=810&h=1080&q=framed%20leather%20portrait%20art&ved=2ahUKEwjtu7bIyqb3AhVoCjQIHUhCDVIQMygMegUIARCOAw','L'),
  ('Global Harmony',1000.00,'The artist intended on having this piece represent the global oneness that is shared between everyone universally. This piece would stand out in a garden, industrial, or residential setting.','Bartley Berry','https://i.etsystatic.com/34949270/r/il/c843bd/3809781770/il_1588xN.3809781770_7ejs.jpg','M'),
  ('Coral Reef',5400.00,'His sculptures capture the vivid coloration and sleek beauty of fish, coral and other sea creatures and would be a welcome addition to our houses. While these sculptures may not fit everyone’s aesthetic, you have to admit these are incredible art pieces.','Joe Peters','https://i.pinimg.com/originals/54/c9/8d/54c98d4eef128b7e5dbaeb9a482ca118.jpg','G');
