"""Main module for VtMfun."""

import pynecone as pc
from vtmfun.base_state import State
from vtmfun.pages import routes

app = pc.App(state=State)

for route in routes:
    app.add_page(
        route.component,
        route.path,
        f"VtM Utils - {route.title}",
        description="Utilities for Vampire: The Masquerade play-by-post games.",
    )

app.compile()
