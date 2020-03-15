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
官网：https://tensorflow.google.cn/js

https://github.com/tensorflow/tfjs
https://github.com/tensorflow/tfjs-models
https://github.com/tensorflow/tfjs-examples
https://github.com/tensorflow/tfjs-wechat

API查询:
https://js.tensorflow.org/api/latest/#input

### 运行这个demo
建立python3虚拟环境
pip install -r requirements.txt
bash start.sh
