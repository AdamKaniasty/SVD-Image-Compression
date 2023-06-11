# SVD-Image-Compression

### Authors:
- Adam Kaniasty
- Igor Kołodziej
- Hubert Kowalski

### Goal:
Project's goal is to explore practical applications of linear algebra. 
We focused on processing images using SVD (Singular value decomposition), especially reducing the size of data necessary to reconstruct an image without much loss of image's quality.

### Results:
We performed the SVD compression on a few images (see images folder) each time with a diffrent k - parameter (k is the percange of singular values of a matrix that we want to keep, meaning the smaller k is, more information about starting image is lost).
We also measured how much space was saved by performing the compression (see saved="" in images' titles) as a percentage of the size of original matrix.

### Conclusions:
SVD compression performs the best on bigger images when k parameter is set to values < 0.2. Also, when performed on RGB images, sometimes a visible noise appears even for larger values of k.
