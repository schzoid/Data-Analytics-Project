CREATE OR REPLACE VIEW vw_line_performance AS
SELECT
    line,
    SUM(produced_units) AS total_production,
    SUM(defect_count) AS total_defects,
    SUM(good_units) AS total_good_units,
    ROUND(
        SUM(defect_count)::numeric / NULLIF(SUM(produced_units), 0) * 100, 2
    ) AS overall_defect_rate,
    ROUND(
        AVG(downtime_minutes)::numeric, 2
    ) AS avg_downtime
FROM production_data
GROUP BY line;

CREATE OR REPLACE VIEW vw_product_quality AS
SELECT
    product,
    SUM(produced_units) AS total_production,
    SUM(defect_count) AS total_defects,
    SUM(good_units) AS total_good_units,
    ROUND(
        SUM(defect_count)::numeric / NULLIF(SUM(produced_units), 0) * 100, 2
    ) AS overall_defect_rate
FROM production_data
GROUP BY product;

CREATE OR REPLACE VIEW vw_shift_performance AS
SELECT
    shift,
    SUM(produced_units) AS total_production,
    SUM(defect_count) AS total_defects,
    ROUND(
        SUM(defect_count)::numeric / NULLIF(SUM(produced_units), 0) * 100, 2
    ) AS overall_defect_rate,
    ROUND(
        AVG(downtime_minutes)::numeric, 2
    ) AS avg_downtime
FROM production_data
GROUP BY shift;