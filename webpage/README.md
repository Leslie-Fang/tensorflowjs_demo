## 网页版本的应用

### 加载tensorflowjs
```
<script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@1.0.1"> </script>
```
或者
```
<script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@1.0.0/dist/tf.min.js"></script>
```
### 下载模型
这里下载模型可能
```
<script src="https://cdn.jsdelivr.net/npm/@tensorflow-models/mobilenet@1.0.0"> </script>
```
被墙的话, 直接offline去下载模型
首先加载这个html看看超时的URL是什么:https://tfhub.dev/google/imagenet/mobilenet_v1_100_224/classification/1/model.json?tfjs-format=file
直接将https://tfhub.dev 替换成国内镜像 https://hub.tensorflow.google.cn
输入这个URL
```
https://hub.tensorflow.google.cn/google/imagenet/mobilenet_v1_100_224/classification/1/model.json?tfjs-format=file
跳转到了
https://www.gstaticcnapps.cn/tfhub-tfjs-modules/google/imagenet/mobilenet_v1_100_224/classification/1/model.json
```

#### 下载模型的时候跨域请求
```
blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present 
```
https://github.com/tensorflow/tfjs/issues/2338


### 示例代码
* 官网：https://tensorflow.google.cn/js

* https://github.com/tensorflow/tfjs
* https://github.com/tensorflow/tfjs-models
* https://github.com/tensorflow/tfjs-examples
* https://github.com/tensorflow/tfjs-wechat

* API查询: https://js.tensorflow.org/api/latest/#input

### 运行这个demo
```
预训练的TFJS model：
https://github.com/tensorflow/tfjs-models/tree/master/coco-ssd

对应的TF model
https://github.com/tensorflow/models/tree/master/research/object_detection
```
一共检测90类物体
https://github.com/tensorflow/tfjs-models/blob/master/coco-ssd/src/classes.ts

预测结果返回值的物理意义:
```buildoutcfg
[{
  bbox: [x, y, width, height],
  class: "person",
  score: 0.8380282521247864
}, {
  bbox: [x, y, width, height],
  class: "kite",
  score: 0.74644153267145157
}]
```

将model copy到本地，自己写代码(objection_detection_local.html)的时候参考这个:
https://github.com/tensorflow/tfjs-models/blob/master/coco-ssd/src/index.ts

### 数据集
http://cocodataset.org/#home

### Fine-tune
预训练的模型下载:
* https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md#coco-trained-models
使用lite_mobilenet_v2，虽然精度稍低，但是速度快很多

### fine-tune模型转换和转换之后的post-process 提高performance
https://github.com/tensorflow/tfjs-models/tree/master/coco-ssd
