-- Визначити по категоріям з яких країн країн скільки лауреатів
WITH laur_prizes as
(
	SELECT 
		pr.category, o.organizationcountry 
	FROM
		laureate as l 
		INNER JOIN organization as o ON l.organizationname = o.organizationname
		INNER JOIN prizelaureates as lp ON l.laureateid = lp.laureateid
		INNER JOIN prize as pr ON lp.id = pr.id
)
SELECT organizationcountry, category, COUNT(category) as number_prizes_in_categories FROM laur_prizes
GROUP BY organizationcountry, category
ORDER BY organizationcountry;

-- Визначити в яких категоріях і скільки отримали призів жінки
WITH laur_prizes as
(
	SELECT 
		pr.category, l.gender 
	FROM
		laureate as l 
		INNER JOIN prizelaureates as lp ON l.laureateid = lp.laureateid
		INNER JOIN prize as pr ON lp.id = pr.id
)
SELECT category, COUNT(category) as number_prizes_in_categories FROM laur_prizes
WHERE gender = 'female'
GROUP BY gender, category
ORDER BY gender;

-- Визначити у яких містах скільки чоловіків лауреатів
WITH laur_with_city as
(
	SELECT 
		l.gender, o.organizationcity
	FROM
		laureate as l INNER JOIN organization as o ON l.organizationname = o.organizationname
)
SELECT organizationcity, COUNT(gender) as number_males FROM laur_with_city
WHERE gender = 'male'
GROUP BY organizationcity, gender
ORDER BY number_males DESC