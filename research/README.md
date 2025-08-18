# Research Ingestion Guide

This folder documents how to add research outputs (LLM generated) into the site.

## Folder Map
```
docs/
  data/
    refs/                # BibTeX shards
    glossary_fragments/  # YAML glossary shards
    references.bib       # auto-generated on build
    glossary.yaml        # auto-generated on build
```

## Naming Rules
- Prefix each shard with `R_` followed by a short slug.
- Reference shards use `.bib` extension; glossary shards use `.yaml`.
- Inside `.bib` files, use standard BibTeX keys (e.g., `schultz1997`).

## Sample Payloads
**docs/data/refs/R_sample.bib**
```bibtex
@article{schultz1997,
  author = {Schultz, Wolfram and Dayan, Peter and Montague, P. Read},
  title = {A Neural Substrate of Prediction and Reward},
  journal = {Science},
  year = {1997},
  doi = {10.1126/science.275.5306.1593}
}
```

**docs/data/glossary_fragments/R_sample.yaml**
```yaml
incentive salience: "The 'wanting' property of a stimulus driving approach."
```

## 5-Step Workflow
1. Drop new `R_*.bib` and `R_*.yaml` shards into the folders above.
2. Reference the material in pages using anchors like `[[R_sample-C01]]` and citations like `[@schultz1997]`.
3. Run `mkdocs build --strict` to merge shards into `references.bib` and `glossary.yaml`.
4. Review the build output and verify links resolve.
5. Commit the shards and page updates, then open a pull request.
