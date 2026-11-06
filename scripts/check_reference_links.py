"""Check printed bibliography URLs and the actual URI annotations on those pages."""
import re
import sys
import unicodedata
from pathlib import Path

import pymupdf


def compact(text):
    return re.sub(r"\s+", "", unicodedata.normalize("NFKC", text))


def check(md):
    source = md.read_text(encoding="utf8")
    heading = re.search(r"^## (References|Referencias)[^\n]*", source, re.M)
    if not heading:
        raise ValueError(f"{md}: missing reference section")
    section = source[heading.end():]
    if re.search(r"<https?://[^>\s]+>[\w/%-]", section):
        raise ValueError(f"{md}: a reference URL continues beyond its closing delimiter")
    expected = re.findall(r"<(https?://[^>\s]+)>", section)
    if not expected:
        raise ValueError(f"{md}: no printed references")
    targets = []
    text = []
    started = False
    with pymupdf.open(md.with_suffix(".pdf")) as doc:
        for page in doc:
            top = 0
            if not started:
                hits = page.search_for(heading.group()[3:].strip())
                if not hits:
                    continue
                started = True
                top = hits[-1].y1
            text.append(page.get_text(clip=pymupdf.Rect(0, top, page.rect.width, page.rect.height)))
            for annotation in sorted(page.get_links(), key=lambda a: (a["from"].y0, a["from"].x0)):
                uri = annotation.get("uri", "")
                if annotation["from"].y1 > top and uri.startswith(("https://", "http://")):
                    targets.append(uri)
    printed = compact("".join(text))
    absent = [url for url in expected if compact(url) not in printed]
    # Wrapped URLs can carry one annotation per line, even across pages.
    def in_order(values):
        return [v for i, v in enumerate(values) if i == 0 or v != values[i - 1]]
    if absent or in_order(targets) != in_order(expected):
        raise ValueError(f"{md}: not printed={absent}; expected URIs={expected}; "
                         f"bibliography URIs in reading order={in_order(targets)}")
    return dict(status="PASS", count=len(expected), urls=expected,
                method="Printed bibliography text and exact external PDF URI annotations")


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        result = check(Path(arg))
        print(f"{arg}: {result['count']} references, printed text and URI targets PASS")
