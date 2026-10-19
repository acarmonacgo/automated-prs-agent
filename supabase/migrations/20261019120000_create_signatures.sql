CREATE TABLE signatures (
    id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    petition_id bigint NOT NULL,
    email text NOT NULL,
    country_code text NOT NULL,
    signed_at timestamptz NOT NULL
);

CREATE UNIQUE INDEX signatures_petition_id_lower_email_idx
    ON signatures (petition_id, lower(email));
