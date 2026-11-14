# Data Card — BEIR CQADupStack (`unix` + Held-Out Abstention Split)

- **Provenance & License:** Derived from StackExchange Unix & Linux via BEIR (`https://github.com/beir-cellar/beir`), Apache-2.0 license. No private or sensitive user credentials included.
- **Unit of Analysis:** One technical support query (`query_id`) paired with ground-truth post IDs (`qrels`).
- **Raw Size & Quality Checks:** 47,382 corpus documents; 1,072 queries; 1,072/1,072 unique query strings (0 exact duplicates).
- **Exclusions & Construction of Unanswerables:**
  - Removed 11,125 documents matching 6 Unix topic clusters (`ssh/iptables`, `apt/yum/pacman`, `vim/emacs/nano`, `git/svn`, `cron/systemd`, `zsh/fish`) from the searchable index to simulate missing-documentation support queries.
  - Excluded 66 queries whose gold documents spanned both active and held-out sets.
- **Final Splits (`seed=42`):**
  - Active Index: **36,257** documents.
  - Validation (`data_splits/val_ids.json`): **503** queries (407 answerable, 96 unanswerable / 19.1%).
  - Frozen Test (`data_splits/test_ids_frozen.json`): **503** queries (407 answerable, 96 unanswerable / 19.1%).
  - Frozen Test SHA-256: `decc77b8a8ef3745a09b2d34bb5b410613638fc720e96dbd9406601a6a6150bb`.
- **Known Limits:** Corpus reflects ~2014 Unix StackExchange posts; held-out topic abstention simulates missing documentation rather than naturally annotated "impossible" user tickets.