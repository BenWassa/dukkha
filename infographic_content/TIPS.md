# Tips for generating infographics (NotebookLM / LLM use)

- Use the Markdown file as the content source. Provide the LLM with the corresponding images (from `context/original_html/`) when asking for a visual.
- Example prompt: "Create a single-slide infographic summarising the key points from `attention.md`. Include a simple diagram showing the Ping/Scroll Loop, a short title, 3-4 bullets with practical steps, and a color palette consistent with Project Dukkha. Return a JSON manifest describing layout and assets."
- If you want per-protocol infographics, include the protocol `.md` file plus any diagrams referenced in that protocol's HTML.
