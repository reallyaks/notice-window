# notice-window

Lists notice windows in a plain-text contract: `30 days' prior written notice`, `10 business days' notice`.

Not legal advice. It does not decide if a window is enforceable, and it ignores a cure period that never uses the word notice.

## Run

```bash
python -m notice_window samples/contract.txt --out /tmp/notices.md
python -m unittest discover -s tests
```

The sample result is already in [samples/notices.md](samples/notices.md). Python 3.10+. No packages.
