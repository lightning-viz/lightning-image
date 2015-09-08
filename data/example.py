from lightning import Lightning
from sklearn import datasets

lgn = Lightning()

imgs = datasets.load_sample_images()['images']

lgn.image(imgs[0])