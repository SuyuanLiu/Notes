# SEED

SEED 汇总

|    Model     |         非跨人         |    跨人    |
| :----------: | :--------------------: | :--------: |
|     IAG      |      95.44/05.48       | 86.30/6.91 |
| graph_concat | 96.44/4.24, 95.64/5.08 | 88.38/4.8  |
|  graph_add   |       95.25/5.19       | 87.54/6.92 |

### SEED 非跨人

|    Model     |     Acc/std     |              Note              | bs  | seed |
| :----------: | :-------------: | :----------------------------: | :-: | :--: |
|     IAG      | **95.44/05.48** |                                |     |      |
|      -       |        -        |               -                |  -  |      |
|   IAG+VAE    |    94.1/5.94    | `10 * VAE_loss,20 * regu_loss` | 32  | yes  |
| IAG+0.001VAE |    93.88/6.5    | `10 * VAE_loss,20 * regu_loss` | 32  | yes  |
| IAG+0.002VAE |   94.02/6.42    |                                | 32  | yes  |
| IAG+0.003VAE |    93.57/6.4    |                                | 32  | yes  |
| IAG+0.004VAE |   94.78/6.23    |                                | 32  | yes  |
| IAG+0.005VAE |   93.58/6.26    |                                | 32  | yes  |
| IAG+0.006VAE |   94.08/5.77    |                                | 32  | yes  |
| IAG+0.007VAE |   94.11/6.11    |                                | 32  | yes  |
| IAG+0.008VAE |    93.51/6.9    |                                | 32  | yes  |
| IAG+0.009VAE |   93.88/6.25    |                                | 32  | yes  |
| IAG+0.01VAE  |   94.28/6.04    | `10 * VAE_loss,20 * regu_loss` | 32  | yes  |
| IAG+0.02VAE  |    93.8/6.21    | `10 * VAE_loss,20 * regu_loss` | 32  | yes  |
| IAG+0.03VAE  |   93.33/6.39    | `10 * VAE_loss,20 * regu_loss` | 32  | yes  |
| IAG+0.04VAE  |   94.65/6.52    | `10 * VAE_loss,20 * regu_loss` | 32  | yes  |
| IAG+0.05VAE  |   93.79/6.81    | `10 * VAE_loss,20 * regu_loss` | 32  | yes  |
| IAG+0.06VAE  |   93.71/6.38    | `10 * VAE_loss,20 * regu_loss` | 32  | yes  |
| IAG+0.07VAE  |    94.11/6.5    | `10 * VAE_loss,20 * regu_loss` | 32  | yes  |
| IAG+0.08VAE  |   93.66/6.33    | `10 * VAE_loss,20 * regu_loss` | 32  | yes  |
| IAG+0.09VAE  |   94.26/6.11    | `10 * VAE_loss,20 * regu_loss` | 32  | yes  |
|  IAG+0.1VAE  |   94.44/6.26    | `10 * VAE_loss,20 * regu_loss` | 32  | yes  |
|  IAG+0.2VAE  |   94.14/6.26    | `10 * VAE_loss,20 * regu_loss` | 32  | yes  |
|  IAG+0.3VAE  |   94.32/5.33    | `10 * VAE_loss,20 * regu_loss` | 32  | yes  |
|  IAG+0.4VAE  |   94.24/5.92    | `10 * VAE_loss,20 * regu_loss` | 32  | yes  |
|  IAG+0.5VAE  | **95.25/5.19**  | `10 * VAE_loss,20 * regu_loss` | 32  | yes  |
|  IAG+0.6VAE  |   95.05/5.48    | `10 * VAE_loss,20 * regu_loss` | 32  | yes  |
|  IAG+0.7VAE  |   94.39/6.34    | `10 * VAE_loss,20 * regu_loss` | 32  | yes  |
|  IAG+0.8VAE  |   94.24/5.61    | `10 * VAE_loss,20 * regu_loss` | 32  | yes  |
|  IAG+0.9VAE  |   95.03/5.93    | `10 * VAE_loss,20 * regu_loss` | 32  | yes  |

### SEED 跨人

|    Model     |    Acc/std     |                      Note                       | seed |
| :----------: | :------------: | :---------------------------------------------: | :--: |
|     IAG      | **86.30/6.91** |                                                 |      |
|      -       |       -        |                        -                        |      |
|   IAG+VAE    |   86.77/7.82   | `1.0 * VAE_loss,20 * regu_loss, batch_size=128` | yes  |
| IAG+0.001VAE |   85.16/7.16   | `1.0 * VAE_loss,20 * regu_loss, batch_size=128` | yes  |
| IAG+0.01VAE  | **87.54/6.92** | `1.0 * VAE_loss,20 * regu_loss, batch_size=128` | yes  |
|  IAG+0.1VAE  |   84.4/8.66    | `1.0 * VAE_loss,20 * regu_loss, batch_size=128` | yes  |
