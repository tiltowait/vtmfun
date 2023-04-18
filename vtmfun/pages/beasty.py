"""Main module for VtMfun."""

import pynecone as pc
from vtmfun.base_state import State
from vtmfun.templates import webpage


class State(State):
    text: str = ""
    beast: str = ""
    copied: bool = False

    @pc.var
    def copy_label(self) -> str:
        return "Copy to Clipboard" if not self.copied else "Copied!"

    @pc.var
    def copy_disabled(self) -> bool:
        return not self.beast

    @pc.var
    def copy_button_bg(self) -> str:
        return "green" if self.copied else "gray"

    def update_beast(self, new_text):
        self.text = new_text
        self.copied = False

        if not self.text:
            self.beast = ""
            return

        bold = False
        chars = []

        for char in self.text:
            if bold:
                chars.append(f"**{char}**")
            else:
                chars.append(char)
            bold = not bold

        self.beast = "*" + "".join(chars) + "*"

    def copy_clicked(self):
        self.copied = True


@webpage("/", "Beasty")
def beasty_page():
    return pc.vstack(
        pc.heading("Beasty"),
        pc.text("Represent mixed thoughts with Beast thoughts."),
        pc.text_area(
            on_change=State.update_beast, placeholder="Enter your Beast thoughts here ..."
        ),
        pc.spacer(),
        pc.text_area(value=State.beast, is_read_only=True),
        pc.spacer(),
        pc.copy_to_clipboard(
            pc.button(
                State.copy_label,
                on_click=State.copy_clicked,
                is_disabled=State.copy_disabled,
                color_scheme=State.copy_button_bg,
            ),
            text=State.beast,
        ),
        align_items="start",
    )
