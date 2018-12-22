# 机器学习中常见面试题与答案（一）

这里罗列机器学习中常见的面试题与我自己整理的答案。

## sigmoid 和 softmax 区别与联系

- sigmoid也叫logistic，输出值在[0,1]之间，作为激活函数会存在梯度消失的问题；可用于二分类问题中；
- softmax是sigmoid在多分类的推广，输出每个类别的概率，加和为1；当类别为2时，与sigmoid等价；
- softmax并不存在学习慢的问题，参考[这里](https://blog.csdn.net/Bixiwen_liu/article/details/52946867)；
- softmax放在最后一层，cost function用cross entropy，[原因](https://www.zhihu.com/question/40403377)

## 常用激活函数比较

[reference](https://www.jianshu.com/p/22d9720dbf1a)

神经网络用激活函数，是为了给网络引入非线性元素，使得网络可以逼近任何非线性函数。    
常见的有sigmoid, tanh, Relu及其变体；

- sigmoid: 在特征相差不是特别大，或者特征比较复杂的时候，效果比较好；还可以用来做二分类；但是：激活函数计算量大，并且容易出现梯度消失的问题；
- tanh: 输出值在[-1, 1]之间，零点对称，实际应用中效果比sigmoid好；在特征相差明显时效果比较好；
- Relu：优点：在SGD时收敛速度很快；不存在梯度消失的问题；计算方便，计算速度快；单侧抑制，具有相对宽阔的兴奋边界，稀疏激活性；
        缺点：比较脆弱，很容易die,神经元失活，要注意学习率设置不能过大；输出不是以0为中心



## Dropout作用，防止过拟合的方式

Dropout让神经网络中的神经元以一定的概率失活，用于防止过拟合。   
其他防止过拟合的方式：
- 扩充数据
- early stopping
- cross validation
- Batch Normalization 
- weight decay(权值衰减)

## weight decay原理与作用



## 损失函数表达式

- 最小平方项
- 对数损失函数


## padding 方式

- padding = 'VALID'，不补0，卷积后图片大小变为： (W-F+1)/S
- padding = 'SAME', 补0， 图片大小变为 W/S

## 各种曲线的含义：ROC，AUC，代价曲线等； ROC和代价曲线的联系

## SVM相关

### SVM硬核表达式

### SMO作用，缺点

### SVM为什么可以逼近任意函数

## 梯度消失，梯度爆炸是什么，怎么解决   

梯度消失：梯度小于1，反向传播梯度是一个类乘，最后就会消失；如果大于1，最后结果就会变得特别大；  
梯度消失一般出现在：深层网络，或采用了不合适的激活函数如sigmoid;    
梯度爆炸一般出现在：深层网络，和权值初始化值太大的情况下；

解决办法：
- 预训练加微调（现在用的不是很多）
- 梯度剪切（大于阈值，强制限制在这个范围内），权重正则化：l1, l2 norm 
- 使用 Relu 等激活函数
- batch Normalization（本质是解决方向传播过程中的梯度问题）
- 残差结构：resnet
- LSTM


## 神经网络输入图片大小为什么要一样，不一样的怎么办

- 神经网络图片输入大小一致：是因为全连接层的参数是固定的，所以不能动；
- SPPnet可以让输入图片大小不一样。它在最后全连接层前面，对feature map用pooling，得到图片长宽为1,2,4的，然后再把他们拉成一条，变成长度为21(1+2x2+4x4)的向量，最后再送到全连接层即可。(知道想要的特征的大小，可以反推出pooling大小，步长等)

## 数据归一化方式

https://www.zhihu.com/question/20467170（还没仔细看）

- min-max归一化：让各个维度特征归一化到[0,1]之间， value_ = (value - min) / (max - min) 
- z_score标准化：用各维的均值和标准差来标准化各维特征值， value_ = (value - u) / sigma

归一化的作用：
- 维度量纲不同，做归一化，可以提高模型正确率（针对不具有伸缩不变性的机器学习算法）；
- 可以加快模型的训练速度；

## 在训练一开始loss就不变，是怎么回事，怎么排查这个问题

### loss = 87.33 不变：

- 在Inception-V3网络的fine-tuning或者train时遇到，softmax计算过程中概率值出现了0，（而softmax是指数计算，都是大于0），应该是计算过程中出现了float溢出，出现了inf,nan等异常值；   
- softmax先求指数，会超出float的数据范围，成为inf。inf与其他任何数值的和都是inf，任何正常范围的数值除以inf都会变成0，然后求loss就出现了87.3356的情况。
- 解决办法：softmax输入的feature由两部分计算得到：输入数据，各层的权值；
    - 减小初始化权重，以使得softmax的输入feature处于一个比较小的范围 
    - 降低学习率，这样可以减小权重的波动范围 
    - 如果有BN(batch normalization)层，finetune时最好不要冻结BN的参数，否则数据分布不一致时很容易使输出值变得很大(注意将batch_norm_param中的use_global_stats设置为false )。 
    - 观察数据中是否有异常样本或异常label，导致数据读取异常 

### 欠拟合

- 欠拟合的变现：训练很长时间，在训练集上，loss仍然很大，和初始值没啥区别，精确度也很低，几乎接近于0，在测试集上也是。
- 怎么判断是否欠拟合：让网络在每次训练时，只迭代同样的数据，甚至每个batch里面都是一样的数据，然后看一下loss和acc的变化。如果这是loss开始下降，acc开始上升，那么就是网络拟合能力不足。
- 解决办法：
    - 加深网络的深度或宽度（加深深度效果一般比较好）
    - 寻找最优的权重初始化方案
    - 使用合适的激活函数
    - 选择合适的优化器和学习速率
    - 过量的正则化会导致欠拟合


### 排查

- 数据输入是否正常，data和label是否一致
- 网络架构的选择
- loss对不对



## Batch Normalization


## Resnet 相关

### Resnet有几种shortcut方式


### Resnet的残差结构特点，Desnet...


## SPPnet

## 权重初始化方案

https://blog.ailemon.me/2018/04/09/deep-learning-the-ways-to-solve-underfitting/

- 全零初始化 Zeros
- 全1初始化 Ones
- 初始化为固定值value  Constant
- 随机正态分布初始化 RandomNormal
- 随机均匀分布初始化 RandomUniform
- 截尾高斯分布初始化 TruncatedNormal
- VarianceScaling
- 用随机正交矩阵初始化Orthogonal
- 使用单位矩阵初始化 Identiy
- LeCun均匀分布初始化方法 lecun_uniform
- LeCun正态分布初始化方法 lecun_normal
- Glorot正态分布初始化方法 glorot_normal
- Glorot均匀分布初始化 glorot_uniform
- He正态分布初始化 he_normal
- LeCun均匀分布初始化 he_uniform

这么多初始化方案，其实按照大类来分，主要就三种：均匀分布、正太分布和相同固定值。

全0的初始化，一般只会被用于逻辑斯蒂回归之类的这种二分类问题上，最多是浅层的神经网络上。全为1或者某个其他相同的值的方案则很少见。因为这种初始化方案，会使得网络处于对称状态，导致的结果就是，每个神经元都具有相同的输出，然后在反向传播计算梯度时，会得到一个同一个梯度值，并且进行着同样的参数更新，这是我们不希望看到的。



- l1,l2正则化和区别
- XGBoost和提升树
- relu  
- 梯度消失
- 循环神经网络，为什么好
- 朴素贝叶斯为什么称为“朴素”；以及朴素贝叶斯的公式表达
从Kmeans、KNN，还有一个我忘了，选择一个算法进行详细的描述及应用说明
机器学习有哪些损失函数
对数损失和均方损失有什么区别
逻辑回归能不能用均方损失
机器学习有哪些评价指标
11.解释一下F1-SCORE？
12.解释一下auc roc？
13.介绍一下决策树?
14.python元组和列表的区别
15.讲一下二叉树排序？
16.红黑树了解嘛？
Bagging和boosting的区别
2-讲讲随机森林的原理？主要是随机属性引入加集成。。

3-Linux 复制命令是什么？查询帮助用什么命令？cp --help
7-xgboost和gbdt区别？一个利用牛顿法二阶导数信息，正则项加上了树的复杂度，缺失值样本不同权重处理？一个一阶导啥的。

8-随机森林和gbdt谁主要降低偏差和方差？gbdt，随机森林。

有哪些分类模型
（4）然后问正则化有哪些
（5）问L1和L2为什么一个稀疏一个平滑
（6）问梯度下降算法与牛顿算法的优缺点
（7）问BP的过程，然后链式求导怎么做
（8）问SVM与贝叶斯的优缺点
（9）问KNN如何解决数据维度问题（不会）

lr和svm，比较优缺点