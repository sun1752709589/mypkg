# 使用cython将python源文件转为c文件进而编译为so文件，一般用于代码加密。

## 使用
1. 在setup.py中指定想要被编译的.py文件。
2. 在version.py中指定包名和版本。
3. 运行：`./build.sh`，会在dist文件夹下生成打包好的.tar.gz文件
4. 清扫：`python clear.py`，删除中间过程生成的.c和.so文件。

