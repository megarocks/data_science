from keras.datasets import mnist
import matplotlib.pyplot as plt

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

my_slice = train_images[10:100]
my_slice2 = train_images[10:100, :, :]
my_slice3 = train_images[10:100, 0:28, 0:28]

print(my_slice.shape, my_slice2.shape, my_slice3.shape)

bottom_left = train_images[178:179, 7:-7, 7:-7]
print(bottom_left.shape)

plt.imshow(bottom_left[0], cmap=plt.get_cmap('summer'))
plt.show()
