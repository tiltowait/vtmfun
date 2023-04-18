"""Logic for the sidebar component."""

from __future__ import annotations

import pynecone as pc


def sidebar(current_page: str):
    from vtmfun.pages import routes

    pages = []
    for route in routes:
        if route.title == current_page:
            pages.append(pc.text(route.title, as_="b"))
        else:
            pages.append(pc.link(route.title, href=route.path))

    return pc.box(
        pc.hstack(
            pc.image(src="favicon.ico"),
            pc.heading("VtM Utils"),
        ),
        pc.spacer(),
        pc.hstack(pc.text("Pages:", as_="u"), *pages, padding_left="0.75em"),
        width="100%",
        top="0px",
        z_index="5",
    )
