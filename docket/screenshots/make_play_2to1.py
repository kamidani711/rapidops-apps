"""Convert the 1080x2400 renders to the 1080x2160 Play accepts.

Play caps a screenshot's long side at twice its short side. These are rendered at
1080x2400 (2.22:1) because that is the real device aspect, so they need adjusting.

Cropping is not an option: every render leaves only 49-134px of empty margin, well
short of the 240px that would have to come off. Squashing to 1080x2160 distorts the
type. So the whole frame is scaled to 972x2160 -- aspect intact, no content lost --
and the remaining 54px each side is filled by stretching the outermost pixel column.
The backgrounds are flat or vertically graded at the edges, so the fill is seamless.

Idempotent: anything already 1080x2160 is left alone.
"""
from PIL import Image
import glob
import os

TARGET_W, TARGET_H = 1080, 2160
# Anything in this folder that is not a phone screenshot. The glob is indiscriminate and the
# resize is destructive and in-place, so a non-screenshot that is not listed here gets silently
# stretched to 1080x2160 and overwritten -- which is exactly what happened to play_store_qr.png
# on 2026-09-07. A QR stretched 4:1 no longer scans, and the file was untracked, so there was
# nothing to restore from.
SKIP = ('feature_graphic', 'store_icon', 'play_store_qr')

for path in sorted(glob.glob(os.path.join(os.path.dirname(__file__), '*.png'))):
    name = os.path.basename(path)
    if any(s in name for s in SKIP):
        continue

    src = Image.open(path).convert('RGB')
    if src.size == (TARGET_W, TARGET_H):
        print('  %-34s already 2:1, skipped' % name)
        continue

    scaled_w = round(src.width * TARGET_H / src.height)
    scaled = src.resize((scaled_w, TARGET_H), Image.LANCZOS)

    out = Image.new('RGB', (TARGET_W, TARGET_H))
    left = (TARGET_W - scaled_w) // 2
    out.paste(scaled, (left, 0))

    # Stretch the edge columns outward rather than filling with a guessed colour,
    # so a vertical gradient at the edge continues cleanly into the fill.
    if left > 0:
        out.paste(scaled.crop((0, 0, 1, TARGET_H)).resize((left, TARGET_H)), (0, 0))
        right = TARGET_W - scaled_w - left
        out.paste(
            scaled.crop((scaled_w - 1, 0, scaled_w, TARGET_H)).resize((right, TARGET_H)),
            (left + scaled_w, 0),
        )

    out.save(path)
    print('  %-34s %dx%d -> %dx%d' % (name, src.width, src.height, TARGET_W, TARGET_H))
