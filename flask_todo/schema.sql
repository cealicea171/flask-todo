

DROP TABLE IF EXISTS tasks;




CREATE TABLE tasks (
  id bigserial  PRIMARY KEY,
  task text NOT NULL,
  created_at timestamp NOT NULL,
  completed boolean NOT NULL
);
