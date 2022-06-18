# Detecting-Translated-Korean-Texts-Using-GRU


## Sources and how to execute

### 1. `src/Detecting Translated Texts Using GRU.ipynb`

Pre-trained word-embedding load, model, training and evaluation

#### Google Colab
You can directly execute the codes with google colab in following link.
https://colab.research.google.com/drive/1SHLihEsln__gdXxKJQzmk5ZUptOFBS3J?usp=sharing

#### Local
Execute src/Detecting Translated Texts Using GRU.ipynb file

e.g.

`jupyter nbconvert --to python src/Detecting Translated Texts Using GRU.ipynb`\
`python Detecting Translated Texts Using GRU.py`

`pip install papermill`\
`papermill src/Detecting Translated Texts Using GRU.ipynb output.ipynb`

*   Run all blocks to build, train, and evluate the model. It runs with default setting. \ 
*   Default setting is GRU-2 (2 linear layers) without pre-trained vector.\
*   To change the setting, block/unblock the codes as followings.
1. Use of pre-trained embedding layer : Block/unblock the codes in part named "Embedding Mode"
2. GRU-2 / GRU-3 : Block/unblock the codes in part named "GRU-2 / GRU-3"

### 2. `src/parse.py`

Data preprocessing

`python src/parse.py`

## Model

This is GRU-based model for translated(machine-generated) Korean sentence detection.\
GRU-2 consists of 2 linear + dropout layers.\
GRU-3 consists of 3 linear + dropout layers.

![image.png](data:image/png;base64,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)

With Sihwan Kim, Jaewon Wi. Project. CS376 Machine Learning. KAIST 2022 Spring.
