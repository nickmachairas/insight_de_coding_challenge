SELECT soc_name AS top_occupations, 
       COUNT(soc_name) AS number_certified_applications, 
       to_char((COUNT(soc_name)/(SELECT COUNT(*)::float 
                                 FROM lca_data 
                                 WHERE status = 'CERTIFIED'
                                   AND year = 2014)) * 100, '999D9%') AS percentage 
FROM lca_data
WHERE status = 'CERTIFIED'
  AND year = 2014
GROUP BY soc_name
ORDER BY number_certified_applications DESC, soc_name ASC
LIMIT 10;


SELECT state AS top_states, 
       COUNT(state) AS number_certified_applications, 
       to_char((COUNT(state)/(SELECT COUNT(*)::float 
                              FROM lca_data 
                              WHERE status = 'CERTIFIED'
                                AND year IS NULL)) * 100, '999D9%') AS percentage 
FROM lca_data
WHERE status = 'CERTIFIED'
  AND year IS NULL
GROUP BY state
ORDER BY number_certified_applications DESC, top_states ASC
LIMIT 10;
