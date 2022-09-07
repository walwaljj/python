from PIL import Image#모듈명은 PIL 패키지명은 pillow

image = Image.open("C:\animal/bird1.png")

image.show()
#ImportError: DLL load failed while importing _imaging: 지정된 모듈을 찾을 수 없습니다.

