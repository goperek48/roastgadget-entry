"""One-Line Roast: The Gadget You Use Every Day — entry program.

Writes one original one-line roast to /output/entry.txt.

The roast targets the gadget I reach for every day — my AirPods.
On their own they hold a charge for hours, but the moment I'm
actually on a call the left bud gives up at minute eleven, so every
meeting ends with me sounding like I'm being kidnapped mid-sentence.
The joke is the betrayal with a stopwatch: four hours of battery
until anyone is listening, eleven minutes once they are.
"""

from pathlib import Path

ROAST = (
    "My AirPods last four hours \u2014 unless I'm on a call, when the left "
    "one quits at minute eleven and every meeting ends with me sounding "
    "kidnapped."
)

OUTPUT_PATH = Path("/output/entry.txt")


def prepare_roast(text: str) -> str:
    """Collapse stray whitespace and enforce the gate's shape rules.

    The gate accepts UTF-8 text of 1 to 200 characters that is not only
    white space, and the bounty asks for a single line, so the roast is
    normalised to one line and measured before anything is written.
    """
    roast = " ".join(text.split())
    if "\n" in roast or "\r" in roast:
        raise ValueError("roast must be a single line")
    if not 1 <= len(roast) <= 200:
        raise ValueError(f"roast must be 1-200 chars, got {len(roast)}")
    return roast


def main() -> None:
    roast = prepare_roast(ROAST)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(roast, encoding="utf-8")
    print(f"Wrote one-line roast ({len(roast)} chars) to {OUTPUT_PATH}")
    print(roast)


if __name__ == "__main__":
    main()
