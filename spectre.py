from PIL import Image
from PIL import ImageDraw
from matplotlib import pyplot as plt

width = 1900
height = 200

image = Image.new("RGB", (width, height))
draw = ImageDraw.Draw(image)

plt.axes('off')

def wavelength_to_rgb(wavelength, gamma=0.8):
    # return 255, 255, 255
    """This converts a given wavelength of light to an
    approximate RGB color value. The wavelength must be given
    in nanometers in the range from 380 nm through 750 nm
    (789 THz through 400 THz).

    Based on code by Dan Bruton
    http://www.physics.sfasu.edu/astro/color/spectra.html
    """

    wavelength = float(wavelength)
    if 380 <= wavelength <= 440:
        attenuation = 0.3 + 0.7 * (wavelength - 380) / (440 - 380)
        R = ((-(wavelength - 440) / (440 - 380)) * attenuation) ** gamma
        G = 0.0
        B = (1.0 * attenuation) ** gamma
    elif 440 <= wavelength <= 490:
        R = 0.0
        G = ((wavelength - 440) / (490 - 440)) ** gamma
        B = 1.0
    elif 490 <= wavelength <= 510:
        R = 0.0
        G = 1.0
        B = (-(wavelength - 510) / (510 - 490)) ** gamma
    elif 510 <= wavelength <= 580:
        R = ((wavelength - 510) / (580 - 510)) ** gamma
        G = 1.0
        B = 0.0
    elif 580 <= wavelength <= 645:
        R = 1.0
        G = (-(wavelength - 645) / (645 - 580)) ** gamma
        B = 0.0
    elif 645 <= wavelength <= 750:
        attenuation = 0.3 + 0.7 * (750 - wavelength) / (750 - 645)
        R = (1.0 * attenuation) ** gamma
        G = 0.0
        B = 0.0
    else:
        R = 1.0
        G = 1.0
        B = 1.0
    R *= 255
    G *= 255
    B *= 255
    return int(R), int(G), int(B)


me = 9.10938356 * 10 ** -31
meso = 207 * me
mp = 1.67 * 10 ** -27
e = 1.6 * 1e-19
c = 3 * 1e8
ee = 8.8541878128 * 10 ** (-12)
h = 6.62607015 * 10 ** (-34)


# ε
def RydbergConst(m):
    const = (m * e ** 4) / (8 * ee ** 2 * h ** 3 * c)
    return const


def wave_length(R, k, n):
    const = (R * (1 / (k ** 2) - 1 / (n ** 2))) ** -1
    return const * 10 ** 9


def reduced_mass(m1, m2):
    return (m1 * m2) / (m1 + m2)


def zinchick(R, n):
    E = -R * c * h * (1 / n ** 2)
    return E


def zinchik_wl(E1, E2):
    diff = abs(E1 - E2)
    wl = h * c / diff
    return wl


m = reduced_mass(me, mp)
R = RydbergConst(m)

k = 1
n = k + 1
buffer = []
print("Lyman series")
for i in range(n, n + 6):
    wl = wave_length(R, k, i)
    print(wl)
    draw.line((wl, 0, wl, height), fill=wavelength_to_rgb(wl))

print("Balmer series")
k = 2
n = k + 1
for i in range(n, n + 6):
    wl = wave_length(R, k, i)
    print(wl)
    draw.line((wl, 0, wl, height), fill=wavelength_to_rgb(wl), width=2)

print("Paschen series")
k = 3
n = k + 1
for i in range(n, n + 6):
    wl = wave_length(R, k, i)
    print(wl)
    draw.line((wl, 0, wl, height), fill=wavelength_to_rgb(wl), )

# print("Brackett series")
# k = 4
# n = k + 1
# for i in range(n, n + 6):
#     wl = wave_length(R, k, i)
#     print(wl)
#     draw.line((wl, 0, wl, height), fill=wavelength_to_rgb(wl))

# draw.line((10, 0, 10, height), fill=wavelength_to_rgb(10))
image.save("spectre.png", "PNG")

print("Zinchik")
print(zinchik_wl(zinchick(R, 4), zinchick(R, 5)) * 10 ** 9)
