# SGA ENGINEERS - Website Redesign

A modern, multi-page redesign of [sgaengineers.com](https://www.sgaengineers.com/), a formal multi-page redesign for a professional MEP consulting firm.

## Pages

| File | Content |
|------|---------|
| `index.html` | Home - hero, services, pillars, selected work, markets preview, CTA |
| `expertise.html` | Full MEPFT + commissioning capability lists |
| `markets.html` | Market sectors & positioning |
| `projects.html` | Selected work - anonymized project writeups (no client names) |
| `about.html` | Why SGA, mission/vision, leadership bios |
| `careers.html` | Culture, perks, open roles & co-op |
| `contact.html` | Contact info + inquiry form (mailto) |

## Preview locally

Double-click `index.html`, or from this folder:

```powershell
# Python (if installed)
python -m http.server 8080
```

Then open `http://localhost:8080`.

## Design notes

- **Typography:** Candara site-wide
- **Brand palette** (from `Logo Color Number.txt` + marketing blue):
 - Orange `#B62C00` (primary CTAs, accents)
 - Gray `#BFBFBF` (brand gray, eyebrows, borders)
 - Bright blue `#0077C8` (nav active, links, secondary buttons)
 - Charcoal / light gray neutrals for a formal professional look
- **Logo (site-wide):** `assets/logo/logo-primary-invert.png` (close-crop invert wordmark)
- **Images:** SGA-owned only (logos, team headshots). No third-party stock photography. Brand CSS panels where photos are not available.
- **Form:** Client-side form opens email to `engineer@sgaengineers.com` (no backend required)

## Deploy options

1. **Netlify / Cloudflare Pages / Vercel** - drag the folder or connect a Git repo  
2. **Existing domain** - upload contents to your web host; point `sgaengineers.com` DNS when ready  
3. **Google Sites replacement** - export/host this static site instead of the current Google Sites stack  

## Conversion content (client-search oriented)

Homepage and key pages include copy aimed at people evaluating MEP firms:

- Who hires us (architects, owners, contractors)
- Outcomes / reasons to choose SGA
- Engagement process (connect → scope → design → build)
- FAQ for RFP-stage questions
- Market outcome blurbs and “when to bring us in” on Expertise
- Contact “what to include” checklist

## Project privacy

`projects.html` uses real SGA engagement experience rewritten without owner or facility names. Prefer that pattern for any new marketing copy.

## Suggested next steps

1. Optional: add **SGA-owned project photography** (anonymized as needed) - no stock / third-party copyrighted images  

2. Wire contact form to **Formspree**, **Netlify Forms**, or your CRM  
3. Add **office address / phone** if you want them public  
4. Optional: simple CMS (e.g. Astro + Markdown) when you want non-technical content edits  
5. Deploy when ready (Netlify / Cloudflare Pages / Vercel / existing host)  

## Content source

Copy and service lists were adapted from the live site as of the redesign build date. Review and update any credentials, openings, or market language before going live.
