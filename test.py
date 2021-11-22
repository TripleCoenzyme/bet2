import bet2
import SimpleITK as sitk
import time
import numpy as np

img = sitk.ReadImage('tmp.nii')
arr = sitk.GetArrayViewFromImage(img).transpose(2,1,0)[:,:,:,np.newaxis] # Remember SimpleITK use array differently
arr = np.concatenate((arr, arr), -1) # create a (x, y, z, echo) array

print(arr.shape)
start = time.time()

mask = bet2.run_bet(arr.astype(float), (1,1,1), 0.4, 0) # main BET

print(time.time()-start)
print(mask.shape)

mask_img = sitk.GetImageFromArray(mask.astype(np.uint8).transpose(2,1,0,3)) # Remember SimpleITK use array differently
mask_img.SetSpacing(img.GetSpacing())
mask_img.SetOrigin(img.GetOrigin())
mask_img.SetDirection(img.GetDirection())
sitk.WriteImage(mask_img, 'tmp_test.nii')