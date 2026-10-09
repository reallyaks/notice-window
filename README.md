# notice-window

Lists notice windows in a plain-text contract: `30 days' prior written notice`, `10 business days' notice`.

A cure period that never uses the word notice is ignored. The tool does not decide whether the window is enforceable.

## Run

```bash
python -m notice_window samples/contract.txt --out /tmp/notices.md
python -m unittest discover -s tests
```

The sample result is already in [samples/notices.md](samples/notices.md). Python 3.10+. No packages.
