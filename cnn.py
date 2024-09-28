import numpy as np

imgN = 20
image = np.random.randn(imgN, imgN)

# convolution kernel
kn = 7
Y, X = np.meshgrid(np.linspace(-3, 3, kn), np.linspace(-3,3,kn))
krnl = np.exp( -(X**2+Y**2)/7)

# now for the convolution
convout = np.zeros((imgN, imgN))
half_kr = kn//2

for rowi, in range(half_kr, imgN-half_kr):
    for coli in range(half_kr, imgN-half_kr):
        # cut out a piece of the image
        p_img = image[rowi-half_kr:rowi+half_kr+1,:] # get the rows
        p_img = p_img[:, coli-half_kr:coli+half_kr+1] # extract the columns 

        # dot product: 
        dotprod = np.sum(p_img*krnl[::-1, ::-1])

        # store the result for this pixel
        convout[rowi, coli] = dotprod
