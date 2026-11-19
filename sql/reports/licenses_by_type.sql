-- Purpose: Count of active licenses by license type.
SELECT
    license_type,
    COUNT(*) AS active_count
FROM rpt.active_licenses
GROUP BY license_type
ORDER BY active_count DESC;
