SHOW GLOBAL VARIABLES LIKE 'PORT';
SET GLOBAL FOREIGN_KEY_CHECKS=1;

use rent_kitten;

insert into user(firstname, lastname, email, password, created_at, updated_at) values('Peter','Smith', 'smith@yahoo.com','smith', NOW(), NOW());
insert into user(firstname, lastname, email, password, created_at, updated_at) values('Jane','Doe', 'jane@yahoo.com','smith', NOW(), NOW());
select * from user;

insert into address(street, city, zip, phone, created_at, updated_at, user_id) values('123 Zoo Dr', 'San Jose', '95148', '408-234-4365',NOw(), NOW(),1);
insert into address(street, city, zip, phone, created_at, updated_at, user_id) values('123 Planet Dr', 'San Jose', '95148', '608-214-4365',NOw(), NOW(),2);
select * from address;

insert into pricing(types,price, created_at, updated_at) values('rent',10, NOW(), NOW());
insert into pricing(types,price, created_at, updated_at) values('adopt',5, NOW(), NOW());
select * from pricing;

insert into cat(name, breed, status, created_at, updated_at,user_id, pricing_id) values('django', 'tabby', 'rented', NOW(), NOW(), 1,1);
insert into cat(name, breed, status, created_at, updated_at,user_id, pricing_id) values('sculley', 'tabby', 'rented', NOW(), NOW(), 1, 1);
insert into cat(name, breed, status, created_at, updated_at,user_id, pricing_id) values('maulder', 'skinny', 'rented', NOW(), NOW(),1,1);
insert into cat(name, breed, status, created_at, updated_at,user_id, pricing_id) values('spike', 'tabby', 'rented', NOW(), NOW(),2,1);
insert into cat(name, breed, status, created_at, updated_at,user_id, pricing_id) values('wanderer', 'tabby', 'adopted', NOW(), NOW(),2,2);
select * from cat;

insert into invoice(price, created_at, updated_at, user_id) values(30, NOW(), NOW(), 1);
insert into invoice(price, created_at, updated_at, user_id) values(15, NOW(), NOW(), 2);
select * from invoice;
