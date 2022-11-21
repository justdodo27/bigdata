%DECLARE collisions_path $input_dir3/results.csv
%DECLARE zips_path $input_dir4/zips-boroughs.csv
%DECLARE output_path $output_dir6

--LOAD FILES
collision = LOAD '$collisions_path' USING org.apache.pig.piggybank.storage.CSVExcelStorage('\t',
    'NO_MULTILINE','NOCHANGE')
    as (street: chararray, 
        zipcode: chararray, 
        person_type:chararray, 
        collision_type: chararray, 
        collision_num:int);
DESCRIBE collision;

borough = LOAD '$zips_path' USING org.apache.pig.piggybank.storage.CSVExcelStorage(',',
    'NO_MULTILINE','NOCHANGE', 'SKIP_INPUT_HEADER')
    as (
        zipcode: chararray,
        borough: chararray
    );

DESCRIBE borough;

-- JOIN
collision_borough = JOIN collision BY zipcode, borough BY zipcode;

DESCRIBE collision_borough;

-- FILTER
collision_manhatan = FILTER collision_borough BY (borough::borough == 'MANHATTAN');

DESCRIBE collision_manhatan;

collision_grouped = GROUP collision_manhatan BY (collision::street, collision::person_type, collision::collision_type);

DESCRIBE collision_grouped;

collision_sum = FOREACH collision_grouped GENERATE
    group.collision::street as street,
    group.collision::person_type as person_type, 
    group.collision::collision_type as collision_type,
    SUM(collision_manhatan.collision::collision_num) as collision_sum;

DESCRIBE collision_sum;


collision_injured = FILTER collision_sum BY (collision_type == 'injured');

DESCRIBE collision_injured;

collision_killed = FILTER collision_sum BY (collision_type == 'killed');

DESCRIBE collision_killed;

-- JOIN injured and killed
collision_all = JOIN collision_injured BY (street, person_type), collision_killed BY (street, person_type);

DESCRIBE collision_all;

collision_final = FOREACH collision_all GENERATE
    collision_injured::street as street,
    collision_injured::person_type as person_type,
    collision_injured::collision_sum as injured,
    collision_killed::collision_sum as killed,
    (collision_injured::collision_sum + collision_killed::collision_sum) as collision_sum;

DESCRIBE collision_final;

collision_final_grouped = GROUP collision_final BY person_type;

DESCRIBE collision_final_grouped;


collision_pedestrians = FILTER collision_final_grouped BY (group == 'pedestrians');
collision_pedestrians_flatten = FOREACH collision_pedestrians GENERATE
    FLATTEN(collision_final);
collision_pedestrians_limit = LIMIT (ORDER collision_pedestrians_flatten BY collision_final::collision_sum DESC) 3;


collision_cyclists = FILTER collision_final_grouped BY (group == 'cyclists');
collision_cyclists_flatten = FOREACH collision_cyclists GENERATE
    FLATTEN(collision_final);
collision_cyclists_limit = LIMIT (ORDER collision_cyclists_flatten BY collision_final::collision_sum DESC) 3;

collision_motorists = FILTER collision_final_grouped BY (group == 'motorists');
collision_motorists_flatten = FOREACH collision_motorists GENERATE
    FLATTEN(collision_final);
collision_motorists_limit = LIMIT (ORDER collision_motorists_flatten BY collision_final::collision_sum DESC) 3;

collision_union = UNION collision_pedestrians_limit, collision_cyclists_limit, collision_motorists_limit;

final_result = FOREACH collision_union GENERATE
    collision_final::street AS street,
    collision_final::person_type AS person_type,
    collision_final::injured AS injured,
    collision_final::killed AS killed;
DESCRIBE final_result;

--STORE
STORE collision_sum INTO '$output_path' USING JsonStorage();