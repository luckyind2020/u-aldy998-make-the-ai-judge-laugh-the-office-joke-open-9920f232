"""Print the one-line office joke stored in entry.txt."""

from pathlib import Path


def load_joke() -> str:
    text = Path(__file__).with_name("entry.txt").read_text(encoding="utf-8")
    joke = text.strip()
    if len(joke) > 200:
        raise ValueError("office joke must fit in one line of 200 characters")
    return joke


def main() -> None:
    print(load_joke())


if __name__ == "__main__":
    main()
