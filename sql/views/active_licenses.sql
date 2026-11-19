-- Purpose: Licenses that are currently active. Used by the public dashboard.
CREATE OR ALTER VIEW rpt.active_licenses AS
SELECT
    license_id,
    business_name,
    license_type,
    county,
    issued_date,
    expires_date
FROM stg.licenses
WHERE UPPER(TRIM(status)) = 'ACTIVE';
