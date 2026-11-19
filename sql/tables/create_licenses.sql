-- Purpose: Staging table for the nightly license extract.
CREATE TABLE stg.licenses (
    license_id     VARCHAR(20)  NOT NULL PRIMARY KEY,
    business_name  VARCHAR(200) NOT NULL,
    license_type   VARCHAR(50)  NOT NULL,
    county         VARCHAR(50)  NULL,
    status         VARCHAR(20)  NOT NULL,
    issued_date    DATE         NOT NULL,
    expires_date   DATE         NOT NULL
);
