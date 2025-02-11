-- section 1
SELECT
    t.first_name,
    t.last_name,
    t.passport_number,
    t.date_of_birth,
    t.gender,
    t.email,
    t.phone,
    t.tour_id,
    c.country_name
FROM tourists t
    INNER JOIN countries c
        ON t.country_id = c.id;

-- section 2
SELECT
   tourists.id as tourist_id,
   tourists.first_name,
   tourists.last_name,
   tourists.passport_number,
   tourists.date_of_birth,
   tourists.gender,
   tourists.email,
   tourists.phone,
   tourists.tour_id,
   tours.tour_name,
   tours.description,
   tours.start_date,
   tours.end_date,
   tours.price,
   tours.max_participants,
   tours.guide_name,
   tours.difficulty_level,
   tours.pickup_location
FROM tourists
   JOIN tours
       ON tourists.tour_id = tours.id;

-- section 3
SELECT
   tourists.id as tourist_id,
   tourists.first_name,
   tourists.last_name,
   tourists.passport_number,
   tourists.date_of_birth,
   tourists.gender,
   tourists.email,
   tourists.phone,
   tourists.tour_id,
   tours.tour_name,
   tours.description,
   tours.start_date,
   tours.end_date,
   tours.price,
   tours.max_participants,
   tours.guide_name,
   tours.difficulty_level,
   tours.pickup_location
FROM tourists
   LEFT JOIN tours
       ON tourists.tour_id = tours.id;

-- section 4
SELECT
   tourists.id as tourist_id,
   tourists.first_name,
   tourists.last_name,
   tourists.passport_number,
   tourists.date_of_birth,
   tourists.gender,
   tourists.email,
   tourists.phone,
   tours.id,
   tours.tour_name,
   tours.description,
   tours.start_date,
   tours.end_date,
   tours.price,
   tours.max_participants,
   tours.guide_name,
   tours.difficulty_level,
   tours.pickup_location
FROM tourists
   FULL JOIN tours
       ON tourists.tour_id = tours.id;
