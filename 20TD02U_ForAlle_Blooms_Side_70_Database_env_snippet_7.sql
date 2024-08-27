-- Vise aktive spørringer
        SELECT * FROM pg_stat_activity;

        -- Forklare en spørringsplan
        EXPLAIN ANALYZE SELECT * FROM kunder WHERE navn LIKE '%mann%';