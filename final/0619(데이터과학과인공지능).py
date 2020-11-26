# 데이터과학과 인공지능
# pip : 파이썬 패키지 관리자

# matplotlib : 그래프, 그림을 그리는데 사용
import matplotlib.pyplot as plt
plt.plot([x축 값], [y축 값], 옵션)
plt.show()

# axis() : x축 y축 값의 범위 지정
# plt.bar : 막대그래프

# image.open() : 이미지파일가져오기
# imshow : 이미지보여주기
import matplotlib.pyplot as plt
from PIL import Image
digitImage = Image.open("digit-5.png")
plt.imshow(digitImage)
plt.show()

# numpy : 벡터 및 행렬 연산에 있어서 매우 편리한 기능 ,  다차원 배열
import numpy as np
a = np.arrange(6)
b = a.reshape(3, 2)   #3행 2열 행렬

# pandas : 데이터 수집과 분석
# Series : 1차원배열 , DataFrame : 2차원배열
import pandas as pd
list1 = ['hello', 2, 4.5, 'AB', True]
sr1 = pd.Series(list1)
print(sr1)
dict1 = {'A':'hello', 'B':2, 'C':4.5, 'D':'AB', 'E':True}
sr2 = pd.Series(dict1)
print(sr2)

import pandas as pd
dict2 = {'A':[1,2,3], 'B':[4,5,6], 'C':[6,7,8], 'D':[9,10,11]}
df1 = pd.DataFrame(dict2)
print(df1)

# keras : 딥러닝 인간의신경망개념모델링
from keras.datasets import mnist
(trainImages, trainLabels), (testImages, testLabels) = mnist.load_data()
print("학습 이미지 개수=", trainImages.shape)
print("테스트 이미지 개수=", testImages.shape)







