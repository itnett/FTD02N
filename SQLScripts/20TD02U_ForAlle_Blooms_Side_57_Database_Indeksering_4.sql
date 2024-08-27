sql
-- Analysera spørringsmønstre og foreslå optimal indeksering
-- Eksempel: Opprettelse av flere indekser basert på spørringsanalyse
CREATE INDEX idx_alder ON elever (alder);
CREATE INDEX idx_navn_alder ON elever (navn, alder);