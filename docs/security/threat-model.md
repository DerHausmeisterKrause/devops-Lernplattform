# Threat Model
- Authentifizierte Learner mit Terminalzugriff als Hauptangreifer.
- Ziele: Sandbox-Escape, Tenant-Breakout, DoS, SSRF.
- Kontrollen: RBAC, NetworkPolicy default deny, ResourceQuota, short-lived terminal tokens, audit logging.
