# TensorFlow 使用 MultiGPU 训练模型

使用多个GPU训练分为两种情况：模型并行和数据并行。模型并行是指模型的不同部分在不同的GPU上运行，数据并行是指在不同的GPU上训练不同的数据。数据并行运算还分为同步和异步，同步是指当所有GPU的一个batch数据处理完成后，平均所有GPU上的梯度去更新参数，而异步是各个GPU完成一个batch数据，就利用自己的梯度去更新参数。












## 参考

- https://www.cnblogs.com/hrlnw/p/7779058.html     
