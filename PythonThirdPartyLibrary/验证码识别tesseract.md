# 验证码识别

安装 pytesseract，是 Tesseract 关于 Python 的接口。`pip3 install pytesseract`.
PIL 依赖 pillow 库。

验证：

```python
import pytesseract
from PIL import Image

img = Image.open('./t.jpg')
text = pytesseract.image_to_string(img)
```
