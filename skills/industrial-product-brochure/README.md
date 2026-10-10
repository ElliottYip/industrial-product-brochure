# Industrial Product Brochure Skill

An agent skill for creating, revising, reviewing, and preparing print-ready industrial product brochures and machinery catalogs.

This skill was distilled from a real multi-page machinery brochure project where the hard parts were not "making pretty images"; they were asset truth, model-photo mapping, machine scale at A4, buyer communication, bilingual typography, approval discipline, and print-shop delivery.

The skill is designed for agent workflows that combine user-supplied product assets, deterministic layout/editing, optional image generation, and final print delivery.

## What It Helps With

- A4 machinery brochure pages
- Product hero pages
- Multi-model catalog pages
- Application/sample pages
- Covers and back covers
- Image-generation workflows with locked product assets
- Print-ready delivery packages

## Install

Copy this folder into your agent skills directory, for example:

```text
~/.codex/skills/industrial-product-brochure
```

or:

```text
~/.agents/skills/industrial-product-brochure
```

Then start a new agent session so the skill metadata is loaded.

## Trigger Examples

```text
I have photos for the next catalog page. Make a preview first.
```

```text
This page has four machines. Keep the model-photo mapping correct and make it A4 print-ready.
```

```text
The page looks good but the machines are too small for print.
```

```text
Prepare the approved brochure pages for a print shop.
```

## Core Ideas

1. Lock the user's assets before designing.
2. Write a manifest before visual production.
3. Design from the buyer's recognition path.
4. Write a compact design brief before prompting or laying out.
5. Choose a page role and layout archetype.
6. Keep real product images large enough for A4 inspection.
7. Use image generation only where it does not damage product truth.
8. Run an editor-style self-review before showing drafts.
9. Show previews before masters.
10. Package final delivery as PDF + original images + print instructions.

## Workflow at a Glance

```text
user assets
  -> allowed-assets folder
  -> manifest and asset/model mapping
  -> buyer-view design chain
  -> art direction and compact design brief
  -> preview with measured product scale
  -> editor review + sales gate + print gate
  -> user approval
  -> final master
  -> A4 PDF / ZIP / print instructions
```

## What Makes It Different

- It treats a brochure page as a sales communication object, not a poster.
- It measures the visible product body instead of counting white photo canvas.
- It separates truth, scale, communication, genre, art, and production failures during revisions.
- It discourages giant all-purpose prompts; design the page first, then use concise prompts or deterministic layout.
- It includes print-shop delivery habits: page order, A4 PDF, original images, bleed notes, and proofing instructions.

## Included Files

```text
industrial-product-brochure/
  SKILL.md
  README.md
  CHANGELOG.md
  LICENSE
  evals/evals.json
  references/
    design-review.md
    image-generation.md
    print-prepress.md
    project-lessons.md
  templates/
    page-manifest.md
    print-instructions.txt
  scripts/
    audit_pages.py
```

## Script

Audit image pages before print delivery:

```bash
python scripts/audit_pages.py /path/to/progress-folder --expected-pages 24
```

The script reports page order, pixel size, A4 ratio, approximate print DPI, and missing pages.

## Open Source Notes

This skill is intentionally generic. It should not require a specific brand, machine category, local folder path, image model, or design tool. If you adapt it for a company, keep company-specific facts in page manifests or project memory rather than hardcoding them into the skill.

## License

MIT.
