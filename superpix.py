import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from skimage.color import rgb2gray
from skimage.filters import sobel
from skimage.segmentation import slic, quickshift, watershed
from skimage.segmentation import mark_boundaries
from skimage.util import img_as_float
 
f = Image.open("test.png")
f = np.asarray(f)
img = img_as_float(f[::2, ::2])
 
segments_slic = slic(img, n_segments=180, compactness=10, sigma=1, start_label=1)
segments_quick = quickshift(img, kernel_size=6, max_dist=100, ratio=0.5)
gradient = sobel(rgb2gray(img))
segments_watershed = watershed(gradient, markers=600)
 
print(f'SLIC number of segments: {len(np.unique(segments_slic))}')
print(f'Quickshift number of segments: {len(np.unique(segments_quick))}')
print(f'Watershed number of segments: {len(np.unique(segments_watershed))}')
 
fig, ax = plt.subplots(1, 3, figsize=(10, 10), sharex=True, sharey=True)
 
ax[0].imshow(mark_boundaries(img, segments_slic))
ax[0].set_title('SLIC')
ax[1].imshow(mark_boundaries(img, segments_quick))
ax[1].set_title('Quickshift')
ax[2].imshow(mark_boundaries(img, segments_watershed))
ax[2].set_title('Watershed')
 
for a in ax.ravel():
    a.set_axis_off()
 
plt.tight_layout()
plt.show()
