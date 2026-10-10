# Print and Prepress Notes

Use these notes when preparing industrial brochure pages for print.

## A4 Basics

- Trim size: 210 x 297 mm.
- Portrait ratio: about 0.707.
- 300 DPI A4 raster: 2480 x 3508 px.
- 2400 x 3392 px is close to A4 and about 290 DPI.
- 3 mm bleed canvas: about 216 x 303 mm, or roughly 2552 x 3580 px at 300 DPI.

## Safe Zones

- Keep important text, logos, model names, and contact details at least 5 mm inside trim.
- Use 10-15 mm near binding when possible.
- Do not place critical details at the outer edge unless a bleed layout is deliberately prepared.

## Type Size

- Body/spec text should generally be 9 pt or larger.
- Dense specification pages may use smaller text only if the user accepts reduced readability.
- If the user finds a page hard to read at A4 size, enlarge and reflow rather than blaming screen resolution.

## Bleed

If the print shop requires full-bleed trimming:

1. Ask for required bleed, usually 3 mm.
2. Create a bleed canvas.
3. Extend backgrounds/accent shapes beyond trim.
4. Keep important content inside the trim safe zone.
5. Export both bleed-ready and preview/trim versions if useful.

Do not fake bleed by blindly scaling the finished A4 page; it may crop text, page numbers, or contact details.

## PDF Delivery

For image-based brochure pages:

- Create one A4 PDF with pages in order.
- Preserve the approved page images.
- Do not let the print shop guess page order from loose files.
- If color is important, request a physical proof.
- If any approved page image changes after PDF export, the previous PDF is stale and must be regenerated.

## Color

Many AI/image workflows produce RGB files. For local digital print, a print shop may prefer to convert using its own device profile. Do not casually convert to CMYK unless you know the target profile; brand red can become dull or dirty.

Include a note:

```text
Current files are RGB page images composed into an A4 PDF. Please convert according to your press/profile and provide a proof for color confirmation.
```

## Delivery Package

A practical print-shop package includes:

- `brochure_A4_preview.pdf`
- `brochure_original_pages.zip`
- `print_instructions.txt`
- `page_audit.txt`

The instruction file should state:

- final size;
- page count;
- cover/back cover;
- page order;
- scaling rule;
- bleed status;
- proofing request;
- color caution.

## Final-Stage Revisions

Small changes near delivery can create visible artifacts:

- Do not cover old page numbers, marks, or logos with a plain block unless the background is truly uniform.
- Match local background color, gradient, texture, and anti-aliasing.
- Keep a backup before overwriting final page images.
- Re-run page audit and PDF export after the repair.
