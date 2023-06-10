import os
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

path_grey = './images/gray'
path_color = './images/color'

color_images = []
gray_images = []
color_images_names = []
gray_images_names = []

for filename in os.listdir(path_color):
    if filename.endswith('.jpg'):
        img = Image.open(os.path.join(path_color, filename))
        img_matrix = np.array(img)
        color_images.append(img_matrix)
        color_images_names.append(filename[:-4])

for filename in os.listdir(path_grey):
    if filename.endswith('.jpg'):
        img = Image.open(os.path.join(path_grey, filename)).convert('L')
        img_matrix = np.array(img)
        gray_images.append(img_matrix)
        gray_images_names.append(filename[:-4])


def performSVD(img, gray=True, k=0.05):
    num = None
    if gray:
        U, S, V = np.linalg.svd(img, full_matrices=False)
        num = round(S.shape[0] * k)
        return [U[:, :num], S[:num], V[:num, :], num]
    else:
        U = []
        S = []
        V = []
        for i in range(3):
            U_temp, S_temp, V_temp = np.linalg.svd(img[:, :, i])
            num = round(S_temp.shape[0] * k)
            U.append(U_temp[:, :num])
            S.append(S_temp[:num])
            V.append(V_temp[:num, :])
        return [U, S, V, num]


def reconstructSVD(U, S, V, gray=True):
    if gray:
        return np.matrix(U) * np.diag(S) * np.matrix(V)
    else:
        print(U[0].shape, S[0].shape, V[0].shape)
        svd_r = reconstructSVD(U[0], S[0], V[0], True)
        svd_g = reconstructSVD(U[1], S[1], V[1], True)
        svd_b = reconstructSVD(U[2], S[2], V[2], True)
        img = np.zeros((U[0].shape[0], V[0].shape[1], 3))
        img[:, :, 1] = svd_g
        img[:, :, 0] = svd_r
        img[:, :, 2] = svd_b
        return img


def spaceSavings(imgarr, k, gray=True):
    rows, cols = imgarr.shape[:2]
    bpp = imgarr.itemsize * 8
    bps = np.dtype(np.float32).itemsize * 8
    if gray:
        orig_size = rows * cols * bpp
        rankk_size = (rows * k + k + k * cols) * bps
        saved = (orig_size - rankk_size) / orig_size * 100
    else:
        orig_size = rows * cols * 3 * bpp
        rankk_size = (rows * k + k + k * cols) * 3 * bps
        saved = (orig_size - rankk_size) / orig_size * 100
    return saved


def processIMG(img, name, k, gray=True):
    svd = performSVD(img, gray, k)
    num = svd[3]
    reconstruction = reconstructSVD(svd[0], svd[1], svd[2], gray)
    plt.figure(figsize=(9, 6))
    saved = spaceSavings(img, num, gray)
    plt.subplot(121)
    if gray:
        plt.imshow(img, cmap='gray')
        plt.subplot(122)
        plt.imshow(reconstruction, cmap='gray')
        plt.title(f'{name}, k = {k}, saved={saved:.2f}%')
        plt.savefig(f'./images/gray/figs/{name}_{k}.jpg')
        plt.close()
        plt.imsave(f'./images/gray/reconstructed/{name}_{k}.jpg', reconstruction, cmap='gray')
    else:
        plt.imshow(img)
        plt.subplot(122)
        plt.imshow(reconstruction.astype(np.uint8))
        plt.title(f'{name}, k = {k}, saved={saved:.2f}%')
        plt.savefig(f'./images/color/figs/{name}_{k}.jpg')
        plt.close()
        plt.imsave(f'./images/color/reconstructed/{name}_{k}.jpg', reconstruction.astype(np.uint8))


def testPerformanceGray():
    k_params = [0.01, 0.05, 0.1, 0.2, 0.5]
    for (index, img) in tqdm(enumerate(gray_images)):
        for k in tqdm(k_params):
            processIMG(img, gray_images_names[index], k)


processIMG(color_images[0], color_images_names[0], 0.05, False)
