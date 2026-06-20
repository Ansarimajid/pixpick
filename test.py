# import sys
# sys.path.insert(0, '.')  # run from the pixpick parent directory

# import cv2
# import urllib.request
# import numpy as np
# import pixpick
# from pixpick.selectors.box import SelectionCancelled

# # ------------------------------------------------------------------
# # 1. Load image — swap this path with any image on your machine
# # ------------------------------------------------------------------

# # Option A: download a sample image
# # url = "https://ultralytics.com/images/bus.jpg"
# # resp = urllib.request.urlopen(url)
# # img_array = np.frombuffer(resp.read(), dtype=np.uint8)
# # image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
# # cv2.imwrite("test_image.jpg", image)
# source = r"c:\Users\khans\Downloads\ChatGPT Image Jun 4, 2026, 07_00_01 PM.png"
# # Option B: use a local path directly
# # source = "/path/to/your/image.jpg"

# # ------------------------------------------------------------------
# # 2. Interactive selection
# # ------------------------------------------------------------------

# print("Window will open — drag a box, release mouse to confirm, Esc to cancel.\n")

# try:
#     region = pixpick.box(source)
# except SelectionCancelled:
#     print("Selection cancelled.")
#     sys.exit(0)

# # ------------------------------------------------------------------
# # 3. Inspect the selection
# # ------------------------------------------------------------------

# print("=" * 40)
# print(f"Box       : {region}")
# print(f"xyxy      : {region.xyxy}")
# print(f"xywh      : {region.xywh}")
# print(f"cxcywh    : {[round(v, 2) for v in region.cxcywh]}")
# print(f"normalized: {[round(v, 4) for v in region.normalized]}")
# print(f"center    : {region.center}")
# print(f"area      : {region.area} px²")

# # ------------------------------------------------------------------
# # 4. Adapter outputs
# # ------------------------------------------------------------------

# print("\n--- Adapter outputs ---")
# print(f"to_yolo()      : {region.to_yolo()}")
# print(f"to_raw() keys  : {list(region.to_raw().keys())}")

# # ------------------------------------------------------------------
# # 5. Visualise selection drawn on the image
# # ------------------------------------------------------------------

# vis = region.visualize(image)
# cv2.imshow("pixpick — result", vis)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # ------------------------------------------------------------------
# # 6. Save and reload
# # ------------------------------------------------------------------

# region.save("selection.json")
# print("\nSaved to selection.json")

# reloaded = pixpick.load("selection.json")
# print(f"Reloaded  : {reloaded}")
# assert reloaded.xyxy == region.xyxy
# print("Round-trip: OK")











import cv2
import pixpick

# select ROI interactively
region = pixpick.box(r"c:\Users\khans\Downloads\ChatGPT Image Jun 4, 2026, 07_00_01 PM.png")

print("\n=== RAW ===")
print(region.to_raw())

print("\n=== XYXY ===")
print(region.xyxy)

print("\n=== XYWH ===")
print(region.xywh)

print("\n=== NORMALIZED ===")
print(region.normalized)

print("\n=== YOLO ===")
print(region.to_yolo())

print("\n=== CENTER ===")
print(region.center)

print("\n=== AREA ===")
print(region.area)

# save
region.save("roi.json")

# load
loaded = pixpick.load("roi.json")

print("\n=== LOADED ===")
print(loaded)

# visualize
img = cv2.imread(r"c:\Users\khans\Downloads\ChatGPT Image Jun 4, 2026, 07_00_01 PM.png")
vis = loaded.visualize(img)

cv2.imshow("Selection", vis)
cv2.waitKey(0)
cv2.destroyAllWindows()










