# SVD-Image-Compression
## Overview
The SVD-Image-Compression project aims to explore the practical applications of linear algebra, focusing on image processing using [Singular Value Decomposition (SVD)](https://en.wikipedia.org/wiki/Singular_value_decomposition). The primary goal is to reduce the amount of data necessary to reconstruct an image with minimal loss of quality.

## Results
We applied SVD compression to several images, each time varying the **k** parameter. The **k** parameter represents the percentage of singular values retained, where a **smaller** k results in **more information loss** from the original image. The results, including the space saved as a percentage of the original matrix size, can be found in the `images/` folder.

## Conclusions
- SVD compression is most effective on larger images when the k parameter is set to values less than 0.2.
- For RGB images, noticeable noise can appear even with higher k values.

## Example
<div align="center">
  <img src="https://github.com/AdamKaniasty/SVD-Image-Compression/blob/main/images/gray/figs/geralt_0.1.jpg" alt="SVD Compressed Image" width="800">
  <p>Figure 1: Example of an image compressed using SVD with k=0.1.</p>
</div>

## Authors
- Adam Kaniasty
- Igor Kołodziej
- Hubert Kowalski
