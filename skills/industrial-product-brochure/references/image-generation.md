# Image Generation Notes

Use image generation carefully in industrial brochures. The goal is not to create impressive images; it is to support product truth and buyer recognition.

## Safe Uses

Use image generation for:

- no-brand product samples;
- photo-like application examples;
- clean backgrounds for covers;
- controlled visual exploration;
- process effect samples when the machine identity is protected by locked assets.

## Design First, Prompt Second

Do not use a long prompt as a substitute for design thinking. First decide the page role, visual hierarchy, product scale, grid, evidence, and catalog tone. Then write a compact prompt for the parts that should be generated.

Separate:

- exact text, model names, and specifications;
- locked product assets;
- generated sample or background prompt;
- deterministic overlay or layout instructions.

This prevents the prompt from becoming a checklist that technically includes many constraints while still producing a weak brochure page.

## Risky Uses

Avoid free generation for:

- exact machinery structure;
- model comparison pages;
- control panels with readable labels;
- precise technical diagrams;
- pages with many exact bilingual text items;
- any page where wrong geometry would mislead the buyer.

## Prompt Pattern for Product Samples

Use concise prompts that specify object, material, processing effect, lighting, background, and branding limits.

```text
Photorealistic studio product photo of [object type], [material/color],
with [heat transfer / hot stamping / metallic logo / wraparound pattern] on [surface],
clean white catalog background, soft studio lighting, no brand name, no readable text,
no hands, no people, no extra props, industrial catalog sample image.
```

Examples:

```text
Photorealistic studio product photo of several cylindrical cosmetic packaging tubes,
matte black and white plastic, with subtle gold hot-stamped curved lines on the side,
clean white catalog background, soft studio lighting, no brand name, no readable text.
```

```text
Photorealistic studio product photo of flat plastic caps and a small plastic box lid,
with a simple metallic foil logo mark on the flat top surface,
clean white catalog background, no brand name, no readable text.
```

## Generated Asset Discipline

After generating a sample:

1. Save it into the page allowed-assets folder.
2. Record which model/application it supports.
3. Keep it no-brand unless the user supplies branding.
4. Check that it does not imply unsupported materials, shapes, sizes, or capacities.
5. Do not let samples become more important than the machine on product pages.

## Full-Page Generation

If using a full-page image model:

- list exact text before generation;
- reduce small text density;
- prepare a compact design brief instead of a giant rule dump;
- use the approved logo asset when possible;
- inspect for typo, logo drift, model mismatch, false mechanisms, and missing parts;
- regenerate or switch to deterministic layout when correctness fails.
