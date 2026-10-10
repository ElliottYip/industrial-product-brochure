---
name: industrial-product-brochure
description: Use whenever creating, revising, reviewing, or preparing print-ready industrial product brochures, machinery catalogs, A4 product pages, image-generation brochure pages, multi-model comparison pages, application/sample pages, covers, back covers, or print-shop delivery files. Trigger even if the user only says "make the next page" when product assets, model names, specifications, machinery photos, page approval, or print delivery are involved.
version: 1.0.0
---

# Industrial Product Brochure

Use this skill to turn product assets into commercially useful industrial brochure pages. Treat the work as print production and sales communication, not as a loose image prompt.

The page must satisfy four priorities, in order:

1. **Truth:** correct assets, models, names, parameters, logos, and user-approved facts.
2. **Buyer communication:** the page helps a potential customer recognize fit, compare options, trust the product, and inquire.
3. **Art direction:** the page has a deliberate visual posture, not just constraints.
4. **Print readiness:** the page survives A4 print, review, approval, master export, and delivery to a print shop.

## First Move

Before designing, identify the page role:

- **Product hero:** one machine/product must be inspected and trusted.
- **Series catalog:** several models need equal scanning.
- **Form-led comparison:** different machine shapes or motions explain the differences.
- **Application proof:** samples or processed products help the buyer recognize use cases.
- **Selection/comparison:** the buyer chooses by shape, range, or configuration.
- **Front cover:** brand/domain recognition and confidence.
- **Back cover:** closure, contact, company identity, restraint.
- **Print delivery:** packaging approved pages into PDF/ZIP/instructions for production.

Do not force one successful page template onto another role. A back cover, a comparison page, and a product hero page have different visual grammar.

## Page Workflow

Follow this sequence for each page:

1. Confirm page number, output stage, and user-designated asset folder/files.
2. Create a dedicated page work folder.
3. Copy only user-approved assets into the allowed-assets folder.
4. Write a page manifest before visual design.
5. Map each asset to model/name/application/role.
6. Run the buyer-view design chain.
7. Run the art-direction pass.
8. Write a compact design brief before prompting or laying out.
9. Choose a layout archetype and visual-mass plan.
10. Build a preview, not a master.
11. Measure print size and readability.
12. Run the editor review, aesthetic gate, and sales gate.
13. Show the preview ID and path.
14. Wait for explicit approval.
15. After approval, generate the master from the approved logic.
16. Verify dimensions and visual match.
17. For final delivery, create PDF/ZIP/print instructions and audit page order.

## Work Folder

Use a page-specific folder so assets cannot drift between pages:

```text
PROJECT_ROOT/
  P{page}_work/
    01_allowed_assets/
    02_previews/
    03_approved_master/
    04_rejected_archive/
    P{page}_manifest.md
```

If the user's project uses localized folder names, keep their convention. The important rule is one page, one locked asset set, one manifest.

## Manifest Template

Write this before designing. Keep it practical and page-specific. Use `templates/page-manifest.md` when creating a real project file.

```text
P{page} Manifest

Allowed assets:
- [file] = [model/name] = [role] = [application]

Required text:
- Page title:
- Models:
- Chinese names:
- English names:
- Applications:
- Provided parameters:
- Prohibited or unknown parameters:

Buyer-view design chain:
- Recognition object:
- Machine/product match:
- Range boundary:
- Trust mechanism:
- Inquiry hook:

Art direction:
- Page role:
- Layout archetype:
- Design brief:
- Visual hierarchy:
- Primary visual mass:
- Image treatment:
- Type rhythm:
- Accent budget:
- White-space strategy:
- Aesthetic risks:

Editor review:
- Self-reject reason:
- Revision layer:
- Proof needed before showing:

Print rules:
- Target size:
- Preview ID:
- Preview output path:
- Master output path:
- Approval rule:
```

## Buyer-View Design Chain

Build the page from the customer's likely recognition path, not from the manufacturer's urge to list every fact.

1. **Recognition object:** What product, shape, material, process, or pain point should the buyer recognize first?
2. **Product match:** Which machine, model, option, or service corresponds to that recognition object?
3. **Range boundary:** Which few maximum values or limits decide whether the buyer should inquire?
4. **Trust mechanism:** Which real structure, control method, sample, or process evidence proves the claim?
5. **Inquiry hook:** What concise sales point can a salesperson use when sending this page?

Keep this logic mostly inside the layout. Do not print guide-like copy such as "look here first, then choose this model" unless the user explicitly wants a selection guide.

## Art-Direction Pass

Run this before visual production. Record the compact result in the manifest.

Ask:

- What commercial role does this page play?
- What should stop a reader who is flipping quickly?
- Which machine/product/sample owns the first glance?
- Should the page be symmetrical, asymmetric, horizontal, vertical, table-led, or specimen-like?
- What image treatment protects product truth?
- What type rhythm works for the audience: Chinese-first bilingual, model-led, spec-led, caption-light?
- Where does the brand accent color do real work?
- What is the most likely failure: template fatigue, web-page feel, manual page, sample takeover, machine shrinkage, or decoration clutter?

Good art direction is not decoration. It is a decision that makes the product easier to inspect and sell.

## Design Brief Before Prompt

Before using an image model or visual design tool, translate the page into a short design brief. Think like a catalog designer first, then compress the instruction for the tool.

Use this structure:

```text
Role: [product hero / series catalog / application proof / cover / back cover / delivery]
Reader first glance: [machine / product shape / application / brand]
Main visual mass: [what owns the largest area, with approximate share]
Grid: [1-column hero / 2-band / 3-column / asymmetric / specimen strip]
Evidence: [machine photo / sample photo / mechanism / max range / option list]
Tone: [quiet technical / premium catalog / dense comparison / restrained corporate]
Do not do: [wrong assets / tiny machines / web hero / manual copy / decorative clutter]
```

If using image generation, turn the design brief into a concise prompt. Do not paste every rule into the prompt. Keep exact text, model names, and parameters as a separate checklist for post-generation inspection or deterministic overlay.

## Layout Archetypes

### Product Hero

Use for one main machine/product.

- The product should normally occupy 40-60% of the page's meaningful visual mass.
- Show critical structure clearly.
- Use short copy: model/name, application, 4-6 proof points, provided parameters.
- Samples support the machine; they must not replace it.

### Multi-Model Series

Use when several models need scanning.

- Lock image/model/name/application mapping before design.
- Prefer disciplined grids or bands over collage.
- Each model needs a clear landing point.
- If machines become too small at A4 size, simplify or split the page.

### Form-Led Comparison

Use when physical form or process motion explains the difference.

- Let long machines earn width; tall/rotary/feeder structures earn height.
- Use asymmetry only when it clarifies product logic.
- Do not force unlike machines into identical cards.

### Application Proof

Use when samples help recognition.

- Use supplied photos or photo-like generated samples.
- Keep samples no-brand and text-free unless the user provides branding.
- Pair samples with the related machine or model.
- Avoid schematic icons when the user expects product photography.

### Cover

Use for first recognition.

- Show brand/domain confidence.
- Avoid over-explaining.
- The first print glance must communicate the company or product domain.

### Corporate Back Cover

Use for closure and contact.

- Hierarchy usually: logo/company -> product scope or closing line -> contact -> small footer.
- Use generous white space and minimal geometry.
- Avoid product-page corner tabs, page numbers, model cards, spec cards, machine-photo blocks, and four-corner decoration.
- If the user rejects photo backgrounds, remove photo thinking entirely; do not replace it with noisy pseudo-corporate geometry.

## Production Method

### Deterministic Layout First

Use deterministic placement, cropping, and local layout code when:

- multiple machines/models appear;
- assets are visually similar;
- model-photo mapping must be exact;
- prior drafts had wrong assets;
- the page is a comparison, catalog, overview, or selection page.

This prevents image models from swapping machines, redrawing structures, or inventing details.

### Image Generation

Use image generation for:

- photo-like no-brand application samples;
- controlled aesthetic exploration;
- background/cover imagery when identity is not at risk;
- process effect samples when the machine identity is protected by locked assets.

Never invent specifications, mechanisms, brands, logos, certifications, capacities, or customer claims. Generated samples become assets: save them into the allowed-assets folder and record their role in the manifest.

### Full-Page Image Generation

Use cautiously. Full-page generation can be useful for simple heroes, but it can distort machines and text. Inspect for false mechanisms, wrong labels, missing parts, logo drift, and text errors. Switch back to deterministic layout when identity matters.

### Local Visual Repair

When revising an approved page or final delivery file, preserve the accepted layers. Repair only the failing surface unless the role or composition is fundamentally wrong.

- For page numbers, logos, small labels, and footer changes, use deterministic overlays.
- When clearing old graphics, sample or reconstruct the local background. Do not cover with plain white unless the local background is actually plain white.
- Do not let a repair rectangle, clone patch, or anti-alias fringe become visible at print size.
- Re-audit the touched area at the page's real aspect ratio and in a contact sheet with neighboring pages.
- If the fix changes page geometry, regenerate the audit and delivery PDF.

## Catalog Voice

Brochure copy should sound like a catalog or technical sales sheet, not a live shopping guide, tutorial, landing page, or internal design rationale.

Prefer factual labels:

- `Applications / 应用`
- `Sample Applications / 应用样品`
- `Processing Range / 加工范围`
- `Machine Features / 设备特点`
- `Configuration Options / 配置选项`
- `Max. Diameter / 最大直径`
- `Max. Area / 最大面积`

Avoid guide-like wording:

- "look at this first"
- "then choose this model"
- "ask the seller to confirm"
- "if you see this product..."

For mixed domestic and overseas audiences, use Chinese-first paired bilingual labels when appropriate, for example:

```text
最大直径 / Max. Dia.: 320 mm
加工范围 / Processing Range
应用样品 / Sample Applications
```

## Parameters

- Include only user-provided values.
- Mark maximum capacities as `最大` / `Max.`; do not treat them as fixed sizes.
- Do not invent voltage, air pressure, power, dimensions, speed, material range, or certifications.
- If a range is cautious or product-dependent, say so briefly rather than broadening the promise.

## Print Rules

- A4 portrait trim: 210 x 297 mm, ratio about 0.707.
- Common preview: about 1200 x 1696 px.
- High-quality raster master: 2400 x 3392 px or A4 300 DPI 2480 x 3508 px.
- Bleed-ready raster with 3 mm bleed: about 2552 x 3580 px; keep trim content centered.
- Keep logos, model names, parameters, page numbers, and contact details at least 5 mm inside trim; use 10-15 mm near binding when needed.
- Body/spec text should generally be 9 pt or larger in print.
- Judge previews at approximate A4 size, not only zoomed on screen.

## Machine Print-Size Gate

Before showing a preview with machinery/product photos:

1. Measure the visible product body, not the image canvas or card.
2. Convert pixels to print millimeters:
   - `printed_width_mm = visible_width_px / canvas_width_px * 210`
   - `printed_height_mm = visible_height_px / canvas_height_px * 297`
3. Record the result in the manifest or working notes.
4. Self-reject if catalog-subject machines print as thumbnails.

Practical thresholds:

- Single product hero: important structures should be inspectable and usually own 40-60% of meaningful visual mass.
- Primary machine in multi-model page: aim for at least 70 mm on the meaningful long dimension.
- Secondary catalog machine: aim for at least 45 mm on the meaningful short dimension and 60 mm on the meaningful long dimension.
- Four-or-more-machine pages: if thresholds cannot be met, simplify or split the page.

White machine backgrounds do not count as product area.

## Aesthetic Gate

Before showing a preview, self-review:

- **Role fitness:** Does the page unmistakably match its role?
- **Hierarchy:** Can the reader tell what to inspect first, second, and third?
- **Specificity:** Does the design come from this product and its application, or from a generic template?
- **Execution:** Are margins, columns, type sizes, image boxes, and label positions stable for A4 print?
- **Restraint:** Does every accent, line, sample, and block earn its space?

If any answer is weak, revise before showing the user.

## Editor Review Loop

Act like a strict brochure editor before the user sees the draft. This is not a taste memo; it is a go/no-go gate.

Reject your own draft when:

- the page could be mistaken for a website hero, poster, manual page, or internal design rationale;
- the machine/product cannot be inspected at A4 size;
- samples, icons, or decoration steal the job of the product photo;
- the layout is balanced but commercially mute;
- bilingual type looks like a fallback rather than a deliberate catalog system;
- a cover/back cover uses product-page grammar;
- a tool or reference says the design is fine but the page role is still wrong.

When self-rejecting, name the failing layer, rebuild that layer, and keep any layer that already passed truth and user approval.

## Sales Gate

Review as a skeptical buyer:

- Can the buyer identify the category or application within 5 seconds?
- Does the page show what problem or product shape this solves?
- If multiple models appear, can the buyer tell why they differ?
- Are decisive maximum ranges easy to scan?
- Do real photos, samples, parameters, or mechanisms support trust?
- Is there a clear inquiry or sales talking point?

A page is not allowed to be only pretty. Every major block should support recognition, comparison, trust, or inquiry.

## Feedback Correction

When the user rejects a draft, classify the failure before changing it:

- truth failure: wrong asset/model/name/logo/parameter;
- scale failure: machine or text too small;
- material failure: samples look fake, schematic, or unrelated;
- communication failure: pretty but does not sell or explain value;
- copy-tone failure: guide/tutorial/ad wording;
- genre failure: manual, poster, or website instead of brochure;
- role failure: cover/back cover/product page grammar confused;
- reference laundering: using a design reference or tool output to excuse weak taste.

Correct only the failing layer when possible. If layout is accepted but copy is rejected, preserve the layout. If the user rejects basic taste or role fit, rebuild from the page role instead of polishing the same weak composition.

Use this repair ladder:

1. **Truth layer:** asset, model, logo, parameter, page order.
2. **Scale layer:** machine body size, readable text, A4 inspection.
3. **Communication layer:** recognition, differentiation, trust proof.
4. **Genre layer:** brochure vs web page, manual, poster, ad, or dashboard.
5. **Art layer:** hierarchy, spacing, typography, rhythm, restraint.
6. **Production layer:** export size, page number, background repair, PDF, ZIP.

Move up only as far as needed. Do not overcorrect one complaint into a different failure.

## Approval and Master Rules

- Always show a preview first.
- Give each preview a clear ID, such as `P8-C`.
- Do not create or overwrite the final master/progress file until the user explicitly approves the page/version.
- After approval, generate the master from the approved preview logic, not by loosely regenerating.
- Verify dimensions and visually compare the master against the approved preview.

## Print-Shop Delivery

When preparing final delivery:

- Verify all pages exist and are ordered.
- Create a combined A4 PDF.
- Provide original page images as a ZIP.
- Add a print instruction text file.
- State whether the files include bleed.
- Tell the print shop not to reorder pages or stretch images.
- Recommend a physical proof before batch printing, especially for brand red and small text.

Use `scripts/audit_pages.py` to check page count, A4 ratio, approximate DPI, and file sizes when image pages are available locally.

Use `templates/print-instructions.txt` as the starting point for the print-shop note, then fill in page count, bleed status, included files, and proofing requirements.

## Common Failures and Fixes

| Failure | Cause | Fix |
|---|---|---|
| Wrong assets | Nearby folders were used | Lock allowed assets per page |
| Model/photo mismatch | Image generation swapped similar machines | Use deterministic layout |
| Pretty but wrong | Design started before manifest | Map truth first |
| Correct but ugly | Constraints replaced art direction | Run the art-direction pass |
| Web-page feel | Landing-page composition dominates | Return to catalog structure |
| Machine too small | Text/samples/decorations consumed area | Enlarge, simplify, or split |
| White canvas counted as machine | Measuring the frame instead of product body | Measure visible body pixels |
| Page feels like manual | Selection logic over-explained | Use recognition visuals and factual labels |
| Max values look fixed | Missing `Max.` / `最大` | Label maximum/range values |
| Samples look cheap | Icons or sketches used as product evidence | Use real or photo-like samples |
| Chinese typography weak | Bad fallback font | Use deliberate CJK fonts |
| Back cover overdecorated | Product-page grammar reused | Use quiet logo/contact hierarchy |
| Tool says OK but page weak | Reference treated as approval | Self-reject and rebuild |
| Revision patch visible | Old mark was covered with a flat color | Repair with local background sampling or rebuild the layer |
| Prompt becomes a rule dump | Constraints were pasted instead of designed | Write a design brief, then compress the prompt |

## When More Detail Is Needed

Read only the relevant reference:

- `references/project-lessons.md` for distilled lessons from a real 24-page machinery brochure project.
- `references/design-review.md` for editor-style review, self-rejection, and revision triage.
- `references/print-prepress.md` for A4, bleed, PDF, ZIP, and print-shop delivery notes.
- `references/image-generation.md` for using image models without losing product truth.
