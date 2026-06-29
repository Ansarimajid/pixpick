## Adding a new selector type (e.g. Line)

1. Add `Line` dataclass to `core/selection.py` with properties and adapter methods.
2. Add `select_line()` to `BaseBackend` and implement it in `CV2Backend`.
3. Create `selectors/line.py` with `LineSelector` — mirrors `BoxSelector` exactly.
4. Add `pixpick.line()` to `__init__.py`.

No other files change.

## Adding a new framework method

Add a method directly to the relevant class in `core/selection.py`.

```python
# in Box
def to_detectron2(self) -> dict:
    return {"bbox": self.xyxy, "bbox_mode": BoxMode.XYXY_ABS}
```

That's it.
