CREATE TABLE IF NOT EXISTS raw_data (
	data_id serial PRIMARY KEY,
	creation_time TIMESTAMP NOT NULL,
	value INT NOT NULL
);
