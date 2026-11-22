# Scripts

## `hello_world.py`

Minimal runnable entrypoint that prints a greeting.

### Usage

```bash
./scripts/hello_world.py
```

or:

```bash
python3 scripts/hello_world.py
```

Expected output:

```
Hello, World!
```

The script requires only Python 3.12+ (no external dependencies).

### Smoke test

```bash
python3 -m unittest discover -s tests -v
```
