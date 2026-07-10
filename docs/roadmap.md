# Roadmap

## v0.1 — Core ✅

- Box selector, cv2 backend
- Polygon selector, cv2 backend
- Line selector, cv2 backend
- YOLO, SAM2, Supervision framework methods
- JSON persistence
- `pixpick.box()`, `pixpick.polygon()`, `pixpick.line()`, `pixpick.load()`

## v0.2 — More selectors + environments

- `Points` selector — click foreground/background points for SAM2
- `Perspective` selector — 4-corner pick for BEV `sv.ViewTransformer`
- `NotebookBackend` — Matplotlib-based, works in Jupyter and Colab
- `GradioBackend` — works on headless servers and SSH sessions

## v0.3 — Video + multi-selection

- `pixpick.multi_polygon()` — pick N zones in one pass
- Video scrubbar UI in cv2 backend

## v0.4 — Polish + CLI

- Zoom and pan in the cv2 window
- Selection validation warnings (degenerate polygon, box near image edge)
- CLI: `pixpick image.jpg --type box --save zone.json`
- More framework methods: Kornia, EasyOCR, Detectron2, Albumentations
