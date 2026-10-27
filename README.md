<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/cpintl-org/.github/main/profile/assets/cpi-logo-circle-badge-200.png">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/cpintl-org/.github/main/profile/assets/cpi-logo-circle-badge-200.png">
  <img src="https://raw.githubusercontent.com/cpintl-org/.github/main/profile/assets/cpi-logo-circle-badge-200.png" alt="Community Partners International (CPI)" width="30%">
</picture>

<br><br>

# cpintl-org

### Unofficial GitHub organization of **Community Partners International (CPI)**
Managed by **Mohammad Ariful ISLAM**, Health Program Manager (HPM), Bangladesh Mission

<br>

[![CPI website](https://img.shields.io/badge/website-cpintl.org-2d2926?style=for-the-badge&labelColor=d91e4d)](https://cpintl.org/)  
[![CPI Bangladesh](https://img.shields.io/badge/website-cpintl.org%2Fbangladesh-2d2926?style=for-the-badge&labelColor=d91e4d)](https://cpintl.org/bangladesh/)

<br>

</div>

---

# CPINTL Public Site Repository Blueprint

Design document for the repository `cpintl-org.github.io`: what it contains, why, how it is published, and how it is changed.

> **Status:** draft for review. Blueprint version `0.1.0-draft.1`, dated 2026-10-27. Nothing in this document has been published yet.

## 1. Purpose and scope

The repository is the public face of the CPINTL GitHub organization. It serves three things:

1. A small public website (home, about, structure overview, glossary, standards listing).
2. The public JSON Schemas for the hierarchy registry, at stable URLs that the schemas use as their `$id`.
3. A small automated check that keeps the schemas valid.

Out of scope: private working documents, personal data, project or partner records, financial information, and anything that needs access control. Those belong in private repositories or in Google Workspace shared drives.

## 2. Design principles

1. **Public by default means safe by default.** Every file is readable by anyone. Content rules in section 7 are a hard gate, not a guideline.
2. **Web browser only.** Every step works in the GitHub web interface on the free plan. No command line and no local tools are required to maintain it.
3. **Stable identifiers.** A published URL that is used as a schema `$id` never changes or disappears.
4. **Small and static.** Plain Markdown pages, one built-in theme, no custom JavaScript, no external services.
5. **One purpose per file.** Each file has a single job, listed in section 4.
6. **Changes are reviewed.** Every change goes through a pull request that the owner reads before merging.
7. **Check what can be checked.** Schemas are validated automatically on every change.

## 3. Audience and public URLs

Audience: CPI staff and partners, and anyone who needs to resolve a schema URL.

| Path | Public URL | Source file | Phase |
|---|---|---|---|
| Home | `https://cpintl-org.github.io/` | `index.md` | 1 |
| Not found page | any missing path | `404.md` | 1 |
| About | `https://cpintl-org.github.io/about/` | `about/index.md` | 2 |
| Structure overview | `https://cpintl-org.github.io/structure/` | `structure/index.md` | 2 |
| Global and HQ | `https://cpintl-org.github.io/structure/global-and-hq.html` | `structure/global-and-hq.md` | 2 |
| Bangladesh Mission | `https://cpintl-org.github.io/structure/bangladesh-mission.html` | `structure/bangladesh-mission.md` | 2 |
| Thailand Mission | `https://cpintl-org.github.io/structure/thailand-mission.html` | `structure/thailand-mission.md` | 2 |
| Myanmar Mission | `https://cpintl-org.github.io/structure/myanmar-mission.html` | `structure/myanmar-mission.md` | 2 |
| Glossary | `https://cpintl-org.github.io/glossary/` | `glossary/index.md` | 2 |
| Standards listing | `https://cpintl-org.github.io/standards/` | `standards/index.md` | 2 |
| Schemas index | `https://cpintl-org.github.io/schemas/` | `schemas/index.md` | 1 |
| Node schema | `https://cpintl-org.github.io/schemas/hierarchy-node.schema.json` | `schemas/hierarchy-node.schema.json` | 1 |
| Position schema | `https://cpintl-org.github.io/schemas/hierarchy-position.schema.json` | `schemas/hierarchy-position.schema.json` | 1 |
| Relation schema | `https://cpintl-org.github.io/schemas/hierarchy-relation.schema.json` | `schemas/hierarchy-relation.schema.json` | 1 |

Pages made from Markdown are served as `.html` (or as a folder URL when the file is `index.md`). Files that are not Markdown, such as the schema JSON files, are served as they are.

## 4. Full repository tree

Phase 1 is the launch set. Phase 2 is public content, added after approval. Phase 3 is optional and depends on decisions in section 11.

```text
cpintl-org.github.io/
|-- README.md                                  phase 1   repository guide; not published on the site
|-- BLUEPRINT.md                               phase 1   this design document; not published on the site
|-- CHANGELOG.md                               phase 1   change history (Keep a Changelog layout); not published
|-- _config.yml                                phase 1   site settings and the exclude list
|-- index.md                                   phase 1   home page
|-- 404.md                                     phase 1   page shown for missing paths
|-- about/
|   `-- index.md                               phase 2   about CPI (approved mission sentence only)
|-- structure/
|   |-- index.md                               phase 2   levels L0 to L5 explained in plain words
|   |-- global-and-hq.md                       phase 2   global layer and HQ divisions, role titles only
|   |-- bangladesh-mission.md                  phase 2   departments and units, role titles only
|   |-- thailand-mission.md                    phase 2   role level, marked to be detailed
|   `-- myanmar-mission.md                     phase 2   role level, marked to be detailed
|-- glossary/
|   `-- index.md                               phase 2   public glossary with term IDs (GLO-001 style)
|-- standards/
|   `-- index.md                               phase 2   list of standards repositories; purpose to be defined
|-- schemas/
|   |-- index.md                               phase 1   human-readable list of schemas and their URLs
|   |-- hierarchy-node.schema.json             phase 1   JSON Schema for one node row
|   |-- hierarchy-position.schema.json         phase 1   JSON Schema for one position row
|   `-- hierarchy-relation.schema.json         phase 1   JSON Schema for one relation row
|-- tools/
|   `-- check_schemas.py                       phase 1   checks schemas are valid and $id matches the URL; not published
|-- assets/
|   |-- css/
|   |   `-- style.scss                         phase 2   optional small style overrides
|   `-- img/                                   phase 2   approved logo and images only (no photos of people)
`-- .github/
    `-- workflows/
        `-- validate-schemas.yml               phase 1   runs the schema check on every change

Not created (decision pending, see section 11):
    LICENSE                                              reuse terms for the public repository
    registry/                                            public copies of the three hierarchy CSV files
    CNAME                                                only if a custom domain is ever used

Must never exist in this repository:
    .nojekyll                                            would switch off the page builder and break the theme
```

### 4.1 Folder purposes

| Folder or file | Purpose | Public on the site |
|---|---|---|
| Root `.md` documents | Repository documentation | No (excluded in `_config.yml`) |
| `_config.yml` | Site title, description, theme, exclude list | No |
| `about/`, `structure/`, `glossary/`, `standards/` | Public information pages | Yes |
| `schemas/` | Public schemas at stable URLs | Yes |
| `tools/` | Maintenance scripts | No (excluded) |
| `assets/` | Style and images | Yes |
| `.github/workflows/` | Automation | No (folders that start with a dot are not published) |

## 5. File specifications

### 5.1 `_config.yml` (phase 1)

```yaml
title: Community Partners International (CPI)
description: Public site and standards files of the CPINTL GitHub organization
url: "https://cpintl-org.github.io"
baseurl: ""
lang: en
theme: jekyll-theme-minimal
exclude:
  - README.md
  - BLUEPRINT.md
  - CHANGELOG.md
  - tools/
```

Notes:

- `jekyll-theme-minimal` is one of the themes GitHub Pages supports without extra setup. Confirm it still builds on the first publish.
- The `exclude` list keeps repository documents and tools out of the published site.

### 5.2 Page front matter (every `.md` page)

```yaml
---
layout: default
title: Page Title
---
```

A Markdown file without this block is copied as a plain file and is not turned into a web page.

### 5.3 `index.md`, `404.md`, `schemas/index.md` (phase 1)

| File | Content |
|---|---|
| `index.md` | Title, one approved mission sentence, three links (Schemas, Structure when it exists, Glossary when it exists), a short note that the site shows role titles only. |
| `404.md` | Front matter with `permalink: /404.html`, a one-line message, a link to the home page. |
| `schemas/index.md` | A table of the three schemas with name, purpose and URL, the stability rule (section 8), and a one-line explanation of how to validate a CSV row against a schema. |

### 5.4 `tools/check_schemas.py` (phase 1)

Checks that every file named `*.schema.json` under `schemas/` is a valid Draft 2020-12 schema and that its `$id` equals the URL where Pages publishes it. Tested locally on the three current schemas (pass) and on a wrong `$id` (fail, as intended).

```python
"""Check that every JSON Schema in schemas/ is valid Draft 2020-12
and that its $id matches the URL where GitHub Pages publishes it."""
import json
import pathlib
import sys

from jsonschema import Draft202012Validator
from jsonschema.exceptions import SchemaError

BASE = "https://cpintl-org.github.io/"
problems = 0
files = sorted(pathlib.Path("schemas").rglob("*.schema.json"))
if not files:
    print("No schema files found in schemas/")
    sys.exit(1)
for f in files:
    schema = json.loads(f.read_text(encoding="utf-8"))
    try:
        Draft202012Validator.check_schema(schema)
    except SchemaError as e:
        print(f"{f}: invalid schema: {e.message[:120]}")
        problems += 1
        continue
    expected = BASE + f.as_posix()
    if schema.get("$id") != expected:
        print(f"{f}: $id is {schema.get('$id')} but expected {expected}")
        problems += 1
    else:
        print(f"{f}: OK")
print("PASS" if not problems else f"FAIL ({problems} problems)")
sys.exit(1 if problems else 0)
```

### 5.5 `.github/workflows/validate-schemas.yml` (phase 1)

Runs the check above when anything under `schemas/` or `tools/` changes. It uses a virtual environment so it does not depend on how the runner's system Python is set up.

```yaml
name: validate-schemas

on:
  push:
    paths:
      - "schemas/**"
      - "tools/**"
  pull_request:
    paths:
      - "schemas/**"
      - "tools/**"

permissions:
  contents: read

jobs:
  schemas:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v7
      - name: Install jsonschema in a virtual environment
        run: |
          python3 -m venv .venv
          . .venv/bin/activate
          pip install jsonschema
      - name: Check schemas
        run: |
          . .venv/bin/activate
          python tools/check_schemas.py
```

Notes:

- GitHub Actions is free for public repositories.
- `actions/checkout` was at major version 7 (release 7.0.1) in July 2026. Check the current major version when you create the file. Version 7 changed the default behavior for the `pull_request_target` trigger; this workflow does not use that trigger.
- The YAML was parsed and the script steps were run locally. The workflow itself has not yet run on GitHub; the first run will confirm it.

### 5.6 `CHANGELOG.md` (phase 1)

Keep a Changelog layout: Added, Changed, Deprecated, Removed, Fixed. First entry: `0.1.0-draft.1`, the Phase 1 file set.

## 6. Publishing procedure (one time, web browser only)

1. Confirm the repository is named exactly `cpintl-org.github.io`, belongs to the organization `cpintl-org`, and is **public**. On the free plan, Pages works only from a public repository, and a published site is public.
2. Add the Phase 1 files from section 4. Use **Add file**, then **Upload files**, and drag the folders so the structure is kept, or create each file with **Create new file** and type the path (for example `schemas/index.md`).
3. Open **Settings**, then **Pages**. Under **Build and deployment**, set **Source** to **Deploy from a branch**, set the branch to the default branch (normally `main`) and the folder to `/ (root)`, and save.
4. Open the **Actions** tab. Wait for **pages build and deployment** to finish. The site address appears in **Settings**, then **Pages**.
5. If nothing publishes, check that an organization owner has not disabled Pages for the organization's repositories, and read the error in the **Actions** tab.

### 6.1 Verification checklist

- [ ] The home page loads at `https://cpintl-org.github.io/` over `https`.
- [ ] A made-up address shows the 404 page.
- [ ] Each of the three schema URLs loads and shows JSON text.
- [ ] `https://cpintl-org.github.io/README.html` and `.../BLUEPRINT.html` do not show the documents.
- [ ] The **validate-schemas** workflow run is green on the Actions tab.
- [ ] No file contains a personal name, financial figure, donor name or private link (section 7).

## 7. Public content rules

| Allowed | Never allowed |
|---|---|
| Role titles, department and unit names | Personal names of staff, partners or beneficiaries |
| Structure, definitions, glossary terms | Patient or beneficiary data |
| Schemas, patterns, allowed values | Staff personal details beyond role titles |
| Approved mission sentence | Financial figures, bank details, donor names, funding percentages, donor agreements |
| Public links to published material | Passwords, tokens, keys, private links |

Before every merge, read the changed files for these items. Images must not show identifiable people unless a separate written decision allows it.

## 8. Schema publication policy

1. The `$id` of each schema is its public URL. It never changes.
2. A published schema file is never renamed or removed.
3. Adding an optional property is a minor change: edit the file in place, note it in `CHANGELOG.md`.
4. A change that makes a previously valid record invalid is a breaking change: publish the new schema under `schemas/v2/` (then `v3/`, and so on) with an `$id` that includes that folder, and leave the old files in place. `tools/check_schemas.py` already accepts versioned folders and checks that the `$id` matches the path.
5. If a custom domain is ever used, the old `$id` URLs keep working only while the old address does. Plan that before switching.
6. The schemas describe one record converted from a CSV row (all values are strings). Rules that compare fields or rows are checked by the registry validation script, not by the schemas.

## 9. Governance and change control

- The organization owner approves every change before it is merged.
- Changes are made on a branch and merged by pull request. Merge is the approval record.
- Version the repository plan with Semantic Versioning, using `-draft.N` until approved, and record changes in `CHANGELOG.md`.
- Branch protection or rulesets for a public repository on the free plan can be added later; check the options in repository **Settings** before relying on them.
- Review this blueprint when a phase completes or when GitHub changes how Pages works.

## 10. Phases

| Phase | Content | Exit condition |
|---|---|---|
| 1 | Launch set: documents, config, home, 404, schemas, check, workflow | Section 6.1 checklist all ticked |
| 2 | Public information pages and assets | Owner approves each page; section 7 read for each |
| 3 | Optional: registry copies, license, custom domain | Decisions in section 11 made |

## 11. Open decisions

| ID | Decision | Default until decided |
|---|---|---|
| D-01 | Approved mission sentence for the home page and about page. The README uses a sentence based on the organization overview file; confirm or replace it. | Use the README sentence |
| D-02 | License for the public repository | None chosen; no reuse rights granted |
| D-03 | Are the three hierarchy CSV files published here (`registry/`) or kept private? | Keep private |
| D-04 | Custom domain | Not used; `github.io` address only |
| D-05 | Logo and images | None until approved |
| D-06 | Public statement of what the standards repositories are for | Listed as "standards repository, purpose to be defined" |
| D-07 | Branch protection or rulesets on the default branch | Not set; changes reviewed by pull request |

## 12. Verification record

Checked in this session (October 2026): organization sites must be in a repository named `<organization>.github.io`; on GitHub Free for organizations Pages needs a public repository and published sites are public; organization owners can disable Pages; `jekyll-theme-minimal` is a supported built-in theme; `exclude` in `_config.yml` keeps files out of the build; `actions/checkout` major version 7 current as of July 2026.

Tested locally: the schema check script (pass on current schemas, fail on a wrong `$id` and on a `$id` that does not match a versioned folder), the workflow's YAML syntax, and the install-and-run steps in a virtual environment.

Not tested: the workflow on GitHub, the Pages build, and the live URLs. Run the checklist in section 6.1 after publishing.

---

> [!NOTE]
> This GitHub organization is **unofficial**. It is maintained voluntarily by a single person. Nothing here represents the business, terms, conditions, or policy of Community Partners International (CPI) at any scale.

<div align="center">

<sub>**CPI Bangladesh Mission** · **Health Program**</sub>

</div>
