# Draft evidence checklist

Provide only non-secret evidence. Keep original files on the customer host; submit redacted summaries, filenames, timestamps, versions, hashes, and customer-owned exports only when necessary. Remove unrelated personal data.

- [ ] **1. Identity + memory:** approved identity notes, memory export reference, version/date.
- [ ] **2. Workspace:** project/repository name, revision, relevant filenames, environment summary.
- [ ] **3. Handoff:** last-known-good date, current state, known blockers and human decisions.
- [ ] **4. Credentials:** list providers/accounts requiring reconnect; never attach values, screenshots exposing secrets, recovery codes, or MFA data.
- [ ] **5. Connections:** names of affected integrations, non-secret permission/config summary, redacted errors.
- [ ] **6. Schedules:** job names, time zone, intended cadence, last successful run, non-secret command reference.

Do not submit passwords, API keys/tokens, private keys, cookies, recovery codes, or other secrets. If an item may contain a secret, retain it locally and ask for a safer redacted description.
