# The six rebuild layers

The coverage model uses six layers. Identity and memory are grouped together to keep the six-layer count consistent across the offer and the Muse Resurrection kit.

1. **Identity + memory** — user-approved identity, stable preferences, role instructions, and customer-owned memory exports. No secret values.
2. **Workspace** — project files, prompts, documentation, local folder layout, and customer-owned artifacts.
3. **Handoff** — current-state brief, recovery notes, known gaps, and human decisions needed to resume work.
4. **Credentials** — a secure reconnect checklist only. The customer re-enters secrets into the provider’s official UI or trusted local secret store; this template never collects, exports, or stores credential values.
5. **Connections** — integrations, tools, account links, and non-secret configuration, reconnected and tested with least privilege.
6. **Schedules** — documented recurring jobs, time zones, owners, and intended run behavior; changes are previewed and approved before installation.

## Rebuild sequence

**Package → Import → Reconnect → Schedule → Prove.** Packaging and importing concern customer-owned artifacts. Reconnection is performed by the customer without sharing secrets. Scheduling follows reconnection. Proof is a report of agreed checks, not a guarantee of identical behavior or provider availability.

## Evidence and limits

Evidence should be limited to non-secret filenames, timestamps, versions, redacted errors, and customer-owned exports. A layer may be partially or wholly unrecoverable if source data, account access, provider support, or customer hardware is unavailable. The coverage matrix and exclusions are draft scoping aids, not a binding promise.
