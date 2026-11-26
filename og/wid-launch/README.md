# What I'd Do: announcement template

`launch.html` is the editable source for What I'd Do announcement graphics.

| Format | URL hash | Size | Export |
| --- | --- | --- | --- |
| LinkedIn | `#portrait` | 1080 × 1350 | `export/what-id-do-launch_linkedin_1080x1350@2x.png` |
| X | `#wide` | 1600 × 900 | `export/what-id-do-launch_x_1600x900@2x.png` |

Each format also exports a 1x PNG at its native size.

## Reusing it for a new issue or event

1. Edit the two `.rel` blocks in `launch.html`. Each block has a date, a type and a headline. A guest block also has one short line.
2. Replace `guest.jpg` with the next guest's approved portrait. Use a square crop with the face centred.
3. Render the graphics:

   ```
   python3 -m http.server 8812 -d . &
   NODE_PATH=$(npm root -g) node render.js
   ```

The design uses the site's fonts (Space Grotesk and DM Sans, bundled locally in `fonts/`) and its colours: cream #FFF5D9, ink #111, orange #FF5A2A, dark teal #0E2A2E and mint #8FE3B0.
