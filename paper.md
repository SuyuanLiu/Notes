VAE

```
\begin{equation}
W_{mean} = FC(X) \\
W_{sigma} = FC(X) \\
W_{VAE} = Relu(W_{mean} + e^{W_{sigma} * \epsilon}) \\
y_{VAE} = GCN(X, W_{VAE})\\

W_{original} = (PX+b)*Q \\
y_{original} = GCN(X, W_original) \\

y_{GCN} = concat(y_{VAE}, y_{original}) \\
\end{equation}
$\epsilon$ is the value that randomly take from the series subject to the specified normal distribution.
$FC(.)$ is fully connected layers.


%% Loss
\begin{equation}
Loss_{VAE} = -0.5 * (1 + W_{sigma} - W_{mean}^{2} - e^W_{sigma})
Loss = Loss_{original} + Loss_{VAE}
\end{equation}
```
