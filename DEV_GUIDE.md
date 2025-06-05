# Developer Guide

## How to Add a New Function

1. Go to `libs/` and create your new module or add a function to an existing one.
2. Make sure the function takes a list of arguments: `def my_func(args):`
3. Import and register it in `core/stdlib.py` under `AVAILABLE_FUNCTIONS`.

## Example Function

```python
def double(args):
    return args[0] * 2

AVAILABLE_FUNCTIONS = {
    "double": double
}
```

## How It Works

- Variables are stored in a dictionary.
- Lines are read one by one and parsed.
- Function names are matched from `AVAILABLE_FUNCTIONS`.
