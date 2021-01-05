/* Kisilerin gemi sayisini ekrana yazdiran trigger  */

create or replace function owner_and_ship_count_trigger() returns trigger AS $$
declare 
 mq integer;
 ship_count integer;
begin
 mq := new.ownerId;
 raise notice 'yeni geminin sahip ID si: %',mq;
 if mq = new.OwnerId 
	then
		select into ship_count count(shipID)
		from ships
		WHERE ships.OwnerId = mq;
 end if;
 raise notice 'degisim/ekleme sonrasi bu kisi % gemiye sahip', ship_count;
 return NULL;
end;
$$ language plpgsql;


create trigger trigcount
after insert or update ON ships
for each row execute procedure owner_and_ship_count_trigger();



/* Ayni tipteki gemi sayisini ekrana yazdiran trigger  */

create or replace function type_and_ship_count_trigger() returns trigger AS $$
declare 
 mq integer;
 ship_count integer;
begin
 mq := new.typeId;
 raise notice 'yeni geminin tip ID si: %',mq;
 if mq = new.typeId 
	then
		select into ship_count count(shipID)
		from ships
		WHERE ships.typeId = mq;
 end if;
 raise notice 'degisim/ekleme sonrasi bu tipte % gemi oldu', ship_count;
 return NULL;
end;
$$ language plpgsql;


create trigger trigcount
after insert or update ON ships
for each row execute procedure type_and_ship_count_trigger();


/* Views */

create or replace view ownerAndShips as
select shipName, ownerName, o.ownerId, ownerLname
from ships s, owners o
where s.ownerId = o.ownerId;

create or replace view typeAndShips as
select shipName, typeName, t.typeId
from ships s, typess t
where s.typeId = t.typeId;

create or replace view historyAndShip as
select shipName, r.recId
from ships s, history r
where s.shipId = r.shipId;