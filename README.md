# Simple Photo Filter Library

# Usage

```python
from PIL import Image
from photo_filter import Filterizer, SimpleFilter


image = Image.open("chameleon.jpg")
Filterizer.apply(image, SimpleFilter.negative)
image.save("filterized.jpg")
```

# Examples

## Original photo

![](chameleon.jpg)

Source: [https://www.pexels.com/photo/red-chameleon-567540/](https://www.pexels.com/photo/red-chameleon-567540/)



## Grayscale filters

### Average

![](filterized/grayscale/average.jpg)

### Binary

![](filterized/grayscale/binary.jpg)

### Desaturation

![](filterized/grayscale/desaturation.jpg)

### Luminance

![](filterized/grayscale/luminance.jpg)

### Red channel

![](filterized/grayscale/red_channel.jpg)

### Green channel

![](filterized/grayscale/green_channel.jpg)

### Blue channel

![](filterized/grayscale/blue_channel.jpg)

## Simple filters

### Atmosphere

![](filterized/simple/atmosphere.jpg)

### Blacklight

![](filterized/simple/blacklight.jpg)

### Burn

![](filterized/simple/burn.jpg)

### Color shift

![](filterized/simple/color_shift.jpg)

### Freeze

![](filterized/simple/freeze.jpg)

### Lava

![](filterized/simple/lava.jpg)

### Metal

![](filterized/simple/metal.jpg)

### Negative

![](filterized/simple/negative.jpg)

### Ocean

![](filterized/simple/ocean.jpg)
