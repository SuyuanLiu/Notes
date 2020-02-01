# AAAI Extend Records

对 AAAI 文章进行扩刊实验。之前文章提出的方法是 IAG。扩刊部分主要针对跨人实验进行改进。

IAG 模型在 SEED 上跨人实验结果：mean=86.30, std=6.91

### model1

2019 年 12 月底，使用 GAN 思想，加入对抗。

- 另起一个分支，从 test data 中进行采样，对这部分数据做 encoder， decoder（全部采用 FC layers）；
- 用中间 encoder 后的向量，与 IAG 输出的向量，做对抗；GAN_loss
- 对新分支的输入输出，采用均方差 loss
- IAG 模型的是分类的交叉熵 loss

### model2

2020 年 1 月底，采用 VAE 思想。

- 之前只生成一个 W，现在生成两个 W，一个做 mean，一个做 std，然后从这两个 W 中随机采样，生成一个新 W；
- 同时在模型最后面加入 decoder 网络（两层 FC layers）
- 模型一个三个 loss：IAG 分类的交叉熵；decoder 后的向量与输入 x 的均方差 loss（reconstruction loss）；VAE 对应的 KLloss（latent loss）

实验过程中的问题与发现：

- 新生成的 w 没有进行 tf.nn.relu 操作，最后导致模型 IAG 部分对应的 loss 为 nan，模型不收敛；猜测：应该是图卷积部分对 W 的要求就是非负的，处理过程中若出现负数，会导致 nan 的出现（暂时没有仔细研究）
- 实验过程中，在图卷积部分，误使用之前的 W，但是实验中还是使用了 VAE 的 latent loss（数值很小，0.0004；IAGloss 数值 300-100），reconstruction loss（数量级与 IAG loss 相当）。实验效果有提升，这说明，模型中只要加入一个 decoder，使得输入与输出向量接近，就可以使模型性能提高。(mean accuracy = 87.86, std = 6.44)
