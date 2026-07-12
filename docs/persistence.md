# Persistence

Save selections to JSON and reload them. Useful when you pick a zone once and reuse it across runs — common in production pipelines that run against the same camera feed.

## Save

`Box` `Polygon` and `Line` have a `.save()` method.

```python
region = pixpick.box("frame.jpg")
region.save("selections/entry_zone.json")

zone = pixpick.polygon("frame.jpg")
zone.save("selections/count_zone.json")

line = pixpick.line("frame.jpg")
line.save("selections/line_zone.json")
```

## Load

`pixpick.load()` reads the `"type"` field from the JSON and returns the correct object — you don't need to know what was saved.

```python
selection = pixpick.load("selections/entry_zone.json")
# returns Box or Polygon depending on what was saved
```

If you know the type, you can load directly from the class:

```python
from pixpick.core.selection import Box, Polygon, Line

region = Box.load("entry_zone.json")
zone   = Polygon.load("count_zone.json")
line   = Line.load("line_zone.json")
```

## JSON schema

**Box**

```json
{
  "type": "box",
  "image_size": [1920, 1080],
  "coordinates": {
    "xyxy":       [120, 80, 640, 480],
    "xywh":       [120, 80, 520, 400],
    "normalized": [0.0625, 0.074, 0.333, 0.444]
  }
}
```

**Polygon**

```json
{
  "type": "polygon",
  "image_size": [1920, 1080],
  "coordinates": {
    "points":     [[100, 50], [400, 50], [400, 300], [100, 300]],
    "normalized": [[0.052, 0.046], [0.208, 0.046], [0.208, 0.278], [0.052, 0.278]]
  }
}
```

**Line**

```json
{
  "type": "line",
  "image_size": [1920, 1080],
  "coordinates": {
    " endpoints": [[100, 50], [400, 300]],
    "normalized": [[0.052, 0.046], [0.208, 0.278]]
  }
}
```

## Typical production pattern

Pick once interactively, save, then load on every subsequent run.

```python
import pixpick
from pathlib import Path

ZONE_FILE = "config/count_zone.json"

if Path(ZONE_FILE).exists():
    zone = pixpick.load(ZONE_FILE)
    print("Loaded saved zone.")
else:
    zone = pixpick.polygon("reference_frame.jpg")
    zone.save(ZONE_FILE)
    print("Zone saved.")

```
