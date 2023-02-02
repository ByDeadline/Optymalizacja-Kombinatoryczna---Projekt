# Optymalizacja Kombinatoryczna - Projekt
Superpixel
Edytuj
Autor
Jakub Filipiak 151917
Edytuj
Wstęp
Superpiksel jest pojęciem z zakresu przetwarzania obrazów cyfrowych. Jest to grupa pikseli w obrazie, które są traktowane jako jednostka podczas przetwarzania obrazu. Superpiksel może być wygenerowany przez różne algorytmy, które dzielą obraz na grupy pikseli o podobnych cechach, takich jak kolor lub tekstura.

Jednym z głównych zastosowań superpikseli jest zwiększenie wydajności algorytmów przetwarzania obrazu. Dzielenie obrazu na superpiksele zmniejsza liczbę elementów, z którymi algorytm musi pracować, dzięki czemu może on działać szybciej. Superpiksele mogą być również używane do zwiększenia dokładności algorytmów przetwarzających obrazy, ponieważ traktowanie grup pikseli jako jednostek umożliwia bardziej precyzyjne wykrywanie i rozpoznawanie obiektów w obrazie.

Superpiksele są szeroko stosowane w różnych dziedzinach, takich jak rozpoznawanie obiektów, analiza obrazów medycznych i bezpieczeństwo. Na przykład w rozpoznawaniu obiektów, superpiksele mogą być używane do wykrywania konturów obiektów i dokładniejszego określania ich położenia w obrazie. W analizie obrazów medycznych, superpiksele mogą być wykorzystywane do automatycznego rozpoznawania różnych struktur w obrazach rentgenowskich lub tomografii komputerowej.

Istnieje wiele różnych algorytmów do generowania superpikseli, które różnią się między sobą pod względem dokładności i szybkości działania. Niektóre z nich wykorzystują klasteryzację do grupowania pikseli o podobnych cechach, inne natomiast opierają się na algorytmach selekcji energetycznej.

Edytuj
Algorytmy
SLIC (ang. Simple Linear Iterative Clustering) to jeden z algorytmów do generowania superpikseli. Jego główną ideą jest dzielenie obrazu na grupy pikseli o podobnych cechach, takich jak kolor i tekstura, przy użyciu algorytmu klasteryzacji. Algorytm SLIC jest uważany za jeden z najszybszych i najprostszych algorytmów do generowania superpikseli, a jego dokładność jest porównywalna do bardziej złożonych algorytmów.

Quickshift to inny algorytm do generowania superpikseli. Jego działanie opiera się na selekcji energetycznej, co oznacza, że piksele są grupowane według ich podobieństwa do siebie i do innych pikseli w pobliżu. Quickshift jest uważany za jeden z najdokładniejszych algorytmów do generowania superpikseli, ale jego działanie jest wolniejsze niż w przypadku algorytmów takich jak SLIC.

Watershed to algorytm obrazowania, który jest często używany do generowania superpikseli. Działanie tego algorytmu opiera się na konceptach takich jak dolina i szczyt, a jego głównym celem jest wykrywanie granic obiektów w obrazie. Algorytm watershed jest uważany za jeden z najdokładniejszych algorytmów do wykrywania granic obiektów w obrazie.

Edytuj
Implementacja
Poniższy kod prezentuje implementację algorytmów SLIC, QuickShift i watershed wykorzystaną do przeprowadzenia projektu.

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from skimage.color import rgb2gray
from skimage.filters import sobel
from skimage.segmentation import slic, quickshift, watershed
from skimage.segmentation import mark_boundaries
from skimage.util import img_as_float
 
f = Image.open("test.png")
f = np.asarray(f)
img = img_as_float(f[::2, ::2])
 
segments_slic = slic(img, n_segments=180, compactness=10, sigma=1, start_label=1)
segments_quick = quickshift(img, kernel_size=6, max_dist=100, ratio=0.5)
gradient = sobel(rgb2gray(img))
segments_watershed = watershed(gradient, markers=600)
 
print(f'SLIC number of segments: {len(np.unique(segments_slic))}')
print(f'Quickshift number of segments: {len(np.unique(segments_quick))}')
print(f'Watershed number of segments: {len(np.unique(segments_watershed))}')
 
fig, ax = plt.subplots(1, 3, figsize=(10, 10), sharex=True, sharey=True)
 
ax[0].imshow(mark_boundaries(img, segments_slic))
ax[0].set_title('SLIC')
ax[1].imshow(mark_boundaries(img, segments_quick))
ax[1].set_title('Quickshift')
ax[2].imshow(mark_boundaries(img, segments_watershed))
ax[2].set_title('Watershed')
 
for a in ax.ravel():
    a.set_axis_off()
 
plt.tight_layout()
plt.show()
Edytuj
Wyniki

Na powyższym przykładzie zaprezentowana jest dokładność wykrywania linii przez dane algorytmy. Nawet przy ręcznym ustawieniu odpowiednich parametrach widać dużą precyzje algorytmu QuickShift, jak i Watershed.

out:

SLIC number of segments: 867 0.21482062339782715
Quickshift number of segments: 1353 1.0090453624725342
Watershed number of segments: 576 0.039270639419555664

Na tym przykładzie widać przykładowe wykorzystanie algorytmu Watershed do wykrywania elewacji na obrazie.

out:

SLIC number of segments: 936 0.6368587017059326
Quickshift number of segments: 1716 2.6080825328826904
Watershed number of segments: 609 0.18794465065002441

out:

SLIC number of segments: 985 0.29385948181152344
Quickshift number of segments: 1681 0.9810140132904053
Watershed number of segments: 608 0.04421114921569824
Edytuj
Literatura
https://pyimagesearch.com/2014/07/28/a-slic-superpixel-tutorial-using-python/
https://docs.opencv.org/3.4/df/d6c/group__ximgproc__superpixel.html
