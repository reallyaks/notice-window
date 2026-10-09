import argparse
from pathlib import Path

from notice_window.engine import find_notices, render


def main() -> None:
    parser = argparse.ArgumentParser(description="List notice windows in a plain-text contract.")
    parser.add_argument("contract")
    parser.add_argument("--out", default="notices.md")
    args = parser.parse_args()
    text = Path(args.contract).read_text()
    notices = find_notices(text)
    Path(args.out).write_text(render(notices, Path(args.contract).name))
    print(f"{args.out}: {len(notices)} notice windows")


if __name__ == "__main__":
    main()
