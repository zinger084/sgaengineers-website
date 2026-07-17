# Site themes

## Active now (preview / Vercel candidate)

**Light / hybrid** via `css/styles.css`

- Warm off-white paper (`#f5f4f1`) for body and soft sections
- White cards, soft shadows, brand orange `#B62C00` and blue `#0077C8`
- **Still dark:** homepage hero photo overlays, inner page heroes, film panels, CTA bands, contact side panel, footer
- Header: dark logo on light bar; invert logo over transparent dark heroes

## Dark theme (remembered / full backup)

**Full original dark stylesheet:** `css/styles-dark.css`

This is the dark theme Jared approved (dark paper, dark nav, etc.). Do not delete it.

### Restore dark theme as the live site

1. In the edit folder (`sgaengineers-website`):

```powershell
cd "C:\Users\JaredSinger\OneDrive - SGA ENGINEERS\Documents\.grok\bin\sgaengineers-website\css"
Copy-Item styles.css styles-light.css -Force   # optional: keep light as a named backup
Copy-Item styles-dark.css styles.css -Force
```

2. Optionally switch header logos back to invert-only and `theme-color` to `#0a0a0a` (dark CSS still works with dual logos).
3. Publish only when Jared says yes (playground → GitHub main → Vercel).

### Restore light / hybrid again

```powershell
Copy-Item styles-light.css styles.css -Force
# or rebuild from this session's light styles if styles-light was not saved
```

## Brand constants (both themes)

- Orange `#B62C00`
- Gray `#BFBFBF`
- Blue `#0077C8`
- Font: Candara
- Tagline: Design with Integrity.
