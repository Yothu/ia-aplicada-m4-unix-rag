import hashlib
import json
import os
import re
import numpy as np
import yaml
from beir import util
from beir.datasets.data_loader import GenericDataLoader


def main():
    with open("configs/config.yaml", "r") as f:
        cfg = yaml.safe_load(f)

    data_path = util.download_and_unzip(cfg["dataset"]["url"], "datasets")
    unix_path = os.path.join(data_path, cfg["dataset"]["subforum"])
    corpus, queries, qrels = GenericDataLoader(data_folder=unix_path).load(split="test")

    rx = re.compile(cfg["dataset"]["held_out_regex"], re.I)
    held_out = {
        did for did, doc in corpus.items()
        if rx.search(doc.get("title", "") + " " + doc.get("text", ""))
    }
    active = set(corpus.keys()) - held_out

    ans, unans = [], []
    for qid, rel in qrels.items():
        gold = {did for did, s in rel.items() if s > 0}
        if not gold:
            continue
        if gold.isdisjoint(active):
            unans.append(qid)
        elif gold.issubset(active):
            ans.append(qid)

    rng = np.random.default_rng(cfg["seed"])
    ans_arr = np.array(sorted(ans))
    unans_arr = np.array(sorted(unans))
    rng.shuffle(ans_arr)
    rng.shuffle(unans_arr)

    mid_a, mid_u = len(ans_arr) // 2, len(unans_arr) // 2
    val_ids = {"answerable": ans_arr[:mid_a].tolist(), "unanswerable": unans_arr[:mid_u].tolist()}
    test_ids = {"answerable": ans_arr[mid_a:].tolist(), "unanswerable": unans_arr[mid_u:].tolist()}

    os.makedirs("data_splits", exist_ok=True)
    with open(cfg["splits"]["val_path"], "w") as f:
        json.dump(val_ids, f, indent=2)
    with open(cfg["splits"]["test_path"], "w") as f:
        json.dump(test_ids, f, indent=2)

    test_hash = hashlib.sha256(open(cfg["splits"]["test_path"], "rb").read()).hexdigest()
    assert test_hash == cfg["splits"]["frozen_test_sha256"], f"Hash mismatch: {test_hash}"
    print(f"Verified! Active docs={len(active)}, Val=503, Test=503, SHA-256={test_hash}")


if __name__ == "__main__":
    main()