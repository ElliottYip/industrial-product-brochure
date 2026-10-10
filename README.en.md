# Industrial Product Brochure

Turn equipment photos, model information and technical specifications into clear, consistent product brochures, from single product pages to multi-model catalogs and print handoff.

[中文](README.md) · **English**

Maintained and refined by Yilun Ye through practical project work. Existing source notices and licenses remain attached to the relevant material; see [NOTICE](NOTICE.md).

## What it covers

- Match product photos with the correct models and specifications.
- Design layouts and bilingual copy around the product and its audience.
- Review accuracy, readability and physical print scale.
- Prepare page order, dimensions and print-shop instructions.

## Workflow

Asset review → Page plan → Design → Page review → Prepress → Handoff

## Get started

Install the dependencies below, then copy the skill folders. Back up existing skills with matching names, and keep suite members as siblings.

```bash
git clone https://github.com/ElliottYip/industrial-product-brochure.git
cd industrial-product-brochure
mkdir -p ~/.codex/skills
cp -R skills/* ~/.codex/skills/
```

Start a new session and try:

```text
Use $industrial-product-brochure to plan an A4 catalog from the supplied equipment photos and specifications. Start with an asset map and one preview page before expanding the catalog.
```

## Requirements

An agent with file tools. Page audits require Python 3.10+ and Pillow; image editing, PDF export and visual review use the tools available in your host.

[Configuration and checks](docs/USAGE.md)

## Included skills

- [industrial-product-brochure](skills/industrial-product-brochure/SKILL.md)

examples/ contains editable task briefs; docs/ records setup, validation and snapshot provenance.

## Current version

Retains the existing 1.0.0 baseline and current local content, including the original changelog and MIT license. The workflow captures asset mapping, layout review, product scale and print-handoff practices.

[Packaging notes](CHANGELOG.md) · [Verification](docs/VERIFICATION.md)

## Scope

This is a workflow with audit tools, not a one-command layout engine. Specifications must come from source material, and final print approval remains a separate step.
