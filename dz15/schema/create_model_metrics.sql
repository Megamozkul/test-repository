CREATE TABLE IF NOT EXISTS model_metrics (
    uid SERIAL PRIMARY KEY,
    model_name VARCHAR(100) NOT NULL,
    accuracy NUMERIC(5,4) NOT NULL,
    precision NUMERIC(5,4) NOT NULL,
    recall NUMERIC(5,4) NOT NULL,
    f1_score NUMERIC(5,4) NOT NULL);