def define_env(env):
    """Top-level macros entrypoint for mkdocs-macros-plugin.

    Mirrors the safe component macros used across the documentation.
    """

    def thesis_card(title="", takeaway="", refs=None):
        refs = refs or []
        ref_html = "" if not refs else "<div class='refs'>Refs: " + ", ".join(refs) + "</div>"
        return f"<div data-component='thesis-card'><h3>{title}</h3><p>{takeaway}</p>{ref_html}</div>"

    def caution_callout(heading="", body=""):
        return f"<div data-component='caution-callout'><strong>{heading}</strong><p>{body}</p></div>"

    def protocol_steps(steps=None):
        steps = steps or []
        lis = "".join([f"<li>{s}</li>" for s in steps])
        return f"<ol data-component='protocol-steps'>{lis}</ol>"

    def myth_science_pair(myth="", insight=""):
        return f"<div data-component='myth-science'><div class='myth'>{myth}</div><div class='insight'>{insight}</div></div>"

    def figure_with_caption(src="", caption="", id=""):
        return f"<figure id='{id}'><img src='{src}' alt='{caption}' /><figcaption>{caption}</figcaption></figure>"

    def glossary_term(term=""):
        return f"<span data-glossary='{term}'>{term}</span>"

    env.macro(thesis_card)
    env.macro(caution_callout)
    env.macro(protocol_steps)
    env.macro(myth_science_pair)
    env.macro(figure_with_caption)
    env.macro(glossary_term)
