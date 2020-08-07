use sakila;

select country, city
  from country
 left join (
 select * 
   from city
  where city='Moscow'
 ) as city_sub
 using (country_id);
 
select country, city
  from country
 left join city using (country_id)
 where city.city='Moscow';

 