# Draft coverage matrix

This matrix is a scoping aid only, not an insurance policy or service promise. Confirm what is actually offered, the evidence standard, and customer/provider responsibilities before use.

| Layer | Example non-secret evidence | Possible assisted-rebuild work | Boundary / not covered by this template |
|---|---|---|---|
| 1. Identity + memory | Approved identity notes, versioned memory export, timestamps | Reassemble approved identity and memory files; check provenance | Missing, corrupted, unlawful, or third-party data; secret values |
| 2. Workspace | File inventory, repository revision, project documentation | Restore a documented local layout and customer-owned files | Deleted files without a usable copy; unsupported platforms or licenses |
| 3. Handoff | Current-state brief, known issues, last-good status | Prepare a concise recovery brief and open-items list | Decisions only the customer can make; undocumented context |
| 4. Credentials | Provider names and reconnect checklist; never the values | Guide the customer through secure, provider-side reauthentication | Collection, storage, transfer, or validation of passwords, tokens, keys, recovery codes, or MFA values |
| 5. Connections | Non-secret integration manifest, redacted error and permission list | Recreate documented integrations and verify customer-run tests | Provider/API shutdown, revoked access, policy changes, unavailable permissions |
| 6. Schedules | Schedule catalog, time zone, intended command and owner | Produce reviewed schedule definitions and a restore preview | Automatic activation without approval; unsupported scheduler or customer hardware failure |

Use the corresponding definitions in `six-layers.md`. Every claim must state the selected coverage cadence and identify the specific covered work before assistance begins.
