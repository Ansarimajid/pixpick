# Contributing
We welcome contributions! Please open a GitHub issue or submit a pull request. For major changes, please open an issue first to discuss what you would like to change then submit a pull request.

Below are some guidelines for contributing to the project.

## Adding a new selector type (e.g. Line)

1. Add `Line` dataclass to `core/selection.py` with properties and adapter methods.
2. Add `select_line()` to `BaseBackend` and implement it in `CV2Backend`.
3. Create `selectors/line.py` with `LineSelector` — mirrors `BoxSelector` exactly.
4. Add `pixpick.line()` to `__init__.py`.

No other files change.

## Adding a new framework method or adapter

Add a method directly to the relevant class in `core/selection.py`.

```python
# eg. in Box
def detectron2(self) -> dict:
    return {"bbox": self.xyxy, "bbox_mode": BoxMode.XYXY_ABS}

# eg. in Multibox
def detectron2(self) -> list[dict]:
    return [{"bbox": box.xyxy, "bbox_mode": BoxMode.XYXY_ABS} for box in self.boxes]

# eg. multibox property
@property
def xyxy(self) -> list[int]:
    """[x1, y1, x2, y2] — absolute pixels for each box in boxes."""
    return self.boxes

```

That's it.
