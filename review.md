### review 1

主要认为问题是 evalution week提出了很多。

* 2D only 和 IMU only 的对比实验，希望给出model size 的结果，不希望模型的复杂性来影响结果。这个问题不太好回答吧，确实模型会更大
* merge two branch，结构上的细节，merging part是否很好进行了 ablation研究。同样也有 desigh和复杂度上的疑惑。
* 3DPW 上的可视化结果，可能无法搞出来完全的投影，因为我没有参数，用其他备选参数也可以，只是和图像 aligh 不上。
* VIP 的问题，主要VIP是基于全序列优化的结果，应用价值非常有限。主流现在的方法都是使用小窗口内的帧来进行较为实时的重建。我们的方法是基于预测的。



1.  **size of model** .The size of the proposed architecture is about 2 times of that of 2D only/ IMU only because two branches are utilized. For the cross attention calculation, we only need to calculate the attention between 5 body parts with 256 as the feature dimension. 
2. **merge two branches design** . Based on the proposed architecture, another fusion module is added at the end to concat the IMU and IMU body part features and predict a single rotation with MLPs.  Note that in our proposed architecture,  both IMU and 2D branch generate the SMPL rotation results. Actually, the model size is slightly larger under the "merge two branches" setting.  The design of the merging module is not fully explored and we will add that to the supplementry materials.
3. 3DPW, some parameters missed.
4. VIP belongs to the whole-sequence optimization category while our proposed method just utilize some frames in a small window to predict the central results. The whole-sequence optimization based methods can generate accurate results but are not appliable in real-time tasks.

bordline reject，问题倒是不太难回答。

### review 2

一些语法的错误问题，不重要。

实验部分增加一些解释。

bordline accept ，所以还行。

### review 3

不太好回答，not novel，

如何扭转他觉得不novel的问题，

"need strong arguments to accept the submission"

很难。但是 smoewhat confident 