# 路面損壞分類與資料集整理

## 損壞種類分類

| **類別**       | **損壞種類**                                           |
|----------------|--------------------------------------------------------|
| **裂縫類**     | 縱向裂縫、橫向裂縫、網狀裂縫、塊狀裂縫、邊緣裂縫         |
| **表面損壞類** | 剝落、補丁                                             |
| **凹陷與突出類** | 坑洞、沉陷、隆起                                       |
| **功能性損壞類** | 車轍、磨損                                             |
| **邊緣損壞類** | 邊緣裂縫、邊緣沉陷                                      |

---

## 資料集類型

| **資料集類型** | **資料集名稱**                                           |
|----------------|----------------------------------------------------------|
| **框選資料集** | CNRDD-dataset、Pothole Detection、Pothole.v1-raw.yolov9、RDD2022 |
| **分割資料集** | CrackForest-dataset-master、DeepCrack-master、pavement crack datasets、pothole600 |
| **全圖分類資料集** | RSCD dataset-1million                                    |

---

## 原始資料集整理

### 路徑與狀態說明
- **裂縫類資料集**
  - `0_data\0_rawDataSet\pavement crack datasets\CFDy`  
  - `0_data\0_rawDataSet\CrackForest-dataset-master`  
    - **重複**資料
  - `0_data\0_rawDataSet\pavement crack datasets\CrackAnnotationTool`  
    - **無標註**

---
