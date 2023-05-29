import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt
from scipy.ndimage import zoom

image_files = ["liver_46.nii", "liver_54.nii", "liver_73.nii"]  # Replace with your actual file names
image_slices = []

min_shape = None

for file in image_files:
    img = nib.load(file)
    data = img.get_fdata()

    if min_shape is None or data.shape[:2] < min_shape:
        min_shape = data.shape[:2]

    image_slices.append(data)

resized_slices = []

for slice_data in image_slices:
    if len(slice_data.shape) < 2:
        continue  # Skip slices with less than 2 dimensions

    # Calculate the resize factors for each dimension
    resize_factors = [min_shape[i] / slice_data.shape[i] for i in range(min(len(slice_data.shape), len(min_shape)))]

    # Pad the resize factors with 1s if necessary
    resize_factors += [1] * (len(slice_data.shape) - len(resize_factors))

    # Resize each slice using the calculated resize factors
    resized_slice = zoom(slice_data, resize_factors, order=1)

    resized_slices.append(resized_slice)

# Check if all resized_slices have the same shape
shapes = [slice_data.shape for slice_data in resized_slices]
if len(set(shapes)) != 1:
    # If shapes are different, resize the slices to the minimum shape
    min_shape = min(shapes)

    resized_slices = [np.resize(slice_data, min_shape) for slice_data in resized_slices]

volume = np.stack(resized_slices, axis=-1)

def show_slices(slices):
    fig, axes = plt.subplots(1, len(slices))
    for i, slice in enumerate(slices):
        axes[i].imshow(slice.T, cmap="gray", origin="lower")

# Show slices from the middle of the volume
middle_slices = volume[volume.shape[0] // 2, :, :]
def show_slices(slices):
    fig, axes = plt.subplots(1, len(slices))
    for i, slice in enumerate(slices):
        axes[i].imshow(slice.T, cmap="gray", origin="lower")
    plt.show()


output_file = "output.nii"  # Replace with your desired output file name
output_img = nib.Nifti1Image(volume, affine=np.eye(4))
nib.save(output_img, output_file)
