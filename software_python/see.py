import nibabel as nib
import matplotlib.pyplot as plt

# Load the NIfTI file
nii_file = "output.nii"  # Replace with the path to your .nii file
nii_image = nib.load(nii_file)
data = nii_image.get_fdata()

# Select the middle slice along the z-axis
middle_slice_index = data.shape[-1] // 2
middle_slice = data[:, :, middle_slice_index]

# Display the image
plt.imshow(middle_slice.T, cmap="gray", origin="lower")
plt.axis("off")
plt.show()
