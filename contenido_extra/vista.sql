-- Crear una vista que muestre el monto total transaccionado por día para las diferentes compañías
CREATE OR REPLACE VIEW total_amount_by_company_and_day AS
SELECT
    c.name AS company_name,
    c.id AS company_id,
    ch.created_at::date AS transaction_date,
    SUM(ch.amount) AS total_amount
FROM
    charges ch
JOIN
    companies c ON ch.company_id = c.id
GROUP BY
    c.name, c.id, ch.created_at::date;
	
-- Consulta de la vista
SELECT * FROM total_amount_by_company_and_day;


