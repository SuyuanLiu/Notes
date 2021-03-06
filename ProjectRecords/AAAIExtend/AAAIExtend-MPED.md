# MPED 结果记录

Index

- [protocol-1](#protocol-1)
- [protocol-2](#protocol-2)
- [protocol-3](#protocol-3)

MPED 的代码，以下实验都是基于`IAG_loss * 0.01`。

注：分割线后的 VAE+IAG 模型，做过以下修改：

- `relu(W_mean, W_sigma)`
- `VAE: W_i .... tf.square`
- `VAE_loss: mean --> sum`

MPED

|   Model    | MPED Protocol 1(ACC/STD) | MPED Protocol 2(ACC/F1) | MPED Protocol 3(ACC/STD) |
| :--------: | :----------------------: | :---------------------: | :----------------------: |
|    IAG     |       74.77/10.75        |       73.58/68.41       |       40.38/08.75        |
| new_method |       74.72/10.91        |       74.13/67.83       |       40.40/09.35        |

### protocol-1

|     Model     |     Acc/std     |                    Note                     |    seed    | batchsize |
| :-----------: | :-------------: | :-----------------------------------------: | :--------: | :-------: |
|   IAG-paper   | **74.77/10.75** | 5W: [0.00001,0.00001,0.0001,0.0001,0.00001] |  no seed   |  no idea  |
|  IAG-reShow   |   72.82/11.55   | 5W: [0.00001,0.00001,0.0001,0.0001,0.00001] | np(18), 23 |    64     |
|  IAG-reShow   | **75.06/11.29** | 5W: [0.00001,0.00001,0.0001,0.0001,0.00001] | np(18), 23 |    32     |
|      --       |       --        |                     --                      |     --     |    --     |
| IAG+0.001VAE  | **74.0/12.85**  |                                             |  seed1823  |    32     |
| IAG+0.002VAE  |   73.81/12.68   |                                             |  seed1823  |    32     |
| IAG+0.003VAE  |   73.78/13.0    |                                             |  seed1823  |    32     |
| IAG+0.004VAE  | **74.08/12.61** |                                             |  seed1823  |    32     |
| IAG+0.005VAE  |   73.66/12.96   |                                             |  seed1823  |    32     |
| IAG+0.006VAE  |   73.83/12.52   |                                             |  seed1823  |    32     |
| IAG+0.007VAE  |   73.39/12.61   |                                             |  seed1823  |    32     |
| IAG+0.008VAE  | **74.15/12.28** |                                             |  seed1823  |    32     |
| IAG+0.009VAE  | **74.16/12.71** |                                             |  seed1823  |    32     |
| IAG+0.0001VAE |   73.37/12.5    |                                             |  seed1823  |    32     |
| IAG+0.0002VAE |   73.63/13.12   |                                             |  seed1823  |    32     |
| IAG+0.0003VAE |   73.65/13.1    |                                             |  seed1823  |    32     |
| IAG+0.0004VAE |   73.77/12.82   |                                             |  seed1823  |    32     |
| IAG+0.0005VAE |   73.94/12.76   |                                             |  seed1823  |    32     |
| IAG+0.0006VAE |   73.7/12.83    |                                             |  seed1823  |    32     |
| IAG+0.0007VAE |   73.88/12.8    |                                             |  seed1823  |    32     |
| IAG+0.0008VAE |   73.54/13.28   |                                             |  seed1823  |    32     |
| IAG+0.0009VAE |   73.59/13.0    |                                             |  seed1823  |    32     |
| IAG+0.004VAE  |   73.45/12.58   |                                             |   noseed   |    32     |
| IAG+0.008VAE  |                 |                                             |   noseed   |    32     |
| IAG+0.009VAE  |                 |                                             |   noseed   |    32     |

### protocol-3

|     Model     |        Acc/std         |                    Note                     |    seed    | batchsize |
| :-----------: | :--------------------: | :-----------------------------------------: | :--------: | :-------: |
|   IAG-paper   |    **40.38/08.75**     | 5W:[0.00001,0.00001,0.0001,0.0001,0.00001]  |  no seed   |  no idea  |
|  IAG-reShow   |        38.3/9.7        | 5W: [0.00001,0.00001,0.0001,0.0001,0.00001] | np(18), 23 |    64     |
|  IAG-reShow   |     **39.77/8.54**     | 5W: [0.00001,0.00001,0.0001,0.0001,0.00001] | np(18), 23 |    32     |
|      --       |           --           |                     --                      |     --     |    --     |
| IAG+0.001VAE  |     **39.92/9.07**     |                                             |  seed1823  |    32     |
| IAG+0.002VAE  |     **39.74/8.68**     |                                             |  seed1823  |    32     |
| IAG+0.003VAE  |     **39.81/9.31**     |                                             |  seed1823  |    32     |
| IAG+0.004VAE  |       39.39/8.38       |                                             |  seed1823  |    32     |
| IAG+0.005VAE  |       39.64/8.39       |                                             |  seed1823  |    32     |
| IAG+0.006VAE  |       38.92/9.5        |                                             |  seed1823  |    32     |
| IAG+0.007VAE  |       38.39/9.24       |                                             |  seed1823  |    32     |
| IAG+0.008VAE  |       39.7/9.44        |                                             |  seed1823  |    32     |
| IAG+0.009VAE  |       39.3/9.49        |                                             |  seed1823  |    32     |
| IAG+0.0001VAE |       38.81/9.18       |                                             |  seed1823  |    32     |
| IAG+0.0002VAE |       38.93/8.98       |                                             |  seed1823  |    32     |
| IAG+0.0003VAE |       39.37/9.47       |                                             |  seed1823  |    32     |
| IAG+0.0004VAE |       39.5/9.61        |                                             |  seed1823  |    32     |
| IAG+0.0005VAE |       39.52/9.59       |                                             |  seed1823  |    32     |
| IAG+0.0006VAE |       39.51/8.71       |                                             |  seed1823  |    32     |
| IAG+0.0007VAE |       39.34/9.06       |                                             |  seed1823  |    32     |
| IAG+0.0008VAE |       39.16/9.27       |                                             |  seed1823  |    32     |
| IAG+0.0009VAE |       39.3/8.94        |                                             |  seed1823  |    32     |
| IAG+0.001VAE  | 39.11/9.86，39.53/9.16 |                                             |   noseed   |    32     |
| IAG+0.002VAE  | 38.64/9.89，39.49/8.66 |                                             |   noseed   |    32     |
| IAG+0.003VAE  | 39.34/9.03，38.56/9.57 |                                             |   noseed   |    32     |

### 加入 regu_loss

```
regu_loss_weight = 20
```

sub1,2 的结果比较好，但是后面的结果就很差，在调试参数时，应当以后面为准。（可以先看 3，4）

| protocol |   model    |     Acc/Std     | regu_loss_weight | VAE_loss_weight | seed | Note |
| :------: | :--------: | :-------------: | :--------------: | :-------------: | :--: | :--: |
|    1     | IAG+1.0AVE |   72.18/13.02   |        20        |      0.01       | yes  |      |
|    1     | IAG+1.0AVE |   71.62/13.2    |        20        |       0.1       | yes  |      |
|    1     | IAG+1.0AVE |   73.25/13.04   |       0.5        |      0.01       | yes  |      |
|    1     | IAG+1.0AVE |   73.12/13.04   |       0.5        |       0.1       | yes  |      |
|    1     | IAG+1.0AVE |   73.11/13.3    |       0.5        |       1.0       | yes  |      |
|    1     | IAG+1.0AVE | **73.88/12.88** |        1         |      0.01       | yes  |      |
|    1     | IAG+1.0AVE |   73.72/13.27   |        1         |       0.1       | yes  |      |
|    1     | IAG+1.0AVE |   73.77/12.87   |        1         |       1.0       | yes  |      |

| protocol |   model    |  Acc/Std   | regu_loss_weight | VAE_loss_weight | seed | Note |
| :------: | :--------: | :--------: | :--------------: | :-------------: | :--: | :--: |
|    2     | IAG+0.6AVE | 70.88/9.77 |        20        |      0.01       | yes  |      |
|    2     | IAG+0.6AVE | 70.53/9.77 |        20        |       0.1       | yes  |      |

| protocol |    model    |       Acc/Std        | regu_loss_weight | VAE_loss_weight | seed | Note |
| :------: | :---------: | :------------------: | :--------------: | :-------------: | :--: | :--: |
|    3     | IAG+0.05AVE |     36.75/11.52      |        20        |      0.01       | yes  |      |
|    3     | IAG+0.05AVE |     36.99/11.47      |        20        |       0.1       | yes  |      |
|    3     | IAG+0.07AVE |     **39.4/9.0**     |       0.5        |      0.01       | yes  |      |
|    3     | IAG+0.07AVE |      37.65/9.54      |       0.5        |       0.1       | yes  |      |
|    3     | IAG+0.07AVE |      37.49/10.0      |       0.5        |       1.0       | yes  |      |
|    3     | IAG+0.07AVE |      39.32/9.2       |        1         |      0.01       | yes  |      |
|    3     | IAG+0.07AVE |     38.49/10.67      |        1         |       0.1       | yes  |      |
|    3     | IAG+0.07AVE |     38.21/10.99      |        1         |       1.0       | yes  |      |
|    3     | IAG+0.07AVE |     37.75/10.64      |       0.1        |      0.01       | yes  |      |
|    3     | IAG+0.07AVE |      37.76/8.9       |       0.1        |       0.1       | yes  |      |
|    3     | IAG+0.07AVE |      37.02/9.16      |       0.1        |       1.0       | yes  |      |
|    3     | IAG+0.07AVE |      37.91/9.89      |       0.01       |       1.0       | yes  |      |
|    3     | IAG+0.07AVE | 38.1/8.5, 38.52/9.24 |       0.5        |      0.01       |  no  |      |

### protocol-1

|    Model     |               Acc/std               |                    Note                     |    seed    | batchsize |
| :----------: | :---------------------------------: | :-----------------------------------------: | :--------: | :-------: |
|  IAG-paper   |           **74.77/10.75**           | 5W: [0.00001,0.00001,0.0001,0.0001,0.00001] |  no seed   |  no idea  |
|  IAG-reShow  |             72.82/11.55             | 5W: [0.00001,0.00001,0.0001,0.0001,0.00001] | np(18), 23 |    64     |
|  IAG-reShow  |           **75.06/11.29**           | 5W: [0.00001,0.00001,0.0001,0.0001,0.00001] | np(18), 23 |    32     |
|      --      |                 --                  |                     --                      |     --     |    --     |
|   IAG+VAE    |           **74.39/12.49**           |                                             |  no seed   |    32     |
| IAG+0.01VAE  |             73.39/13.05             |                                             |  no seed   |    32     |
| IAG+0.02VAE  |             73.86/12.29             |                                             |  no seed   |    32     |
| IAG+0.03VAE  |           **74.04/12.29**           |                                             |  no seed   |    32     |
| IAG+0.04VAE  |           **73.84/12.59**           |                                             |  no seed   |    32     |
| IAG+0.05VAE  |           **74.15/12.85**           |                                             |  no seed   |    32     |
| IAG+0.06VAE  |             73.77/12.82             |                                             |  no seed   |    32     |
| IAG+0.07VAE  |             73.81/13.21             |                                             |  no seed   |    32     |
| IAG+0.08VAE  |             73.26/12.54             |                                             |  no seed   |    32     |
| IAG+0.09VAE  |             73.57/12.49             |                                             |  no seed   |    32     |
|  IAG+0.1VAE  |             73.54/13.0              |                                             | np(18), 23 |    32     |
|  IAG+0.2VAE  |             73.74/12.91             |                                             | np(18), 23 |    32     |
|  IAG+0.3VAE  |             73.6/12.81              |                                             | np(18), 23 |    32     |
|  IAG+0.4VAE  |             73.4/12.29              |                                             | np(18), 23 |    32     |
|  IAG+0.5VAE  |             73.51/13.18             |                                             | np(18), 23 |    32     |
|  IAG+0.6VAE  |             73.53/13.09             |                                             | np(18), 23 |    32     |
|  IAG+0.7VAE  |             73.52/13.03             |                                             | np(18), 23 |    32     |
|  IAG+0.8VAE  |           **73.92/11.93**           |                                             | np(18), 23 |    32     |
|  IAG+0.9VAE  |           **73.95/12.5**            |                                             | np(18), 23 |    32     |
|   IAG+VAE    |          **74.34/12.23**,           |                                             |  no seed   |    32     |
| IAG+0.03VAE  |      73.49/12.69, 73.89/12.87       |                                             |  no seed   |    32     |
| IAG+0.05VAE  |          **74.07/12.74**,           |                                             |  no seed   |    32     |
| IAG+0.06VAE  |            73.71/12.26,             |                                             |  no seed   |    32     |
| IAG+0.07VAE  |      72.71/13.38, 73.77/12.55       |                                             |  no seed   |    32     |
|  IAG+0.2VAE  |    73.63/13.12, **73.95/12.88**     |                                             |  no seed   |    32     |
|              |                                     |                                             |            |           |
|   IAG+VAE    |     **74.72/10.91**,73.74/13.26     |                                             |  no seed   |    32     |
| IAG+0.03VAE  |       74.35/12.48,73.51/13.29       |                                             |  no seed   |    32     |
| IAG+0.04VAE  |       73.92/12.68,73.95/12.17       |                                             |  no seed   |    32     |
| IAG+0.05VAE  |       73.6/13.13, 74.22/12.82       |                                             |  no seed   |    32     |
|  IAG+0.2VAE  |       73.49/12.32, 73.56/12.5       |                                             |  no seed   |    32     |
|  IAG+0.8VAE  |       74.0/12.53, 73.93/13.35       |                                             |  no seed   |    32     |
|  IAG+0.9VAE  |       74.23/12.49, 73.5/12.92       |                                             |  no seed   |    32     |
| IAG+0.03VAE  | 73.01/13.27,73.59/12.89,73.51/12.31 |                                             |  no seed   |    32     |
| IAG+0.04VAE  | 73.34/13.27,73.66/12.71,73.3/12.94  |                                             |  no seed   |    32     |
| IAG+0.05VAE  | 74.35/12.47,73.53/13.15,73.55/12.96 |                                             |  no seed   |    32     |
| IAG+0.03VAE  |             73.82/13.5              |                                             |  no seed   |    32     |
| IAG+0.05VAE  |             73.39/13.26             |                                             |  no seed   |    32     |
| IAG+0.003VAE |             73.38/12.6              |                                             |  no seed   |    32     |
| IAG+0.005VAE |             73.27/13.16             |                                             |  no seed   |    32     |
| IAG+0.001VAE |                                     |                                             |  seed1823  |    32     |
| IAG+0.002VAE |                                     |                                             |  seed1823  |    32     |
| IAG+0.003VAE |                                     |                                             |  seed1823  |    32     |
| IAG+0.004VAE |                                     |                                             |  seed1823  |    32     |
| IAG+0.005VAE |                                     |                                             |  seed1823  |    32     |
| IAG+0.006VAE |                                     |                                             |  seed1823  |    32     |
| IAG+0.007VAE |                                     |                                             |  seed1823  |    32     |
| IAG+0.008VAE |                                     |                                             |  seed1823  |    32     |
| IAG+0.009VAE |                                     |                                             |  seed1823  |    32     |

### protocol-3

|    Model     |                Acc/std                |                    Note                     |    seed    | batchsize |
| :----------: | :-----------------------------------: | :-----------------------------------------: | :--------: | :-------: |
|  IAG-paper   |            **40.38/08.75**            | 5W:[0.00001,0.00001,0.0001,0.0001,0.00001]  |  no seed   |  no idea  |
|  IAG-reShow  |               38.3/9.7                | 5W: [0.00001,0.00001,0.0001,0.0001,0.00001] | np(18), 23 |    64     |
|  IAG-reShow  |            **39.77/8.54**             | 5W: [0.00001,0.00001,0.0001,0.0001,0.00001] | np(18), 23 |    32     |
|      --      |                  --                   |                     --                      |     --     |    --     |
|   IAG+VAE    |                                       |                                             |  no seed   |    32     |
| IAG+0.01VAE  |  38.5/10.11, 39.23/10.51, 39.03/9.99  |                                             |  no seed   |    32     |
| IAG+0.02VAE  |  39.17/10.2, 39.46/9.4, 38.78/10.29   |                                             |  no seed   |    32     |
| IAG+0.03VAE  |   38.48/9.1, 39.51/9.68, 39.11/7.78   |                                             |  no seed   |    32     |
| IAG+0.04VAE  | 38.12/9.35, **40.24/9.66**,38.74/9.99 |                                             |  no seed   |    32     |
| IAG+0.05VAE  |   38.34/9.84, 38.85/8.81,38.17/9.48   |                                             |  no seed   |    32     |
| IAG+0.06VAE  | **40.23/8.56**, 38.81/9.1,38.43/9.45  |                                             |  no seed   |    32     |
| IAG+0.07VAE  |  39.46/9.0, **40.4/9.35**,38.56/9.04  |                                             |  no seed   |    32     |
| IAG+0.08VAE  |   38.47/8.82, 39.05/10.08,38.6/8.89   |                                             |  no seed   |    32     |
| IAG+0.09VAE  | 39.39/9.74, **40.09/9.7**,39.19/9.47  |                                             |  no seed   |    32     |
|  IAG+0.1VAE  |      **40.32/7.8**, 39.58/10.14       |                                             |  no seed   |    32     |
|  IAG+0.2VAE  |  38.89/9.46, 39.02/8.58, 38.85/9.68   |                                             |  no seed   |    32     |
|  IAG+0.3VAE  |        38.52/9.74, 38.55/9.83         |                                             |  no seed   |    32     |
|  IAG+0.4VAE  |        38.64/9.24, 39.66/10.02        |                                             |  no seed   |    32     |
|  IAG+0.5VAE  |  38.83/10.11, 39.34/9.72,38.87/9.87   |                                             |  no seed   |    32     |
|  IAG+0.6VAE  |        39.55/7.92, 38.85/9.42         |                                             |  no seed   |    32     |
|  IAG+0.7VAE  |        39.55/8.91, 39.17/10.06        |                                             |  no seed   |    32     |
|  IAG+0.8VAE  |        39.06/9.86, 38.53/9.38         |                                             |  no seed   |    32     |
|  IAG+0.9VAE  |  39.64/8.73, 39.51/10.28,39.25/9.15   |                                             |  no seed   |    32     |
|              |                                       |                                             |            |           |
| IAG+0.04VAE  |         38.4/9.79, 39.55/9.37         |                                             |  no seed   |    32     |
| IAG+0.06VAE  |         39.19/9.3, 39.98/9.32         |                                             |  no seed   |    32     |
| IAG+0.07VAE  |         39.26/9.32,38.36/9.3          |                                             |  no seed   |    32     |
| IAG+0.09VAE  |              39.56/9.34,              |                                             |  no seed   |    32     |
|  IAG+0.1VAE  |        38.63/9.61, 39.43/9.08         |                                             |  no seed   |    32     |
|              |                                       |                                             |            |           |
|   IAG+VAE    |   39.61/9.21,39.28/10.26,39.96/8.89   |                                             |  no seed   |    32     |
| IAG+0.04VAE  |        38.34/10.08, 38.76/8.54        |                                             |  no seed   |    32     |
| IAG+0.06VAE  |              38.78/10.36              |                                             |  no seed   |    32     |
| IAG+0.07VAE  |              39.06/9.17               |                                             |  no seed   |    32     |
| IAG+0.09VAE  |                                       |                                             |  no seed   |    32     |
| IAG+0.04VAE  |        39.18/10.46,39.76/10.66        |                                             |  no seed   |    32     |
| IAG+0.06VAE  |         37.9/9.55,39.4/10.37          |                                             |  no seed   |    32     |
| IAG+0.07VAE  |   38.65/9.22,39.02/10.03,37.99/9.6    |                                             |  no seed   |    32     |
| IAG+0.09VAE  |   39.43/9.85,39.45/8.02,38.05/9.66    |                                             |  no seed   |    32     |
|  IAG+0.1VAE  |   39.72/9.17,38.61/9.18,39.32/10.19   |                                             |  no seed   |    32     |
| IAG+0.003VAE |         39.51/9.09,38.51/9.96         |                                             |  no seed   |    32     |
| IAG+0.005VAE |   38.66/8.64,38.56/9.13, 38.63/9.77   |                                             |  no seed   |    32     |
| IAG+0.007VAE |         38.84/8.68,40.01/9.46         |                                             |  no seed   |    32     |
| IAG+0.009VAE |          39.2/8.62,37.7/8.59          |                                             |  no seed   |    32     |
| IAG+0.07VAE  |  39.47/9.78,38.86/10.96,38.88/10.24   |                                             |  no seed   |    32     |
| IAG+0.09VAE  |   39.39/10.59,38.52/8.83,38.94/9.62   |                                             |  no seed   |    32     |
| IAG+0.09VAE  |              39.34/9.01               |                                             |  no seed   |    32     |

---

### protocol-1-

|    Model    |         Acc/std          |                    Note                     |    seed    | batchsize |
| :---------: | :----------------------: | :-----------------------------------------: | :--------: | :-------: |
|  IAG-paper  |     **74.77/10.75**      | 5W: [0.00001,0.00001,0.0001,0.0001,0.00001] |  no seed   |  no idea  |
| IAG-reShow  |       72.82/11.55        | 5W: [0.00001,0.00001,0.0001,0.0001,0.00001] | np(18), 23 |    64     |
| IAG-reShow  |     **75.06/11.29**      | 5W: [0.00001,0.00001,0.0001,0.0001,0.00001] | np(18), 23 |    32     |
|     --      |            --            |                     --                      |     --     |    --     |
|   IAG+VAE   |     **74.39/12.49**      |                                             |  no seed   |    32     |
| IAG+0.01VAE |       73.39/13.05        |                                             |  no seed   |    32     |
| IAG+0.02VAE |       73.86/12.29        |                                             |  no seed   |    32     |
| IAG+0.03VAE |     **74.04/12.29**      |                                             |  no seed   |    32     |
| IAG+0.04VAE |       73.84/12.59        |                                             |  no seed   |    32     |
| IAG+0.05VAE |     **74.15/12.85**      |                                             |  no seed   |    32     |
| IAG+0.06VAE |     **73.77/12.82**      |                                             |  no seed   |    32     |
| IAG+0.07VAE |     **73.81/13.21**      |                                             |  no seed   |    32     |
| IAG+0.08VAE |       73.26/12.54        |                                             |  no seed   |    32     |
| IAG+0.09VAE |       73.57/12.49        |                                             |  no seed   |    32     |
| IAG+0.1VAE  |        73.54/13.0        |                                             | np(18), 23 |    32     |
| IAG+0.2VAE  |     **73.74/12.91**      |                                             | np(18), 23 |    32     |
| IAG+0.3VAE  |        73.6/12.81        |                                             | np(18), 23 |    32     |
| IAG+0.4VAE  |        73.4/12.29        |                                             | np(18), 23 |    32     |
| IAG+0.5VAE  |       73.51/13.18        |                                             | np(18), 23 |    32     |
| IAG+0.6VAE  |       73.53/13.09        |                                             | np(18), 23 |    32     |
| IAG+0.7VAE  |       73.52/13.03        |                                             | np(18), 23 |    32     |
| IAG+0.8VAE  |       73.92/11.93        |                                             | np(18), 23 |    32     |
| IAG+0.9VAE  |        73.95/12.5        |                                             | np(18), 23 |    32     |
|   IAG+VAE   |     **74.34/12.23**,     |                                             |  no seed   |    32     |
| IAG+0.03VAE | 73.49/12.69, **running** |                                             |  no seed   |    32     |
| IAG+0.05VAE |     **74.07/12.74**,     |                                             |  no seed   |    32     |
| IAG+0.06VAE |       73.71/12.26,       |                                             |  no seed   |    32     |
| IAG+0.07VAE | 72.71/13.38, 73.77/12.55 |                                             |  no seed   |    32     |
| IAG+0.2VAE  | 73.63/13.12, **running** |                                             |  no seed   |    32     |

### protocol-2-

|    Model    |          Acc/f1          |                    5W                    |    seed    | batchsize |
| :---------: | :----------------------: | :--------------------------------------: | :--------: | :-------: |
|  IAG-paper  |     **73.58/68.41**      | [0.00001,0.00001,0.00001,0.0001,0.00001] |  no seed   |  no idea  |
| IAG-reShow  |       72.45/66.71        | [0.00001,0.00001,0.00001,0.0001,0.00001] | np(18), 23 |    64     |
| IAG-reShow  |     **73.19/66.65**      | [0.00001,0.00001,0.00001,0.0001,0.00001] | np(18), 23 |    32     |
|     --      |            --            |                    --                    |     --     |    --     |
|   IAG+VAE   |     **73.64/68.46**      |                                          |  no seed   |    32     |
|   IAG+VAE   |     **73.85/67.19**      |                                          | np(18), 23 |    32     |
| IAG+0.01VAE |       73.02/67.24        |                                          |  no seed   |    32     |
| IAG+0.02VAE |       73.38/66.79        |                                          |  no seed   |    32     |
| IAG+0.03VAE |       72.37/65.39        |                                          |  no seed   |    32     |
| IAG+0.04VAE |     **73.67/68.10**      |                                          |  no seed   |    32     |
| IAG+0.04VAE |     **73.74/67.02**      |                                          | np(18), 23 |    32     |
| IAG+0.05VAE |       72.83/66.21        |                                          |  no seed   |    32     |
| IAG+0.06VAE |       72.39/66.33        |                                          |  no seed   |    32     |
| IAG+0.07VAE |        72.9/66.35        |                                          |  no seed   |    32     |
| IAG+0.08VAE |       72.77/65.04        |                                          |  no seed   |    32     |
| IAG+0.09VAE |       73.29/66.81        |                                          |  no seed   |    32     |
| IAG+0.1VAE  |       72.73/67.35        |                                          |  no seed   |    32     |
| IAG+0.2VAE  |       73.18/66.82        |                                          |  no seed   |    32     |
| IAG+0.3VAE  |       72.34/65.17        |                                          |  no seed   |    32     |
| IAG+0.4VAE  |       73.41/66.28        |                                          |  no seed   |    32     |
| IAG+0.5VAE  |        73.35/67.9        |                                          |  no seed   |    32     |
| IAG+0.6VAE  |     **73.53/65.61**      |                                          |  no seed   |    32     |
| IAG+0.6VAE  |     **74.13/67.83**      |                                          | np(18), 23 |    32     |
| IAG+0.7VAE  |       72.35/66.12        |                                          |  no seed   |    32     |
| IAG+0.8VAE  |       73.24/66.97        |                                          |  no seed   |    32     |
| IAG+0.9VAE  |        72.7/66.62        |                                          |  no seed   |    32     |
|   IAG+VAE   | 72.94/66.28，72.12/66.18 |                                          |  no seed   |    32     |
| IAG+0.04VAE | 73.09/66.52，71.72/64.8  |                                          |  no seed   |    32     |
| IAG+0.6VAE  | 72.45/65.85，72.83/65.91 |                                          |  no seed   |    32     |

### protocol-3-

|    Model    |          Acc/std          |                    Note                     |    seed    | batchsize |
| :---------: | :-----------------------: | :-----------------------------------------: | :--------: | :-------: |
|  IAG-paper  |      **40.38/08.75**      | 5W:[0.00001,0.00001,0.0001,0.0001,0.00001]  |  no seed   |  no idea  |
| IAG-reShow  |         38.3/9.7          | 5W: [0.00001,0.00001,0.0001,0.0001,0.00001] | np(18), 23 |    64     |
| IAG-reShow  |      **39.77/8.54**       | 5W: [0.00001,0.00001,0.0001,0.0001,0.00001] | np(18), 23 |    32     |
|     --      |            --             |                     --                      |     --     |    --     |
|   IAG+VAE   |        39.19/9.63         |                                             |  no seed   |    32     |
| IAG+0.01VAE |      **39.64/9.83**       |                                             |  no seed   |    32     |
| IAG+0.02VAE |        37.41/9.24         |                                             |  no seed   |    32     |
| IAG+0.03VAE |        38.52/9.43         |                                             |  no seed   |    32     |
| IAG+0.04VAE |        37.95/9.87         |                                             |  no seed   |    32     |
| IAG+0.05VAE |      **39.95/8.17**       |                                             |  no seed   |    32     |
| IAG+0.05VAE |        39.39/8.76         |                                             | np(18), 23 |    32     |
| IAG+0.06VAE |         38.6/8.97         |                                             |  no seed   |    32     |
| IAG+0.07VAE |      **40.12/9.83**       |                                             |  no seed   |    32     |
| IAG+0.07VAE |         39.32/9.2         |                                             | np(18), 23 |    32     |
| IAG+0.08VAE |      **39.82/8.82**       |                                             |  no seed   |    32     |
| IAG+0.09VAE |        38.99/9.58         |                                             |  no seed   |    32     |
| IAG+0.1VAE  |        38.72/8.97         |                                             |  no seed   |    32     |
| IAG+0.2VAE  |        38.72/9.86         |                                             |  no seed   |    32     |
| IAG+0.3VAE  |      **40.03/9.75**       |                                             |  no seed   |    32     |
| IAG+0.4VAE  |        38.37/9.63         |                                             |  no seed   |    32     |
| IAG+0.5VAE  |        39.49/9.14         |                                             |  no seed   |    32     |
| IAG+0.6VAE  |      **40.27/9.44**       |                                             |  no seed   |    32     |
| IAG+0.6VAE  |        39.09/9.51         |                                             | np(18), 23 |    32     |
| IAG+0.7VAE  |        39.25/9.97         |                                             |  no seed   |    32     |
| IAG+0.8VAE  |        39.09/10.11        |                                             |  no seed   |    32     |
| IAG+0.9VAE  |         38.28/9.4         |                                             |  no seed   |    32     |
| IAG+0.05VAE | 38.65/10.11, 38.65/10.12  |                                             |  no seed   |    32     |
| IAG+0.07VAE | 38.53/9.3, **40.18/8.98** |                                             |  no seed   |    32     |
| IAG+0.6VAE  |  39.08/8.69, 39.81/9.69   |                                             |  no seed   |    32     |
| IAG+0.01VAE |  38.94/9.51, 38.91/9.75   |                                             |  no seed   |    32     |
| IAG+0.05VAE |  38.15/9.34, 38.88/10.24  |                                             |  no seed   |    32     |
| IAG+0.07VAE |  39.81/8.75,39.02/10.09   |                                             |  no seed   |    32     |
| IAG+0.08VAE |  37.96/9.08, 38.66/9.71   |                                             |  no seed   |    32     |
| IAG+0.3VAE  |  39.49/10.57, 38.44/9.53  |                                             |  no seed   |    32     |
| IAG+0.6VAE  |  39.07/9.99, 39.09/9.44   |                                             |  no seed   |    32     |
