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

# cpintl-org.github.io

Public website and public standards files of the CPINTL GitHub organization, published with GitHub Pages at **https://cpintl-org.github.io/**.

Community Partners International (CPI) is a nonprofit that works to empower vulnerable communities in Asia to meet their essential health, humanitarian, and development needs.

> **Status:** draft for review. Version of this repository plan: `0.1.0-draft.2` (see `BLUEPRINT.md`).

## What this repository is for

This is the only place in the organization that serves public web pages. It holds:

- the public home page and a few public information pages;
- the public JSON Schemas that describe the CPINTL organizational hierarchy registry (nodes, positions, relations);
- a small check that keeps those schemas valid.

## What this repository never holds

The repository is public and so is the published site. Never add any of the following, in any file, image or commit message:

- personal names of staff, partners or beneficiaries (role titles only);
- patient or beneficiary data;
- staff personal details beyond role titles;
- financial figures, bank details, donor names, funding percentages or donor agreements;
- passwords, tokens, keys or private links.

Private working documents live in private repositories of the organization, not here.

## Public URLs

| What | URL |
|---|---|
| Home page | `https://cpintl-org.github.io/` |
| Schemas index | `https://cpintl-org.github.io/schemas/` |
| Node schema | `https://cpintl-org.github.io/schemas/hierarchy-node.schema.json` |
| Position schema | `https://cpintl-org.github.io/schemas/hierarchy-position.schema.json` |
| Relation schema | `https://cpintl-org.github.io/schemas/hierarchy-relation.schema.json` |

The schema URLs are the schemas' official identifiers (`$id`). They must keep working for as long as any registry refers to them.

## Repository layout (short)

```text
cpintl-org.github.io/
  README.md
  BLUEPRINT.md
  CHANGELOG.md
  _config.yml
  _layouts/
  _includes/
  index.md
  404.md
  about/
  structure/
  glossary/
  standards/
  schemas/
  tools/
  assets/
  .github/workflows/
```

The full tree, with the purpose and phase of every file, is in `BLUEPRINT.md`.

## How to publish or change something (web browser only)

You do not need Git or a command line.

1. Open this repository on GitHub and go to the folder you want to change.
2. To change a file, open it and select the pencil icon. To add files, select **Add file**, then **Create new file** or **Upload files**.
3. Choose **Create a new branch for this commit and start a pull request**, then open the pull request and merge it after you have read the changes.
4. Open the **Actions** tab. Wait for **pages build and deployment** to finish. The site updates after it succeeds.
5. Open the changed public URL in a browser and confirm it looks right.

The one-time setup (turning on GitHub Pages) is in `BLUEPRINT.md`, section 6.

## Rules for pages

- Every page file ends in `.md` and starts with a front matter block (`layout`, `title`). A page without front matter is not turned into a web page.
- File and folder names: lowercase English, hyphen-joined, no spaces, no `&` (write `and` or drop it). `README.md`, `BLUEPRINT.md` and `CHANGELOG.md` keep their conventional capital letters.
- Titles use Title Case and `and`, never `&`.
- Use role titles, never personal names.

## Schemas: stability rule

Published schema files are never renamed or removed. A change that would make a valid record invalid is published under a new versioned folder, for example `schemas/v2/`, and the old files stay in place. Details are in `BLUEPRINT.md`, section 8.

## License

No license has been chosen yet, so no reuse rights are granted beyond what GitHub's terms give to viewing and forking public repositories. The choice is listed in `BLUEPRINT.md`, section 11.

## Contact

Use the **Issues** tab of this repository. Do not post personal contact details.

## Related

The organization profile and shared community files (issue and pull request templates) live in the organization's `.github` repository.

---

> [!NOTE]
> This GitHub organization is **unofficial**. It is maintained voluntarily by a single person. Nothing here represents the business, terms, conditions, or policy of Community Partners International (CPI) at any scale.

<div align="center">

<sub>**CPI Bangladesh Mission** · **Health Program**</sub>

</div>
