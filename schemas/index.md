---
layout: default
title: Schemas
---

# Schemas

These files are the public rules (JSON Schemas) for the three CPINTL hierarchy registry files. Each web address below is also the schema's official identifier, so it must always keep working.

| Schema | What it checks | Address |
|---|---|---|
| Node | One row of the nodes file (a place in the structure) | [hierarchy-node.schema.json]({{ '/schemas/hierarchy-node.schema.json' | relative_url }}) |
| Position | One row of the positions file (a role seat, never a person) | [hierarchy-position.schema.json]({{ '/schemas/hierarchy-position.schema.json' | relative_url }}) |
| Relation | One row of the relations file (a link between two rows) | [hierarchy-relation.schema.json]({{ '/schemas/hierarchy-relation.schema.json' | relative_url }}) |

## Stability rule

Published schema files are never renamed or removed. A change that would make a valid record invalid is published in a new versioned folder (for example `schemas/v2/`), and the old files stay in place.

## How to check a row

Each registry file row is first turned into a record where every value is text, and empty cells are empty text. The record is then checked against the matching schema using any tool that supports JSON Schema Draft 2020-12.
