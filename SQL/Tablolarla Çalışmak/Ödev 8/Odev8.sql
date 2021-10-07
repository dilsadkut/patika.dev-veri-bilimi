
-- Ödev 8

/*
Merhabalar,



1.test veritabanınızda employee isimli sütun bilgileri id(INTEGER), name VARCHAR(50), birthday DATE, email VARCHAR(100) olan bir tablo oluşturalım.
2.Oluşturduğumuz employee tablosuna 'Mockaroo' servisini kullanarak 50 adet veri ekleyelim.
3.Sütunların her birine göre diğer sütunları güncelleyecek 5 adet UPDATE işlemi yapalım.
4.Sütunların her birine göre ilgili satırı silecek 5 adet DELETE işlemi yapalım.


Kolay Gelsin.
*/

CREATE TABLE employee (
  id SERIAL PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  birthday DATE,
  email VARCHAR(100)
  );
  
SELECT * 
FROM employee;

insert into employee (name, birthday, email) values ('Madelene', '2020-10-20', 'mmckearnen0@joomla.org');
insert into employee (name, birthday, email) values ('Dela', null, 'dgabby1@phoca.cz');
insert into employee (name, birthday, email) values ('Rustin', '2021-06-10', 'rfilippozzi2@amazon.co.uk');
insert into employee (name, birthday, email) values ('Wyndham', '2021-06-18', 'wtomsen3@xinhuanet.com');
insert into employee (name, birthday, email) values ('Arda', '2021-10-01', 'abuggs4@amazon.com');
insert into employee (name, birthday, email) values ('Lynnette', '2021-07-31', 'lheine5@globo.com');
insert into employee (name, birthday, email) values ('Lionello', null, 'ltolson6@newyorker.com');
insert into employee (name, birthday, email) values ('Laurens', '2021-05-29', 'lpillman7@cmu.edu');
insert into employee (name, birthday, email) values ('Minna', '2021-07-31', 'mbarbrick8@ucoz.com');
insert into employee (name, birthday, email) values ('Arther', '2021-05-23', 'acarillo9@so-net.ne.jp');
insert into employee (name, birthday, email) values ('Dugald', '2021-04-09', 'ddurninga@youku.com');
insert into employee (name, birthday, email) values ('Chadd', null, 'clyenyngb@opensource.org');
insert into employee (name, birthday, email) values ('Eirena', '2021-09-22', 'emckeanc@myspace.com');
insert into employee (name, birthday, email) values ('Siobhan', '2021-04-25', 'sgrassid@google.co.uk');
insert into employee (name, birthday, email) values ('Kristoffer', '2021-02-20', 'kabadame@omniture.com');
insert into employee (name, birthday, email) values ('Ronald', '2021-04-04', 'ramayaf@mit.edu');
insert into employee (name, birthday, email) values ('Cheston', '2021-05-02', 'cmatfieldg@reuters.com');
insert into employee (name, birthday, email) values ('Zaccaria', '2021-08-03', 'zcorballish@nymag.com');
insert into employee (name, birthday, email) values ('Nestor', '2020-12-21', 'nmcgrearyi@dailymotion.com');
insert into employee (name, birthday, email) values ('Athene', '2021-03-04', 'achipchasej@uiuc.edu');
insert into employee (name, birthday, email) values ('Rochette', '2021-08-09', 'rwentk@economist.com');
insert into employee (name, birthday, email) values ('Nance', '2021-05-04', 'nmccaffreyl@hatena.ne.jp');
insert into employee (name, birthday, email) values ('Neilla', '2021-05-22', 'nharpm@buzzfeed.com');
insert into employee (name, birthday, email) values ('Rae', '2021-02-19', 'rlillegardn@foxnews.com');
insert into employee (name, birthday, email) values ('Merla', '2021-04-18', 'msurro@ocn.ne.jp');
insert into employee (name, birthday, email) values ('Antonio', '2021-03-08', 'aaddersonp@auda.org.au');
insert into employee (name, birthday, email) values ('Antonetta', '2021-05-01', 'apinckedq@goo.gl');
insert into employee (name, birthday, email) values ('Rebbecca', '2021-05-20', 'rbartar@unicef.org');
insert into employee (name, birthday, email) values ('Laurence', '2021-06-04', 'lbelzs@cdbaby.com');
insert into employee (name, birthday, email) values ('Minetta', '2021-02-19', 'mfruchtert@buzzfeed.com');
insert into employee (name, birthday, email) values ('Marianne', '2021-09-14', 'mkelshawu@netlog.com');
insert into employee (name, birthday, email) values ('Son', '2021-08-02', 'svoyseyv@ca.gov');
insert into employee (name, birthday, email) values ('Meriel', '2020-11-24', 'mmingayew@smugmug.com');
insert into employee (name, birthday, email) values ('Lanita', '2021-03-23', 'lmccartx@icq.com');
insert into employee (name, birthday, email) values ('Berkly', '2020-11-03', 'bhardery@wikispaces.com');
insert into employee (name, birthday, email) values ('Abby', '2021-05-13', 'awildberz@yale.edu');
insert into employee (name, birthday, email) values ('Sadella', '2021-07-13', 'ssinisbury10@blog.com');
insert into employee (name, birthday, email) values ('Lamond', null, 'lgaughan11@dailymail.co.uk');
insert into employee (name, birthday, email) values ('Dru', '2021-01-02', 'dtickle12@wp.com');
insert into employee (name, birthday, email) values ('Molly', '2021-05-09', 'mschwieso13@theguardian.com');
insert into employee (name, birthday, email) values ('Emerson', '2021-03-10', 'ehartless14@blinklist.com');
insert into employee (name, birthday, email) values ('Floris', '2021-03-22', 'fgiffkins15@miibeian.gov.cn');
insert into employee (name, birthday, email) values ('Wandis', '2020-12-02', 'wsellors16@huffingtonpost.com');
insert into employee (name, birthday, email) values ('Charlton', '2021-04-22', 'csabathier17@nytimes.com');
insert into employee (name, birthday, email) values ('Fredericka', '2021-03-20', 'fmcgettrick18@blogger.com');
insert into employee (name, birthday, email) values ('Melanie', '2021-05-28', 'mclohessy19@digg.com');
insert into employee (name, birthday, email) values ('Esther', '2021-03-24', 'edoumerc1a@flavors.me');
insert into employee (name, birthday, email) values ('Stacie', '2021-09-08', null);
insert into employee (name, birthday, email) values ('Adriaens', null, 'agrigorkin1c@illinois.edu');
insert into employee (name, birthday, email) values ('Pauly', '2021-08-02', 'pspirritt1d@adobe.com');

SELECT *
FROM employee;

UPDATE employee
SET birthday = '2021-08-05'
WHERE email = 'lgaughan11@dailymail.co.uk';

SELECT *
FROM employee;

UPDATE employee
SET birthday = '2020-10-10'
WHERE name = 'Dela';

SELECT *
FROM employee;

UPDATE employee
SET birthday = '2021-04-04'
WHERE id = 49;

SELECT *
FROM employee;

UPDATE employee
SET name = 'XXXX',
    email = 'xxxx@xxxx.com'
WHERE id = 14 AND birthday ='2021-04-25';

SELECT *
FROM employee;

UPDATE employee
SET email = 'xxxxx@xxxxx.com',
    name = 'xxxxx'
WHERE birthday = '2021-09-08' AND name LIKE 'St%'

SELECT *
FROM employee;

DELETE 
FROM employee
WHERE name = 'Pauly' AND email LIKE '%pspirritt%'

SELECT * 
FROM employee;

DELETE 
FROM employee
WHERE id = 1 AND birthday = '2020-10-20'
RETURNING *;

SELECT *
FROM employee;

DELETE
FROM employee
WHERE email LIKE 'abu%'
RETURNING *;

SELECT *
FROM employee;

DELETE 
FROM employee
WHERE birthday='2021-04-09' OR id = 3
RETURNING *;

SELECT *
FROM employee;

DELETE 
FROM employee
WHERE name LIKE '___' 
RETURNING *;

SELECT *
FROM employee;

