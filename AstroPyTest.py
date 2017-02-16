from astropy.io import fits

from astropy.stats import sigma_clipped_stats
from photutils import datasets
from photutils import DAOStarFinder

hdulist = fits.open(
    "/home/smeehan/DT265Project/fits/frame-r-006709-3-0028.fits")

# print(hdulist[0].header['naxis'])

data = hdulist[0].data

print(data[0, 0])
print(data.size)


hdulist.close()


mean, median, std = sigma_clipped_stats(data, sigma=3.0, iters=5)

print(mean, "+/-", std)

daofind = DAOStarFinder(fwhm=3, threshold=5 * std)
sources = daofind(data - median)

sources['mag'] + 24.8

print(sources['xcentroid', 'ycentroid', 'mag'])

sources.write("sources.csv")

