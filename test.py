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










