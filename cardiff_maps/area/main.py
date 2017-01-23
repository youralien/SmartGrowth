import sys
from skimage.io import imread
import numpy as np

if __name__ == "__main__":
    fn = sys.argv[1]
    im = imread(fn)
    # count alpha channel
    n_pixels_area = np.sum(im[:,:,3])/255
    # 127 * 124 white pixels for a kmsq
    n_pixels_kmsq = 15748.
    print n_pixels_area / n_pixels_kmsq
