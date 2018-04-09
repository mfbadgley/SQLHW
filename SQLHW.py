
1a. Display the first and last names of all actors from the table actor.
1b. Display the first and last name of each actor in a single column in upper case letters. Name the column Actor Name.
2a. You need to find the ID number, first name, and last name of an actor, of whom you know only the first name, "Joe." What is one query would you use to obtain this information?
2b. Find all actors whose last name contain the letters GEN:
2c. Find all actors whose last names contain the letters LI. This time, order the rows by last name and first name, in that order:
2d. Using IN, display the country_id and country columns of the following countries: Afghanistan, Bangladesh, and China:
3a. Add a middle_name column to the table actor. Position it between first_name and last_name. Hint: you will need to specify the data type.
3b. You realize that some of these actors have tremendously long last names. Change the data type of the middle_name column to blobs.
3c. Now delete the middle_name column.
4a. List the last names of actors, as well as how many actors have that last name.
4b. List last names of actors and the number of actors who have that last name, but only for names that are shared by at least two actors
4c. Oh, no! The actor HARPO WILLIAMS was accidentally entered in the actor table as GROUCHO WILLIAMS, the name of Harpo's second cousin's husband's yoga teacher. Write a query to fix the record.
4d. Perhaps we were too hasty in changing GROUCHO to HARPO. It turns out that GROUCHO was the correct name after all! In a single query, if the first name of the actor is currently HARPO, change it to GROUCHO. Otherwise, change the first name to MUCHO GROUCHO, as that is exactly what the actor will be with the grievous error. BE CAREFUL NOT TO CHANGE THE FIRST NAME OF EVERY ACTOR TO MUCHO GROUCHO, HOWEVER! (Hint: update the record using a unique identifier.)
5a. You cannot locate the schema of the address table. Which query would you use to re-create it?
Hint: https://dev.mysql.com/doc/refman/5.7/en/show-create-table.html
6a. Use JOIN to display the first and last names, as well as the address, of each staff member. Use the tables staff and address:
6b. Use JOIN to display the total amount rung up by each staff member in August of 2005. Use tables staff and payment.
6c. List each film and the number of actors who are listed for that film. Use tables film_actor and film. Use inner join.
6d. How many copies of the film Hunchback Impossible exist in the inventory system?
6e. Using the tables payment and customer and the JOIN command, list the total paid by each customer. List the customers alphabetically by last name:
    ![Total amount paid](Images/total_payment.png)
7a. The music of Queen and Kris Kristofferson have seen an unlikely resurgence. As an unintended consequence, films starting with the letters K and Q have also soared in popularity. Use subqueries to display the titles of movies starting with the letters K and Q whose language is English.
7b. Use subqueries to display all actors who appear in the film Alone Trip.
7c. You want to run an email marketing campaign in Canada, for which you will need the names and email addresses of all Canadian customers. Use joins to retrieve this information.
7d. Sales have been lagging among young families, and you wish to target all family movies for a promotion. Identify all movies categorized as famiy films.
7e. Display the most frequently rented movies in descending order.
7f. Write a query to display how much business, in dollars, each store brought in.
7g. Write a query to display for each store its store ID, city, and country.
7h. List the top five genres in gross revenue in descending order. (Hint: you may need to use the following tables: category, film_category, inventory, payment, and rental.)
8a. In your new role as an executive, you would like to have an easy way of viewing the Top five genres by gross revenue. Use the solution from the problem above to create a view. If you haven't solved 7h, you can substitute another query to create a view.
8b. How would you display the view that you created in 8a?
8c. You find that you no longer need the view top_five_genres. Write a query to delete it.


use sakila;

select first_name, last_name from actor;

ALTER TABLE actor
ADD `Actor Name` varchar(30);


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

SELECT last_name, count(*) as NUM FROM actor GROUP BY last_name;

SELECT last_name, count(*) as NUM FROM actor GROUP BY last_name
Having NUM >= 2;

UPDATE actor
SET first_name= 'HARPO'
WHERE first_name = 'Groucho' and last_name='Williams';

UPDATE actor
SET first_name= 'GROUCHO'
WHERE first_name = 'Harpo' and last_name='Williams';

****not sure about the second half of 4D question, what they are asking to do...

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

#you get the film_id that matches 'Alone Trip', then you select the actor_ids that have the 
#film_id you returned, then you get the first_name and last_name of the actors with the 
#actor_ids you returned...

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

select name, sum(amount)
from category
join film_category
on (category.category_id = film_category.category_id)
join inventory
on (inventory.film_id = film_category.film_id)
join rental
on (rental.inventory_id = inventory.inventory_id)
join payment
on (payment.rental_id = rental.rental_id)
group by name order by sum(amount) Desc limit 5;

create view top_five as 
select name, sum(amount)
from category
join film_category
on (category.category_id = film_category.category_id)
join inventory
on (inventory.film_id = film_category.film_id)
join rental
on (rental.inventory_id = inventory.inventory_id)
join payment
on (payment.rental_id = rental.rental_id)
group by name order by sum(amount) Desc limit 5;

select * from top_five;

Drop View top_five;