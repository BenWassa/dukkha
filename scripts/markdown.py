"""Minimal markdown converter used when package install is unavailable."""

import html


def markdown(text: str, extensions=None):
    lines = []
    for raw in text.splitlines():
        line = raw.rstrip()
        if not line:
            lines.append("<p></p>")
            continue
        if line.startswith('# '):
            lines.append(f"<h1>{html.escape(line[2:].strip())}</h1>")
        elif line.startswith('## '):
            lines.append(f"<h2>{html.escape(line[3:].strip())}</h2>")
        elif line.startswith('- '):
            lines.append(f"<li>{html.escape(line[2:].strip())}</li>")
        else:
            lines.append(f"<p>{html.escape(line)}</p>")

    html_lines = []
    in_list = False
    for l in lines:
        if l.startswith('<li>'):
            if not in_list:
                html_lines.append('<ul>')
                in_list = True
            html_lines.append(l)
        else:
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            html_lines.append(l)
    if in_list:
        html_lines.append('</ul>')

    return '\n'.join(html_lines)

