# SimpliLang

**SimpliLang** is a beginner-friendly, modular, block-based scripting language built on top of Python.  
It is designed to be open, easy to expand, and understandable even for users with minimal programming knowledge.

---

## 🚀 Features

- Block-based modular system
- Easy-to-read and easy-to-extend syntax
- Built-in Python interpreter
- OpenCV integration
- Support for creating your own blocks/modules
- Organized structure for rapid development

---

## 🛠️ Installation

```bash
git clone https://github.com/your_username/simpli-lang.git
cd simpli-lang
python interpreter.py
```

Python 3.8+ is required. To use OpenCV-based blocks, install OpenCV:

```bash
pip install opencv-python
```

---

## 🧱 Language Structure

Each block is a separate `.block.py` file located inside the `blocks/` directory.  
Blocks are categorized into folders like `image`, `math`, `string`, etc.

### Example structure:

```plaintext
blocks/
  ├── image/
  │    ├── read.block.py
  │    ├── resize.block.py
  │    └── show.block.py
  └── math/
       ├── add.block.py
       └── multiply.block.py
```

---

## 📚 Creating New Blocks

### 1. Create a new block file  
For example: `blocks/image/rotate.block.py`

### 2. Use this basic template:

```python
def run(args, context):
    # args: list of input arguments
    # context: shared variable environment
    import cv2
    img = context[args[0]]
    angle = float(args[1])
    (h, w) = img.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(img, M, (w, h))
    context[args[2]] = rotated
```

### 3. No need to register manually  
The interpreter (`interpreter.py`) automatically loads all `.block.py` files.

---

## 💡 Example Script

```txt
load_image "cat.png" as img
resize img to 200x200 as resized
show resized
```

This script uses blocks under `blocks/image/`.

---

## 🔧 For Developers

- All blocks live inside the `blocks/` folder.
- You can add new block categories such as `audio/`, `video/`, or `network/`.
- Utility functions should be placed inside `lib/utils.py`.
- The interpreter dynamically loads and runs all blocks without manual configuration.

---

## 📂 Project Structure

```plaintext
simpli-lang/
├── interpreter.py         # Main interpreter
├── blocks/                # All categorized block folders
│   ├── image/
│   ├── math/
│   └── string/
├── lib/                   # Helper functions/utilities
│   └── utils.py
├── LICENSE
└── README.md
```

---

## 📜 License

This project is licensed under the MIT License. You are free to use, modify, and distribute it for personal or commercial use.

---

## 👥 Contributing

If you would like to contribute:
- Create new block files and organize them in the appropriate category folder.
- Improve documentation or fix bugs.
- Submit a pull request or open an issue to suggest new features or ideas.

Let's build SimpliLang together!
