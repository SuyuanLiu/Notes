# AAAI Extend Records

**Index**

- [AccSummary](#AccSummary)
- [模型调试结果记录](#模型调试结果记录)
- [model1](#model1)
- [model2](#model2)
- [model3](#model3)

对 AAAI 文章进行扩刊实验。之前文章提出的方法是 IAG。扩刊部分主要针对跨人实验进行改进。

IAG 模型在 SEED 上跨人实验结果：mean=86.30, std=6.91

### AccSummary

**最终**

- 未注明的情况都是：`x*1,regu_loss*1`

非跨人

|   Model    |    SEED(ACC/STD)    | MPED Protocol 1(ACC/STD) | MPED Protocol 2(ACC/F1) | MPED Protocol 3(ACC/STD) |
| :--------: | :-----------------: | :----------------------: | :---------------------: | :----------------------: |
|    IAG     |     95.44/05.48     |       74.77/10.75        |       73.58/68.41       |       40.38/08.75        |
| new_method | 95.52/05.32(0.8VAE) |                          |                         |                          |

跨人

|   Model    |           SEED(ACC/STD)           | MPED Protocol 1(ACC/STD) | MPED Protocol 2(ACC/F1) | MPED Protocol 3(ACC/STD) |
| :--------: | :-------------------------------: | :----------------------: | :---------------------: | :----------------------: |
|    IAG     |            86.30/6.91             |        57.23/7.86        |       63.22/41.54       |        28.29/5.61        |
| new_method | 87.09/6.51(`x*10,regu_loss * 20`) |                          |                         |                          |

**SEED 结果记录**

SEED 非跨人

|   Model    |     ACC/STD     |                        Note                         |
| :--------: | :-------------: | :-------------------------------------------------: |
|    IAG     |   95.44/05.48   |                                                     |
|  IAG+VAE   |   94.54/05.38   |                 `x*10,regu_loss*20`                 |
| IAG+0.1VAE |   93.67/05.92   |                 `x*10,regu_loss*20`                 |
| IAG+0.2VAE |   94.25/05.49   |                 `x*10,regu_loss*20`                 |
| IAG+0.3VAE |   93.61/05.47   |                 `x*10,regu_loss*20`                 |
| IAG+0.4VAE |   94.81/05.14   |                 `x*10,regu_loss*20`                 |
| IAG+0.5VAE |   94.74/05.31   |                 `x*10,regu_loss*20`                 |
| IAG+0.5VAE |   94.50/05.43   |                 `x*10,regu_loss*50`                 |
| IAG+0.6VAE |   94.90/05.44   |                 `x*10,regu_loss*20`                 |
| IAG+0.7VAE |   94.30/05.12   |                 `x*10,regu_loss*20`                 |
| IAG+0.8VAE | **95.52/05.32** |                 `x*10,regu_loss*20`                 |
| IAG+0.8VAE |   93.04/06.40   | `x*10,regu_loss*20, W_mean, W_sigma --> tf.nn.relu` |
| IAG+0.8VAE |   93.03/05.70   |                 `x*10,regu_loss*50`                 |
| IAG+0.8VAE |   88.69/09.16   |                `x*10,regu_loss*100`                 |
| IAG+0.9VAE |   95.28/05.76   |                 `x*10,regu_loss*20`                 |
|            |                 |                                                     |
|  IAG+cVAE  |   91.43/07.18   | `x*10,regu_loss*20, W_mean, W_sigma --> tf.nn.relu` |
|  IAG+cVAE  |   91.48/07.89   | `x*10,regu_loss*50, W_mean, W_sigma --> tf.nn.relu` |
|  IAG+cVAE  |   91.25/06.92   | `x*20,regu_loss*50, W_mean, W_sigma --> tf.nn.relu` |

**MPED protocol 1 结果记录**

注：IAG+VAE 的 MPED 中，`VAE_loss * 10` (在`VAE_loss = latent_loss * 10`那边)

| subject_dependent Model |     ACC/STD     |               Note               |
| :---------------------: | :-------------: | :------------------------------: |
|         **IAG**         | **74.77/10.75** |                                  |
|         IAG+VAE         | **73.11/12.56** |                                  |
|       IAG+0.01VAE       |                 |                                  |
|       IAG+0.02VAE       |                 |                                  |
|       IAG+0.03VAE       |                 |                                  |
|       IAG+0.04VAE       |                 |                                  |
|       IAG+0.05VAE       |                 |                                  |
|       IAG+0.06VAE       |                 |                                  |
|       IAG+0.07VAE       |                 |                                  |
|       IAG+0.08VAE       |                 |                                  |
|       IAG+0.09VAE       |                 |                                  |
|       IAG+0.1VAE        |   72.68/12.45   |                                  |
|       IAG+0.2VAE        |   72.70/12.84   |                                  |
|       IAG+0.3VAE        |   72.42/12.73   |                                  |
|       IAG+0.4VAE        |   72.44/13.08   |                                  |
|       IAG+0.5VAE        |   72.64/13.24   |                                  |
|       IAG+0.6VAE        |   72.61/12.79   |                                  |
|       IAG+0.7VAE        |   72.54/13.04   |                                  |
|       IAG+0.8VAE        |   72.33/13.25   |                                  |
|       IAG+0.9VAE        |   72.92/12.80   |                                  |
|      以下全部满足       |                 | `W_mean, W_sigma --> tf.nn.relu` |
|       IAG+0.1VAE        |   72.33/13.11   |                                  |
|       IAG+0.2VAE        |   71.97/12.43   |                                  |
|       IAG+0.3VAE        |   72.45/13.17   |                                  |
|       IAG+0.4VAE        |   72.31/12.55   |                                  |
|       IAG+0.5VAE        |   72.04/12.63   |                                  |
|       IAG+0.6VAE        |   72.77/12.79   |                                  |
|       IAG+0.7VAE        |   72.43/12.56   |                                  |
|       IAG+0.8VAE        |   72.42/12.90   |                                  |
|       IAG+0.9VAE        | **73.16/11.88** |                                  |
|        IAG+cVAE         | **73.45/12.35** |                                  |

**MPED protocol 2 结果记录**
注：IAG+VAE 的 MPED 中，`VAE_loss * 10` (在`VAE_loss = latent_loss * 10`那边)

| subject_dependent Model |     ACC/F1      |               Note               |
| :---------------------: | :-------------: | :------------------------------: |
|         **IAG**         | **73.58/68.41** |                                  |
|         IAG+VAE         |   71.75/64.53   |                                  |
|       IAG+0.01VAE       |   71.42/64.94   |                                  |
|       IAG+0.02VAE       |   71.66/64.99   |                                  |
|       IAG+0.03VAE       |   70.92/64.82   |                                  |
|       IAG+0.04VAE       |   71.16/64.51   |                                  |
|       IAG+0.05VAE       |   71.27/64.60   |                                  |
|       IAG+0.06VAE       |   71.83/65.23   |                                  |
|       IAG+0.07VAE       |   71.50/65.45   |                                  |
|       IAG+0.08VAE       |   71.17/64.19   |                                  |
|       IAG+0.09VAE       |   71.28/64.21   |                                  |
|       IAG+0.1VAE        | **72.15/64.76** |                                  |
|       IAG+0.2VAE        |   71.96/64.72   |                                  |
|       IAG+0.3VAE        |   71.75/66.08   |                                  |
|       IAG+0.4VAE        |   71.60/65.29   |                                  |
|       IAG+0.5VAE        |   72.03/65.25   |                                  |
|       IAG+0.6VAE        |   71.11/66.06   |                                  |
|       IAG+0.7VAE        | **72.15/66.00** |                                  |
|       IAG+0.7VAE        |   71.00/63.56   | `W_mean, W_sigma --> tf.nn.relu` |
|       IAG+0.7VAE        |   71.65/59.63   |          `reguLoss*10`           |
|       IAG+0.7VAE        |   70.83/59.07   |        `reguLoss*10,x*3`         |
|       IAG+0.7VAE        |   71.41/60.43   |     `reguLoss*10,VAELoss*10`     |
|       IAG+0.8VAE        |   71.48/64.81   |                                  |
|       IAG+0.9VAE        |   71.43/63.76   |                                  |
|      以下全部满足       |                 | `W_mean, W_sigma --> tf.nn.relu` |
|       IAG+0.1VAE        |   72.17/65.50   |                                  |
|       IAG+0.2VAE        | **72.28/66.24** |                                  |
|       IAG+0.3VAE        |   71.78/64.92   |                                  |
|       IAG+0.4VAE        |   71.22/64.24   |                                  |
|       IAG+0.5VAE        |   71.38/65.08   |                                  |
|       IAG+0.6VAE        |   72.06/65.82   |                                  |
|       IAG+0.7VAE        |   71.00/63.56   |                                  |
|       IAG+0.8VAE        |   71.35/64.19   |                                  |
|       IAG+0.9VAE        |   71.98/65.99   |                                  |
|        IAG+cVAE         | **71.46/64.66** |                                  |

**MPED protocol 3 结果记录**
注：IAG+VAE 的 MPED 中，`VAE_loss * 10` (在`VAE_loss = latent_loss * 10`那边)

| subject_dependent Model |     ACC/STD     |               Note               |
| :---------------------: | :-------------: | :------------------------------: |
|         **IAG**         | **40.38/08.75** |                                  |
|         IAG+VAE         |   39.10/10.23   |                                  |
|         IAG+VAE         |   39.16/11.49   |          `regu_loss*10`          |
|       IAG+0.01VAE       |   39.08/09.86   |                                  |
|       IAG+0.02VAE       |   39.17/09.67   |                                  |
|       IAG+0.03VAE       |   39.02/09.63   |                                  |
|       IAG+0.04VAE       |   38.85/09.28   |                                  |
|       IAG+0.05VAE       |   38.96/09.62   |                                  |
|       IAG+0.06VAE       |   38.88/11.08   |                                  |
|       IAG+0.07VAE       |   39.20/10.37   |                                  |
|       IAG+0.08VAE       |   39.10/09.62   |                                  |
|       IAG+0.09VAE       |   39.37/09.74   |                                  |
|       IAG+0.1VAE        |   38.72/10.69   |                                  |
|       IAG+0.2VAE        |   38.87/10.16   |                                  |
|       IAG+0.3VAE        |   37.75/10.78   |                                  |
|       IAG+0.4VAE        |   38.71/09.91   |                                  |
|       IAG+0.5VAE        |   38.27/10.53   |                                  |
|       IAG+0.6VAE        | **39.19/10.35** |                                  |
|       IAG+0.7VAE        | **39.02/09.63** |                                  |
|       IAG+0.8VAE        |   38.89/09.75   |                                  |
|       IAG+0.9VAE        |   38.77/09.57   |                                  |
|      以下全部满足       |                 | `W_mean, W_sigma --> tf.nn.relu` |
|       IAG+0.1VAE        |   38.99/08.87   |                                  |
|       IAG+0.2VAE        |   39.56/10.40   |                                  |
|       IAG+0.3VAE        | **40.35/09.47** |                                  |
|       IAG+0.4VAE        |   39.26/10.81   |                                  |
|       IAG+0.5VAE        |   39.36/10.59   |                                  |
|       IAG+0.6VAE        |   39.19/10.74   |                                  |
|       IAG+0.7VAE        | **39.84/09.02** |                                  |
|       IAG+0.8VAE        |   38.19/10.19   |                                  |
|       IAG+0.9VAE        |   39.15/10.33   |                                  |
|        IAG+cVAE         | **39.75/09.82** |                                  |

### MPED 跨人

**MPED protocol 1 结果记录**

注：IAG+VAE 的 MPED 中，`VAE_loss * 10` (在`VAE_loss = latent_loss * 10`那边)

| subject_independent Model |  ACC/STD   | Note |
| :-----------------------: | :--------: | :--: |
|            IAG            | 57.23/7.86 |      |
|          IAG+VAE          | 54.81/8.23 |      |
|        IAG+0.1VAE         |  running   |      |
|        IAG+0.2VAE         |  running   |      |
|        IAG+0.3VAE         |  running   |      |
|        IAG+0.4VAE         |  running   |      |
|        IAG+0.5VAE         |  running   |      |
|        IAG+0.6VAE         |  running   |      |
|        IAG+0.7VAE         |  running   |      |
|        IAG+0.8VAE         |  running   |      |
|        IAG+0.9VAE         |  running   |      |

**MPED protocol 2 结果记录**
注：IAG+VAE 的 MPED 中，`VAE_loss * 10` (在`VAE_loss = latent_loss * 10`那边)

| subject_independent Model |   ACC/F1    | Note |
| :-----------------------: | :---------: | :--: |
|            IAG            | 63.22/41.54 |      |
|          IAG+VAE          | 63.18/40.2  |      |
|        IAG+0.3VAE         |   running   |      |
|        IAG+0.5VAE         |   running   |      |
|        IAG+0.7VAE         |   running   |      |

**MPED protocol 3 结果记录**
注：IAG+VAE 的 MPED 中，`VAE_loss * 10` (在`VAE_loss = latent_loss * 10`那边)

| subject_independent Model |  ACC/STD   | Note |
| :-----------------------: | :--------: | :--: |
|            IAG            | 28.29/5.61 |      |
|          IAG+VAE          | 27.14/4.83 |      |
|        IAG+0.3VAE         |  running   |      |
|        IAG+0.5VAE         |  running   |      |
|        IAG+0.7VAE         |  running   |      |

### 模型调试结果记录

SEED 跨人

| Idx  |                                    model 说明                                     |    Acc/std     |
| :--: | :-------------------------------------------------------------------------------: | :------------: |
|  -   |                                        IAG                                        |   86.30/6.91   |
|  0   |                                  仅加入 decoder                                   |   87.17/6.12   |
| 0_1  |                      仅加入 decoder, W 的 relu 换为 sigmoid                       |   83.40/7.30   |
|  1   |                        加入 VAE+decoder，去掉 latent loss                         |   84.00/7.88   |
|  2   |                   加入 VAE（reconstruction loss + latent loss）                   |   84.74/6.50   |
|  3   |                        加入 VAE，把 W 的 relu 换为 sigmoid                        |   84.83/6.42   |
|  4   |       加 decoder，加分支 W，两个 W 结果 concat(W_general:`62*62*5`, W-relu)       |   85.33/7.24   |
|  5   |     加 decoder，加分支 W，两个 W 结果 concat(W_general:`62*62*5`, W-sigmoid)      |   83.89/7.35   |
|  6   |        加 decoder，加分支 W，两个 W 结果 concat(W_general:`62*62`, W-relu)        |   83.62/6.87   |
|  7   |               VAE + decoder, W 生成那边的 `x * 10, regu_loss * 20`                |  80.09/10.83   |
| 说明 |          以下如无说明，都是 W_general:`62*62*5`, W-relu,`regu_loss * 20`          |       -        |
|  8   |        VAE(不要 decoder，去掉 reconstruction loss,x _ 10, regu_loss _ 20)         |   74.4/12.13   |
|  9   |                                       cVAE                                        |  76.21/11.83   |
|  10  |                                  cVAE + decoder                                   |   83.16/9.42   |
|  11  |                      cVAE+decoder+Wconcat: 4 的情况，用 cVAE                      |  86.28 /7.27   |
|  12  |                        VAE+Wconcat: 4 的情况，decoder 去掉                        |   83.95/7.95   |
|  13  |                  cVAE+Wconcat: 4 的情况，decoder 去掉，换成 cVAE                  |   84.04/7.91   |
| 13_1 |                        13, cVAE+Wconcat,`cVAE_loss * 0.2`                         |   83.14/8.76   |
| 13_2 |                        13, cVAE+Wconcat,`cVAE_loss * 0.5`                         |   84.07/6.64   |
| 13_3 |                        13, cVAE+Wconcat,`cVAE_loss * 0.8`                         |   82.76/8.24   |
|  14  |                   cVAE + Wconcat, W 生成那边的 `regu_loss * 1`                    |   84.63/8.21   |
| 14_0 |          cVAE + Wconcat, W 生成那边的 `regu_loss * 1`, `cVAE_loss * 0.1`          | **87.29/6.07** |
| 14_1 |          cVAE + Wconcat, W 生成那边的 `regu_loss * 1`, `cVAE_loss * 0.2`          |   84.76/7.19   |
| 14_2 |          cVAE + Wconcat, W 生成那边的 `regu_loss * 1`, `cVAE_loss * 0.3`          |   85.55/6.77   |
| 14_3 |          cVAE + Wconcat, W 生成那边的 `regu_loss * 1`, `cVAE_loss * 0.4`          |   84.97/8.22   |
| 14_4 |          cVAE + Wconcat, W 生成那边的 `regu_loss * 1`, `cVAE_loss * 0.5`          |   86.08/7.28   |
| 14_5 |          cVAE + Wconcat, W 生成那边的 `regu_loss * 1`, `cVAE_loss * 0.6`          |   85.88/7.48   |
| 14_0 |         cVAE + Wconcat, W 生成那边的 `regu_loss * 1`, `cVAE_loss * 0.65`          |   85.54/6.98   |
| 14_6 |          cVAE + Wconcat, W 生成那边的 `regu_loss * 1`, `cVAE_loss * 0.7`          |   86.15/6.47   |
| 14_0 |         cVAE + Wconcat, W 生成那边的 `regu_loss * 1`, `cVAE_loss * 0.75`          |   85.79/6.57   |
| 14_7 |          cVAE + Wconcat, W 生成那边的 `regu_loss * 1`, `cVAE_loss * 0.8`          |   84.79/7.44   |
| 14_8 |          cVAE + Wconcat, W 生成那边的 `regu_loss * 1`, `cVAE_loss * 0.9`          |   84.15/8.18   |
|  15  |          cVAE + Wconcat, `WVAE * 0.5 + W, regu_loss * 1, cVAE_loss * 1`           |   86.87/7.21   |
| 说明 |                      以上（应该是到 11 吧），不是真正到 VAE                       |                |
|      |                用 `(PX+b)*Q` 生成两个 W，但没有用他们进一步生成 wi                |                |
|      |                后续 loss 继续把这两个 W 当作 mean，sigma 进行处理                 |                |
|      |                                                                                   |                |
| 以下 | 在最原始的代码基础上，`(PX+b)*Q`生成 W_original，然后随机生成两个 W_mean, W_sigma |                |
|      |          用 W_mean, W_sigma 随机生成一个 W_VAE，然后 W_original + W_VAE           |                |
|      |                             如无说明，`regu_loss * 1`                             |                |
|  16  |                                W_original + W_VAE                                 |   81.83/8.31   |
| 16_1 |                             `W_original + W_VAE*0.1`                              |   81.61/7.88   |
| 16_2 |                             `W_original + W_VAE*0.2`                              |   81.61/7.89   |
| 16_3 |                             `W_original + W_VAE*0.3`                              |   81.61/7.89   |
| 16_4 |                             `W_original + W_VAE*0.4`                              |   81.61/7.88   |
| 16_1 |                             `W_original + W_VAE*0.5`                              |   81.6/7.88    |
| 16_2 |                             `W_original + W_VAE*0.6`                              |   81.6/7.89    |
| 16_1 |                             `W_original + W_VAE*0.7`                              |   81.59/7.88   |
| 16_2 |                             `W_original + W_VAE*0.8`                              |   81.59/7.88   |
| 16_1 |                             `W_original + W_VAE*0.9`                              |   81.6/7.88    |
|  17  |       original W, VAE：用 FC 生成(输入 x，`x*10`),图卷积的结果 concat 起来        |                |
| 17_1 |                                  `regu_loss * 1`                                  |   86.04/7.78   |
| 17_1 |                                 `regu_loss * 20`                                  | **87.09/6.51** |

---

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

### model3

2020.2.2: IAG 模型加入 decoder，再加入一路分支，使用一个 W（5 个 band 使用自己的 W），把两路结果 concate 起来。
