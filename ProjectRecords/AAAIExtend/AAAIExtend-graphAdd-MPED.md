# MPED graph add

MPED

|    Model     | MPED Protocol 1(ACC/STD) | MPED Protocol 2(ACC/F1) | MPED Protocol 3(ACC/STD) |
| :----------: | :----------------------: | :---------------------: | :----------------------: |
|     IAG      |       74.77/10.75        |       73.58/68.41       |       40.38/08.75        |
| graph_concat |       74.72/10.91        |       74.13/67.83       |       40.40/09.35        |
|  grapn_add   |       74.71/12.48        |       74.04/67.38       |        40.47/9.13        |

### protocol-1

|     Model     |     Acc/std     |                    Note                     |    seed    | batchsize |
| :-----------: | :-------------: | :-----------------------------------------: | :--------: | :-------: |
|   IAG-paper   | **74.77/10.75** | 5W: [0.00001,0.00001,0.0001,0.0001,0.00001] |  no seed   |  no idea  |
|  IAG-reShow   |   72.82/11.55   | 5W: [0.00001,0.00001,0.0001,0.0001,0.00001] | np(18), 23 |    64     |
|  IAG-reShow   | **75.06/11.29** | 5W: [0.00001,0.00001,0.0001,0.0001,0.00001] | np(18), 23 |    32     |
|      --       |       --        |                     --                      |     --     |    --     |
|    IAG+VAE    | **74.7/12.49**  |                                             |  seed1823  |    32     |
| IAG+0.0001VAE |   73.91/12.47   |                                             |  seed1823  |    32     |
| IAG+0.0002VAE |   72.16/13.84   |                                             |  seed1823  |    32     |
| IAG+0.0003VAE |   72.51/13.64   |                                             |  seed1823  |    32     |
| IAG+0.0004VAE |   72.31/13.6    |                                             |  seed1823  |    32     |
| IAG+0.0005VAE |   72.18/13.62   |                                             |  seed1823  |    32     |
| IAG+0.0006VAE |   72.48/13.5    |                                             |  seed1823  |    32     |
| IAG+0.0007VAE |  72.14/13.43,   |                                             |  seed1823  |    32     |
| IAG+0.0008VAE |   72.67/13.74   |                                             |  seed1823  |    32     |
| IAG+0.0009VAE |   72.0/13.73    |                                             |  seed1823  |    32     |
| IAG+0.001VAE  |   73.45/12.8    |                                             |  seed1823  |    32     |
| IAG+0.002VAE  |   74.15/12.49   |                                             |  seed1823  |    32     |
| IAG+0.003VAE  |   73.93/12.26   |                                             |  seed1823  |    32     |
| IAG+0.004VAE  |   73.53/13.07   |                                             |  seed1823  |    32     |
| IAG+0.005VAE  | **74.26/12.06** |                                             |  seed1823  |    32     |
| IAG+0.006VAE  |   73.71/12.36   |                                             |  seed1823  |    32     |
| IAG+0.007VAE  |   73.55/13.12   |                                             |  seed1823  |    32     |
| IAG+0.008VAE  |   73.76/12.71   |                                             |  seed1823  |    32     |
| IAG+0.009VAE  |   73.91/13.01   |                                             |  seed1823  |    32     |
|  IAG+0.01VAE  |   73.82/12.32   |                                             |  seed1823  |    32     |
|  IAG+0.02VAE  |   73.72/12.67   |                                             |  seed1823  |    32     |
|  IAG+0.03VAE  |   74.19/12.49   |                                             |  seed1823  |    32     |
|  IAG+0.04VAE  |   73.79/12.83   |                                             |  seed1823  |    32     |
|  IAG+0.05VAE  |   73.92/13.07   |                                             |  seed1823  |    32     |
|  IAG+0.06VAE  |   73.72/12.69   |                                             |  seed1823  |    32     |
|  IAG+0.07VAE  |   73.9/12.98    |                                             |  seed1823  |    32     |
|  IAG+0.08VAE  |   74.01/13.03   |                                             |  seed1823  |    32     |
|  IAG+0.09VAE  | **74.35/12.21** |                                             |  seed1823  |    32     |
|  IAG+0.1VAE   |   74.04/13.1    |                                             |  seed1823  |    32     |
|  IAG+0.2VAE   |   74.12/12.2    |                                             |  seed1823  |    32     |
|  IAG+0.3VAE   |   73.52/13.03   |                                             |  seed1823  |    32     |
|  IAG+0.4VAE   |   73.7/12.07    |                                             |  seed1823  |    32     |
|  IAG+0.5VAE   | **74.53/12.28** |                                             |  seed1823  |    32     |
|  IAG+0.6VAE   |   74.16/12.97   |                                             |  seed1823  |    32     |
|  IAG+0.7VAE   | **74.31/12.42** |                                             |  seed1823  |    32     |
|  IAG+0.8VAE   |   73.91/13.32   |                                             |  seed1823  |    32     |
|  IAG+0.9VAE   | **74.36/12.78** |                                             |  seed1823  |    32     |
|    IAG+VAE    | **74.71/12.48** |                                             |   noseed   |    32     |
| IAG+0.005VAE  |   73.46/12.6    |                                             |   noseed   |    32     |
|  IAG+0.09VAE  |   73.29/12.89   |                                             |   noseed   |    32     |
|  IAG+0.5VAE   |   73.29/13.31   |                                             |   noseed   |    32     |
|  IAG+0.7VAE   |   74.34/12.82   |                                             |   noseed   |    32     |
|  IAG+0.9VAE   |   73.64/13.71   |                                             |   noseed   |    32     |

### protocol-2

|    Model     |     Acc/f1      |                    5W                    |    seed    | batchsize |
| :----------: | :-------------: | :--------------------------------------: | :--------: | :-------: |
|  IAG-paper   | **73.58/68.41** | [0.00001,0.00001,0.00001,0.0001,0.00001] |  no seed   |  no idea  |
|  IAG-reShow  |   72.45/66.71   | [0.00001,0.00001,0.00001,0.0001,0.00001] | np(18), 23 |    64     |
|  IAG-reShow  | **73.19/66.65** | [0.00001,0.00001,0.00001,0.0001,0.00001] | np(18), 23 |    32     |
|      --      |       --        |                    --                    |     --     |    --     |
|   IAG+VAE    |   73.54/66.97   |                                          |  seed1823  |    32     |
| IAG+0.001VAE | **73.97/67.68** |                                          |  seed1823  |    32     |
| IAG+0.002VAE |                 |                                          |  seed1823  |    32     |
| IAG+0.003VAE |                 |                                          |  seed1823  |    32     |
| IAG+0.004VAE |                 |                                          |  seed1823  |    32     |
| IAG+0.005VAE |                 |                                          |  seed1823  |    32     |
| IAG+0.006VAE |                 |                                          |  seed1823  |    32     |
| IAG+0.007VAE |                 |                                          |  seed1823  |    32     |
| IAG+0.008VAE |                 |                                          |  seed1823  |    32     |
| IAG+0.009VAE |                 |                                          |  seed1823  |    32     |
| IAG+0.01VAE  |   73.47/67.26   |                                          |  seed1823  |    32     |
| IAG+0.02VAE  |                 |                                          |  seed1823  |    32     |
| IAG+0.03VAE  |                 |                                          |  seed1823  |    32     |
| IAG+0.04VAE  |                 |                                          |  seed1823  |    32     |
| IAG+0.05VAE  |                 |                                          |  seed1823  |    32     |
| IAG+0.06VAE  |                 |                                          |  seed1823  |    32     |
| IAG+0.07VAE  |                 |                                          |  seed1823  |    32     |
| IAG+0.08VAE  |                 |                                          |  seed1823  |    32     |
| IAG+0.09VAE  |                 |                                          |  seed1823  |    32     |
|  IAG+0.1VAE  |   72.95/66.63   |                                          |  seed1823  |    32     |
|  IAG+0.2VAE  |   73.29/67.03   |                                          |  seed1823  |    32     |
|  IAG+0.3VAE  |   73.03/65.89   |                                          |  seed1823  |    32     |
|  IAG+0.4VAE  |   73.31/66.58   |                                          |  seed1823  |    32     |
|  IAG+0.5VAE  |   73.42/66.02   |                                          |  seed1823  |    32     |
|  IAG+0.6VAE  |   73.72/67.47   |                                          |  seed1823  |    32     |
|  IAG+0.7VAE  |   73.7/67.37    |                                          |  seed1823  |    32     |
|  IAG+0.8VAE  |   73.61/67.63   |                                          |  seed1823  |    32     |
|  IAG+0.9VAE  | **74.04/67.38** |                                          |  seed1823  |    32     |

### protocol-3

|     Model     |         Acc/std         |                    Note                     |    seed    | batchsize |
| :-----------: | :---------------------: | :-----------------------------------------: | :--------: | :-------: |
|   IAG-paper   |     **40.38/08.75**     | 5W:[0.00001,0.00001,0.0001,0.0001,0.00001]  |  no seed   |  no idea  |
|  IAG-reShow   |        38.3/9.7         | 5W: [0.00001,0.00001,0.0001,0.0001,0.00001] | np(18), 23 |    64     |
|  IAG-reShow   |     **39.77/8.54**      | 5W: [0.00001,0.00001,0.0001,0.0001,0.00001] | np(18), 23 |    32     |
|      --       |           --            |                     --                      |     --     |    --     |
|    IAG+VAE    |       38.51/8.37        |                                             |  seed1823  |    32     |
| IAG+0.0001VAE |       38.63/9.53        |                                             |  seed1823  |    32     |
| IAG+0.0002VAE |       39.35/9.34        |                                             |  seed1823  |    32     |
| IAG+0.0003VAE |        39.84/9.2        |                                             |  seed1823  |    32     |
| IAG+0.0004VAE |       39.28/9.41        |                                             |  seed1823  |    32     |
| IAG+0.0005VAE |        39.31/9.1        |                                             |  seed1823  |    32     |
| IAG+0.0006VAE |     **40.18/8.64**      |                                             |  seed1823  |    32     |
| IAG+0.0007VAE |       39.65/9.42        |                                             |  seed1823  |    32     |
| IAG+0.0008VAE |       39.09/9.42        |                                             |  seed1823  |    32     |
| IAG+0.0009VAE |       39.79/9.38        |                                             |  seed1823  |    32     |
| IAG+0.001VAE  |       39.47/9.67        |                                             |  seed1823  |    32     |
| IAG+0.002VAE  |       39.45/9.38        |                                             |  seed1823  |    32     |
| IAG+0.003VAE  |       39.48/10.08       |                                             |  seed1823  |    32     |
| IAG+0.004VAE  |       39.47/9.79        |                                             |  seed1823  |    32     |
| IAG+0.005VAE  |       39.33/8.76        |                                             |  seed1823  |    32     |
| IAG+0.006VAE  |       39.22/9.57        |                                             |  seed1823  |    32     |
| IAG+0.007VAE  |        39.45/8.7        |                                             |  seed1823  |    32     |
| IAG+0.008VAE  |       39.29/10.25       |                                             |  seed1823  |    32     |
| IAG+0.009VAE  |     **40.24/9.48**      |                                             |  seed1823  |    32     |
|  IAG+0.01VAE  |       39.45/9.58        |                                             |  seed1823  |    32     |
|  IAG+0.02VAE  |       39.07/9.13        |                                             |  seed1823  |    32     |
|  IAG+0.03VAE  |     **40.47/9.13**      |                                             |  seed1823  |    32     |
|  IAG+0.04VAE  |       39.39/9.17        |                                             |  seed1823  |    32     |
|  IAG+0.05VAE  |       39.61/9.64        |                                             |  seed1823  |    32     |
|  IAG+0.06VAE  |       39.94/9.36        |                                             |  seed1823  |    32     |
|  IAG+0.07VAE  |       39.09/9.41        |                                             |  seed1823  |    32     |
|  IAG+0.08VAE  |     **40.08/8.54**      |                                             |  seed1823  |    32     |
|  IAG+0.09VAE  |     **40.08/10.16**     |                                             |  seed1823  |    32     |
|  IAG+0.1VAE   |      **40.17/8.4**      |                                             |  seed1823  |    32     |
|  IAG+0.2VAE   |       38.89/9.05        |                                             |  seed1823  |    32     |
|  IAG+0.3VAE   |       38.88/9.07        |                                             |  seed1823  |    32     |
|  IAG+0.4VAE   |       39.22/8.57        |                                             |  seed1823  |    32     |
|  IAG+0.5VAE   |       39.45/8.67        |                                             |  seed1823  |    32     |
|  IAG+0.6VAE   |       39.14/8.87        |                                             |  seed1823  |    32     |
|  IAG+0.7VAE   |       38.52/9.19        |                                             |  seed1823  |    32     |
|  IAG+0.8VAE   |       39.04/8.88        |                                             |  seed1823  |    32     |
|  IAG+0.9VAE   |       38.23/8.32        |                                             |  seed1823  |    32     |
| IAG+0.009VAE  |       38.51/9.78        |                                             |   noseed   |    32     |
|  IAG+0.03VAE  |       38.12/8.23        |                                             |   noseed   |    32     |
|  IAG+0.08VAE  |        38.76/9.9        |                                             |   noseed   |    32     |
|  IAG+0.09VAE  |       38.16/9.57        |                                             |   noseed   |    32     |
|  IAG+0.1VAE   |        40.07/9.8        |                                             |   noseed   |    32     |
| IAG+0.009VAE  | 39.06/9.44,39.17/10.96  |                                             |   noseed   |    32     |
|  IAG+0.03VAE  | 39.39/11.92,39.66/10.31 |                                             |   noseed   |    32     |
|  IAG+0.08VAE  | 38.54/11.69,38.92/10.23 |                                             |   noseed   |    32     |
|  IAG+0.09VAE  |  39.05/11.08,38.6/9.25  |                                             |   noseed   |    32     |
|  IAG+0.1VAE   | 38.72/11.06,37.41/10.51 |                                             |   noseed   |    32     |
| IAG+0.0095VAE |        39.3/9.7         |                                             |  seed1823  |    32     |
| IAG+0.0085VAE |       38.58/9.17        |                                             |  seed1823  |    32     |
| IAG+0.025VAE  |       39.81/9.11        |                                             |  seed1823  |    32     |
| IAG+0.035VAE  |       39.84/9.05        |                                             |  seed1823  |    32     |
| IAG+0.075VAE  |        39.6/9.43        |                                             |  seed1823  |    32     |
| IAG+0.085VAE  |       39.59/10.56       |                                             |  seed1823  |    32     |
| IAG+0.095VAE  |       39.14/9.51        |                                             |  seed1823  |    32     |
|  IAG+0.15VAE  |       39.57/9.74        |                                             |  seed1823  |    32     |
