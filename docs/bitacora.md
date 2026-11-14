# Bitácora de Evidencias

## Sesión 1 (6 nov) — Borrador de ficha de problema
- **Usuario:** Desarrollador / sysadmin consultando documentación Unix.
- **Decisión apoyada:** Aplicar un comando/configuración documentada o escalar si falta en la base (`ABSTAIN`).
- **Unidad de análisis:** Una consulta técnica (`query_id`) contra el corpus `unix` (`doc_id`).
- **Métrica primaria:** Citation-Abstention Accuracy; secundarias: nDCG@10, Abstention F1; operacional: latencia p95 y RAM del índice.

## Sesión 2 (7 nov) — Auditoría inicial de datos y protocolo experimental
- **Dataset:** BEIR – CQADupStack (`unix`, Apache-2.0).
- **Auditoría:** 47,382 documentos totales; 1,072 consultas únicas (0 duplicados exactos).
- **Hold-out de tópicos para abstención:** Inicialmente solo `systemd/iptables/zsh` arrojó 27 consultas no respondibles (insuficiente). Se amplió a 6 clústeres de tópicos Unix (11,125 docs removidos), logrando **36,257 docs activos**, **814 respondibles** y **192 `ABSTAIN`** (66 consultas ambiguas excluidas).
- **Partición congelada (`seed=42`):** Val (407 ans / 96 unans) y Test congelado (407 ans / 96 unans).
- **Hash SHA-256 del test congelado:** `decc77b8a8ef3745a09b2d34bb5b410613638fc720e96dbd9406601a6a6150bb`.