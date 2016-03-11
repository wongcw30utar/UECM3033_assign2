import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import copy as cp
from PIL import Image

img=mpimg.imread('Ari_1000_800.tiff')
[r,g,b] = [img[:,:,i] for i in range(3)]


fig = plt.figure(1)
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)
ax1.imshow(img)
ax2.imshow(r, cmap = 'Reds')
ax3.imshow(g, cmap = 'Greens')
ax4.imshow(b, cmap = 'Blues')
plt.show()


#calculate svd using np.linalg.svd
#SVD for red color
u_r,s_r,v_r = np.linalg.svd(r)

#create empty square matrix
sigma_red = np.zeros((len(r),len(np.transpose(r))))

#for loop input sigma
for i in range(len(s_r)):
    sigma_red[i][i] = s_r[i]
    

#svd for green color
u_g,s_g,v_g = np.linalg.svd(g)

sigma_green = np.zeros((len(g),len(np.transpose(g))))

for i in range(len(s_g)):
    sigma_green[i][i] = s_g[i]
    
#svd for blue color
u_b,s_b,v_b = np.linalg.svd(b)

sigma_blue = np.zeros((len(b),len(np.transpose(b))))

for i in range(len(s_b)):
    sigma_blue[i][i] = s_b[i]
    
#LOWER RESOLUTIONS
sigma_red_low = cp.copy(sigma_red)
sigma_green_low = cp.copy(sigma_green)
sigma_blue_low = cp.copy(sigma_blue)

for j in range(30,len(sigma_red_low)):
    sigma_red_low[j][j] = 0
    
for j in range(30,len(sigma_green_low)):
    sigma_green_low[j][j] = 0
    
for j in range(30,len(sigma_blue_low)):
    sigma_blue_low[j][j] = 0
    
red_low = np.matrix(u_r) * np.matrix(sigma_red_low) * np.matrix(v_r)
green_low = np.matrix(u_g) * np.matrix(sigma_green_low) * np.matrix(v_g)
blue_low = np.matrix(u_b) * np.matrix(sigma_blue_low) * np.matrix(v_b)

#combine rgb back to single matrix
red_low = np.array(red_low)
green_low = np.array(green_low)
blue_low = np.array(blue_low)

rgb_low = np.dstack((red_low,green_low,blue_low))
rgb_low = np.uint8(rgb_low)

fig = plt.figure(1)
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)
ax1.imshow(rgb_low)
ax2.imshow(red_low, cmap = 'Reds')
ax3.imshow(green_low, cmap = 'Greens')
ax4.imshow(blue_low, cmap = 'Blues')
plt.savefig("figure_low.png")
plt.show()

print("Compression - Lower Resolution: ")
fig_low = plt.figure(1)
plot_low = fig_low.add_subplot(1,1,1)
plot_low.imshow(rgb_low)
plt.show()


#BETTER RESOLUTIONS
sigma_red_better = cp.copy(sigma_red)
sigma_green_better = cp.copy(sigma_green)
sigma_blue_better = cp.copy(sigma_blue)

for j in range(200,len(sigma_red_better)):
    sigma_red_better[j][j] = 0
    
for j in range(200,len(sigma_green_better)):
    sigma_green_better[j][j] = 0
    
for j in range(30,len(sigma_blue_better)):
    sigma_blue_better[j][j] = 0
    
red_better = np.matrix(u_r) * np.matrix(sigma_red_better) * np.matrix(v_r)
green_better = np.matrix(u_g) * np.matrix(sigma_green_better) * np.matrix(v_g)
blue_better = np.matrix(u_b) * np.matrix(sigma_blue_better) * np.matrix(v_b)

#combine rgb back to single matrix
red_better = np.array(red_better)
green_better = np.array(green_better)
blue_better = np.array(blue_better)

rgb_better = np.dstack((red_better,green_better,blue_better))
rgb_better = np.uint8(rgb_better)

fig = plt.figure(1)
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)
ax1.imshow(rgb_better)
ax2.imshow(red_better, cmap = 'Reds')
ax3.imshow(green_better, cmap = 'Greens')
ax4.imshow(blue_better, cmap = 'Blues')
plt.savefig("figure_better.png")
plt.show()

print("Compression - Higher Resolution: ")
fig_high = plt.figure(1)
plot_high = fig_high.add_subplot(1,1,1)
plot_high.imshow(rgb_better)
plt.show()

saveimg = Image.fromarray(rgb_low,'RGB')
saveimg.save('ariana_low.jpg')
saveimg = Image.fromarray(rgb_better,'RGB')
saveimg.save('ariana_better.jpg')