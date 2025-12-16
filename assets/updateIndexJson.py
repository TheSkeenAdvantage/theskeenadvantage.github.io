#!/usr/bin/env python3
# Scans blog/posts/*.md and writes blog/posts/index.json
import re, json
from pathlib import Path
from datetime import datetime

RE_DATE_SLUG = re.compile(r'^(\d{4}-\d{2}-\d{2})-(.+)\.md$', re.IGNORECASE)

repo = Path(__file__).resolve().parents[1]
posts_dir = repo / 'blog' / 'posts'
out_file = posts_dir / 'index.json'

items = []
for md in sorted(posts_dir.glob('*.md')):
    name = md.stem  # filename without .md
    m = RE_DATE_SLUG.match(md.name)
    if m:
        date_str = m.group(1)
    else:
        # fallback to file modified date
        date_str = datetime.utcfromtimestamp(md.stat().st_mtime).strftime('%Y-%m-%d')
    title = None
    excerpt = None
    with md.open('r', encoding='utf-8') as fh:
        lines = [l.rstrip() for l in fh]
    # find first H1/line starting with '# '
    for i, line in enumerate(lines):
        if line.startswith('# '):
            title = line[2:].strip()
            # excerpt: first non-empty paragraph after title
            for p in lines[i+1:]:
                if p.strip():
                    excerpt = p.strip()
                    break
            break
    if not title:
        # fallback to nice name from filename
        title = name.replace('-', ' ').title()
    items.append({
        "slug": name,
        "title": title,
        "date": date_str,
        "excerpt": excerpt or ""
    })

# sort by date desc
items.sort(key=lambda x: x.get('date',''), reverse=True)

out_file.write_text(json.dumps(items, indent=2, ensure_ascii=False))
print(f"Wrote {len(items)} posts to {out_file}")