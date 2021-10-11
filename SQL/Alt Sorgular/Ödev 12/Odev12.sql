
-- Ödev 12

/*
Merhabalar,

Aşağıdaki sorgu senaryolarını dvdrental örnek veri tabanı üzerinden gerçekleştiriniz.



1.film tablosunda film uzunluğu length sütununda gösterilmektedir. Uzunluğu ortalama film uzunluğundan fazla kaç tane film vardır?
2.film tablosunda en yüksek rental_rate değerine sahip kaç tane film vardır?
3.film tablosunda en düşük rental_rate ve en düşün replacement_cost değerlerine sahip filmleri sıralayınız.
4.payment tablosunda en fazla sayıda alışveriş yapan müşterileri(customer) sıralayınız.




Kolay Gelsin.
*/

SELECT COUNT(*)
FROM film
WHERE length > 
(
  SELECT AVG(length)
  FROM film
);

SELECT COUNT(*)
FROM film
WHERE rental_rate = 
(
  SELECT MAX(rental_rate)
  FROM film
);

SELECT *
FROM film
WHERE (film_id,rental_rate,replacement_cost) IN
(
  SELECT film_id, MIN(rental_rate) ,MIN(replacement_cost)
  FROM film
  GROUP BY film_id
);

SELECT customer_id,amount
FROM payment
WHERE (customer_id, amount) IN
(
  SELECT customer_id, MAX(amount)
  FROM payment
  GROUP BY customer_id
);
  


