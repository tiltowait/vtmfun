"""Long post splitter."""

import pynecone as pc
from vtmfun.templates import webpage


@webpage("/splitter", "Long post splitter")
def splitter_page():
    return pc.text("Empty!")
