-- Purpose: Active licenses by type and county.
SELECT
    license_type,
    county,
    COUNT(*) AS active_count
FROM rpt.active_licenses
GROUP BY license_type, county
ORDER BY license_type, county;
