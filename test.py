import bet2
import nibabel as nib
import time
import numpy as np

img = nib.load('../../tmp.nii').get_fdata()
affine = nib.load('../../tmp.nii').affine
img = np.array(img)[:,:,:,np.newaxis]
img = np.concatenate((img, img), -1)
print(img.shape)
start = time.time()
mask = bet2.run_bet(img.astype(float), (1,1,1))
print(time.time()-start)
print(mask.shape)
nib.Nifti1Image(mask, affine).to_filename('../../tmp_test.nii')
# print(time.time()-start)