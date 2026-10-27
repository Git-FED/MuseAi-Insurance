-- Draft schema only; app does not use it and no production persistence is configured.
CREATE TABLE claims (claim_id TEXT PRIMARY KEY, claimant_ref TEXT NOT NULL, incident_date TEXT NOT NULL, layers TEXT NOT NULL, description TEXT NOT NULL, selected_option TEXT, status TEXT NOT NULL DEFAULT 'draft', created_at TEXT NOT NULL);
-- Never store credentials, tokens, passwords, private keys, or unnecessary sensitive PII.
