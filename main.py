import psycopg2
import matplotlib.pyplot as plt
import numpy as np

username = 'Shkarupylo'
password = 'Shkarupylo'
database = 'NobelPrizeWinners'
host = 'localhost'
port = '5432'

query_3 = '''
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
'''
query_2 = '''
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
'''
query_1 = '''
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
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
    cur = conn.cursor()

    for i, query in enumerate([query_1, query_2, query_3]):
        if i != 0:
            print()
            print('_'*20)
            print()
        print(f'Запит {i+1}')
        cur.execute(query_1)

        for row in cur:
            print(row)


