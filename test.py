import bet2
import nibabel as nib
import time
import numpy as np

img = nib.load('C:/Users/42965/Desktop/tmp.nii').get_fdata()
affine = nib.load('C:/Users/42965/Desktop/tmp.nii').affine
img = np.array(img)[np.newaxis,:,:,:]
img = np.concatenate((img, img, img, img, img, img), 0)
print(img.shape)
# img = np.array(img)[:,:,:,np.newaxis]
start = time.time()
mask = bet2.run_bet(img.astype(float), (1,1,1))
print(time.time()-start)
print(mask.shape)
nib.Nifti1Image(mask, affine).to_filename('C:/Users/42965/Desktop/tmp_test.nii')
# print(time.time()-start)