# Technical Support Documentation Q&A with Abstention (Route C: RAG)

**Course:** Diplomado en Inteligencia Artificial 2026 – Módulo 4 (PUCV)  
**Team:** [David Vergaray]  

## 1. Problem & Non-Use Limits
This project builds a grounded Unix technical support Q&A assistant over **BEIR – CQADupStack (`unix`)**. Given a developer/sysadmin query, the system either returns an answer with verifiable `[DocID]` citations from the indexed corpus or outputs **`ABSTAIN`** when the answer is missing from the knowledge base.

**When NOT to use this system:** Never auto-execute destructive shell/root commands (`rm`, `dd`, `chmod`, firewall, or disk changes) without human confirmation, and never rely on it for undocumented proprietary infrastructure.

## 2. Installation & Execution
```bash
pip install -r requirements.txt
python src/prepare_data.py