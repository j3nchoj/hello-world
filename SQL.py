SELECT
v2org.id, COUNT(*)
FROM
tg_user
u
JOIN
v2organization
v2org
ON
u.v2organization_id = v2org.id
WHERE
u.home_v2organization_id
IS
NULL
GROUP
BY
v2org.id
Limit
100;
