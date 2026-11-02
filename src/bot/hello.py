"""Hello helper module."""


class Hello:
    """Helper class for greeting messages."""

    def __init__(self):
        pass

    def print_message(self, text):
        """Print a message to the console."""
        print(text)

    def get_greeting(self, name="World"):
        """Return a formatted greeting message."""
        return f"Hello {name}"
