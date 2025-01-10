# 路面損壞分類與資料集整理

## 安裝步驟
### 步驟一：資料集下載
1. 資料集下載 https://thu-rsxd.com/dxhdiefb/
2. 解壓縮
---
### 步驟二：git

1. 下載資料夾並在資料夾開啟終端
https://github.com/ShihYunChung/ModelArena
2. git init
3. 登入(若有需要)
<br>git config --global user.name "Your Name"<br>git config --global user.email "your_email@example.com"
4. git remote add origin https://github.com/ShihYunChung/ModelArena.git
5. git pull origin main
6. git add .
7.  git commit -m "commit"
8. git push -u origin main

---
### 步驟三：安裝環境
所需套件：matplotlib, Pillow, numpy, scipy, opencv-python, torchvision, timm, tqdm, torch, scikit-learn

torch 官網下載自己的版本 https://pytorch.org/
####  conda
``` bash 
conda create -n ModelArena python=3.10 -y

conda activate ModelArena

pip install nvidia-cudnn-cu11

conda install matplotlib pillow numpy scipy opencv torchvision pytorch scikit-learn timm tqdm -c pytorch -c conda-forge
```
---
### 步驟四：資料集處理
1. 執行 " tools.ipynb "中第一個儲存格 建立資料夾
2. 將資料集放在 " 0_data\0_rawDataSet " 下
3. 執行 " tools.ipynb "中剩下之儲存格即可<br>- 自動處理測試集和驗證集<br>- 查看資料夾結構與資料及資訊<br>- 查看各資料集標註方式
---
---
---

## 檔案相關
### 損壞種類分類(自定義)

| **類別**       | **損壞種類**                                           |
|----------------|--------------------------------------------------------|
| **裂縫類**     | 縱向裂縫、橫向裂縫、網狀裂縫、塊狀裂縫、邊緣裂縫         |
| **表面損壞類** | 剝落、補丁                                             |
| **凹陷與突出類** | 坑洞、沉陷、隆起                                       |
| **功能性損壞類** | 車轍、磨損                                             |
| **邊緣損壞類** | 邊緣裂縫、邊緣沉陷                                      |

---

### 資料集類型

| **資料集類型** | **資料集名稱**                                           |
|----------------|----------------------------------------------------------|
| **框選資料集** | CNRDD-dataset、Pothole Detection、Pothole.v1-raw.yolov9、RDD2022 |
| **分割資料集** | CrackForest-dataset-master、DeepCrack-master、pavement crack datasets、pothole600 |
| **全圖分類資料集** | RSCD dataset-1million                                    |

---

### 原始資料集整理

#### 路徑與狀態說明
- **裂縫類資料集**
  - `0_data\0_rawDataSet\pavement crack datasets\CFDy`  
  - `0_data\0_rawDataSet\CrackForest-dataset-master`  
    - **重複**資料
  - `0_data\0_rawDataSet\pavement crack datasets\CrackAnnotationTool`  
    - **無標註**



RSCD dataset-1million分類（27類）：
dry_asphalt_severe, dry_asphalt_slight, dry_asphalt_smooth, dry_concrete_severe, dry_concrete_slight, dry_concrete_smooth, dry_gravel, dry_mud, fresh_snow, ice, melted_snow, water_asphalt_severe, water_asphalt_slight, water_asphalt_smooth, water_concrete_severe, water_concrete_slight, water_concrete_smooth, water_gravel, water_mud, wet_asphalt_severe, wet_asphalt_slight, wet_asphalt_smooth, wet_concrete_severe, wet_concrete_slight, wet_concrete_smooth, wet_gravel, wet_mud


---

# 待辦

1. val
2. early stop
3. 訓練時間
4. log紀錄
5. 圖像化介面
6. 連續訓練
7. 其他模型
8. 儲存準確度
9. 混淆矩陣 模型名稱、參數
10. 介面?
11. 混和精度訓練?
.py




