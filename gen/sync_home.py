#!/usr/bin/env python3
"""Put the shared header and shared CSS into the homepage (Home-B2.dc.html),
which is edited directly rather than generated."""
import pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from chrome import header, SHARED_CSS

home = pathlib.Path(__file__).parent.parent / 'project' / 'Home-B2.dc.html'
s = home.read_text()
s = re.sub(r'<header\b[^>]*>.*?</header>', lambda m: header(None, home=True), s, count=1, flags=re.S)
s = re.sub(r'\n?/\*shared:start\*/.*?/\*shared:end\*/\n?', '\n', s, flags=re.S)
s = s.replace('</style>\n</helmet>', SHARED_CSS.strip('\n') + '\n</style>\n</helmet>', 1)
home.write_text(s)
print('synced', home.name, len(s))
