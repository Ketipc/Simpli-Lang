# SimpliLang

SimpliLang is a beginner-friendly, block-based interpreted language written in Python.  
It supports custom blocks and integrations like OpenCV for image processing.

## How to Run

```
python main.py examples/opencv_example.simpli
```

## Language Example

```
img = load_image("photo.jpg")
gray = to_grayscale(img)
save_image(gray, "gray.jpg")
```

## Features

- Easy syntax
- Customizable blocks
- OpenCV integration
