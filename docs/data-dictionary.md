# Data dictionary - stg.licenses

| Column | Type | Meaning |
| --- | --- | --- |
| license_id | VARCHAR(20) | Unique license number, e.g. LIC-0001 |
| business_name | VARCHAR(200) | Registered business name |
| license_type | VARCHAR(50) | Retailer, Cultivator, Product Manufacturer, Microbusiness, Transporter |
| county | VARCHAR(50) | County of the licensed premises |
| status | VARCHAR(20) | Current license status as sent by the source system |
| issued_date | DATE | Date the license was issued |
| expires_date | DATE | Date the license expires |
