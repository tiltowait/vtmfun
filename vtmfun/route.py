"""Manage routing for the application."""

import inspect
from typing import Callable

import pynecone as pc
from pynecone.base import Base


class Route(Base):
    """A page route."""

    path: str  # The route's path
    title: str | None = None  # The page's title

    # The component to render for the route
    component: pc.Component | Callable[[], pc.Component]


def get_path(component_fn: Callable):
    """Get the path for a page based on the file location."""
    module = inspect.getmodule(component_fn)
    return module.__name__.replace(".", "/").replace("_", "-").split("vtmfun/pages")[1]
