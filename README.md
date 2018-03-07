# Diabetic Retinopathy

This is a first attempt of a complete beginner at building a simple CNN to classify the extent of diabetic retinopathy in retina scans.

- Data is an augmented subset of https://www.kaggle.com/c/diabetic-retinopathy-detection
- Keras model is in Diabetic Retinopathy.ipynb
- Subset (~3500 images) of the total dataset is in data/
- 1000 epochs is the result of running my model over 1k epochs. You can tell the model is overfitting like crazy and maxes out in finding useful features.
- A print of the model architecture is in 'model architecture.txt'
- weights.h5 are of the thousandth epoch
