-- JOIN
SELECT * FROM orders;

-- I want to get all the orders and the user that placed them
SELECT * FROM users
JOIN orders ON users.id = orders.user_id;

SELECT * FROM orders
JOIN orders_items ON orders.id = orders_items.order_id
JOIN items ON items.id = orders_items.item_id;


SELECT * FROM users
JOIN orders ON users.id = orders.user_id
JOIN orders_items ON orders.id = orders_items.order_id
JOIN items ON items.id = orders_items.item_id
WHERE orders.amount > 1000
ORDER BY items.name DESC;


SELECT users.first_name, COUNT(orders.user_id) as count_of_orders FROM users
JOIN orders ON users.id = orders.user_id
WHERE orders.user_id = 1
GROUP BY orders.user_id;

SELECT orders.amount, COUNT(orders_items.order_id) as num_of_items FROM orders
JOIN orders_items ON orders.id = orders_items.order_id
JOIN items ON items.id = orders_items.item_id
GROUP BY orders_items.order_id;



SELECT * FROM users;
-- USING A JOIN
SELECT users.first_name, users.last_name, orders.amount FROM users
JOIN orders ON users.id = orders.user_id;