use sakila;

select first_name, last_name from actor;


SELECT CONCAT (first_name,' ',last_name) As `Actor Name`
FROM actor;

SELECT actor_id, first_name, last_name
    FROM actor
    WHERE first_name LIKE 'Joe'

SELECT  *
    FROM actor
    WHERE last_name LIKE '%GEN%'
    
SELECT  *
    FROM actor
    WHERE last_name LIKE '%LI%'
    Order by last_name, first_name
    
    
SELECT country_id, country
  FROM country
  WHERE country IN ('afghanistan', 'bangladesh', 'china')
  

  
ALTER TABLE actor
ADD column `Middle Name` varchar(30)
after first_name;

ALTER TABLE actor
modify COLUMN `Middle Name` Blob;

ALTER TABLE actor
DROP COLUMN `Middle Name`;


SELECT last_name, count(*) as NUM FROM actor GROUP BY last_name
Having NUM >= 2;

UPDATE actor
SET first_name= 'HARPO'
WHERE first_name = 'Groucho' and last_name='Williams';

UPDATE actor
SET first_name= 'GROUCHO'
WHERE first_name = 'Harpo' and last_name='Williams';

SHOW CREATE TABLE address;

SELECT first_name, last_name, address
from staff
Left join address
ON staff.address_id=address.address_id;

SELECT first_name, last_name, staff_id,SUM(amount) as total_payment
from staff
Left join payment
Using (staff_id)
Where payment_date Like  '%2005-08%'
group by staff_id;

SELECT title, count(actor_id)
from film
inner join film_actor
Using (film_id)
group by title;

Select title, count(inventory_id)
from film
inner join inventory
Using(film_id)
where title LIKE 'hunch%'
group by title; 

Select first_name, last_name, Sum(amount) As total
from customer
inner join payment
Using(customer_id)
group by customer_id
Order by last_name;


Select title
From film
Where title Like 'k%' or title Like 'Q%'
And Language_id = 1;

select first_name, last_name
From actor
Where actor_id IN(
 Select actor_id
 From film_actor
 Where film_id IN(
  Select film_id 
  From film
  Where title='Alone Trip')
  );

Select first_name, last_name, email, country
From customer
join address
on (customer.address_id=address.address_id)
join city 
on (city.city_id=address.city_id)
join country
on (country.country_id=city.country_id)
where country Like "canada";


select title
from film
where film_id In 
(select film_id
from film_category
where category_id in(
select category_id
from category
where name = "Family"));


select title, count(rental_id) As rental_count
from film 
join inventory
on (film.film_id=inventory.film_id)
join rental 
on (rental.inventory_id = inventory.inventory_id)
group by rental.inventory_id
order by count(rental_id) Desc;

select store.store_id, sum(amount)
From store
join customer
on (store.store_id=customer.store_id)
join payment
on (payment.customer_id = customer.customer_id)
group by store.store_id;

select store_id, city, country
From store
join address
on (store.address_id=address.address_id)
join city
on (city.city_id = address.city_id)
join country
on (country.country_id = city.country_id);


select sum(amount) from payment;
