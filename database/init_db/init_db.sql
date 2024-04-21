CREATE TABLE table_name
(
    col1 int,
    col2 char,
)

-- update postgres date format for any CSV ingestion to be YMD instead of default MDY
SET datestyle 'ISO YMD'

-- Note that the parent_path is the working directory defined in db.dockerfile, in this example, db_app
-- COPY table_name FROM '/db_app/sample.csv' DELIMITER ',' CSV header;
COPY table_name FROM '/<parent_path>/<filename.csv>' DELIMITER ',' CSV header;