-- Create your SELECT statement here
-- Keeping up with my SQL from days of yore 
SELECT
products.*,
companies.name as company_name
FROM products

join companies on products.company_id = companies.id
