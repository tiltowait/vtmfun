from typing import Callable

import pynecone as pc
from vtmfun.components import sidebar
from vtmfun.route import Route

DEFAULT_TITLE = "Vampire: The Masquerade PbP Utilities"


def webpage(path: str, title=DEFAULT_TITLE, props=None) -> Callable:
    """A template for webpages to use. Wraps the page with a sidebar."""

    props = props or {}

    def webpage(contents: Callable[[], Route]) -> Route:
        """Wrapper to create a templated route."""

        def wrapper(*children, **props) -> pc.Component:
            """The template component."""

            return pc.vstack(
                sidebar(title),
                pc.spacer(),
                contents(*children, **props),
                **props,
            )

        return Route(path=path, title=title, component=wrapper)

    return webpage
