# S3DSS-PointNeXt

## Welcome to DUT Sewer3D Semantic Segmentation Dataset ! (Note: The dataset will be released soon)
--
### *by Minghao Li and [Xin Feng](http://faculty.dlut.edu.cn/2004011148/zh_CN/zsxx/724752/content/79928.htm)*
--
---
<p align="center">
<img src="docs/projects/Logo/2-2.jpg" width=85% height=85% class="center">
</p>
---

Additional tool addresses | [[S3DSS Dataset Download Address]](url) | [[OpenPoints Library]](https://github.com/guochengqian/openpoints) | [[PointNeXt Online Documentation]](https://guochengqian.github.io/PointNeXt/)

**This code project is a tutorial using the S3DSS dataset with PointNeXt as an example**

---

## Motivation and Background
Urban sewer pipelines, as the critical guarantors of urban resilience and sustainable development, undertake the task of sewage disposal and flood prevention. However, in many countries, most municipal sewer systems have been in service for *60* to *100* years, with the *worst* condition rating (*D+*) evaluated by ASCE.
As laser scanning is fast becoming the state-of-the-art inspection technique for underground sewers, semantic segmentation of pipeline point clouds is an essential intermediate step for pipeline condition assessment and digital twinning. Currently, similar to other building structures, the scarcity of real-world point clouds has hindered the application of deep learning techniques for automated sewer pipeline semantic segmentation.

---

## Goal
We provided a high-quality, realistic, semantically-rich public dataset named "*Sewer3D Semantic Segmentation*" (*S3DSS*), including *2500* synthetic scans and *500* real-world scans, for point cloud semantic segmentation in the sewer pipeline domain, for which there are no public datasets in the past. S3DSS contains *230 million points* with *8* categories of common sewer defects. We hope it can be a starting point for benchmarking developed approaches to promote deep learning research on the point cloud of sewer pipeline defects.

<p align="center">
<img src="docs/projects/Logo/3.jpg" width=85% height=85% class="center">
</p>

---

## Content and Annotations
The two sub-datasets were obtained in the following way. The real point cloud data were captured in laboratory scenarios using a **FARO Focus S laser scanner**. We used two prototype **reinforced concrete sewer pipes** to create most of the defect scenes. However, for misalign and displace defects that are difficult to operate with concrete pipes, we used two **steel pipes** which were well-designed to simulate. A total of 500 real scans were collected.

The synthetic point cloud data were obtained by our automated synthetic data generator in Unity3D. [The introduction to the synthetic point cloud data generation methodology can be found in our paper.](url) We generated 2500 scans of sewer defect scenes. In S3DSS, 8 common defect classes are used which includes:

-  Normal
-  Spalling
-  Blockage
-  Corrosion
-  Misalign
-  Deposit
-  Displace
-  Rubber Ring

<p align="center">
<img src="docs/projects/Logo/屏幕截图 2023-07-27 224139.png" width=50% height=50% class="center">
<img src="docs/projects/Logo/屏幕截图 2023-07-27 224712.png" width=50% height=50% class="center">
<img src="docs/projects/Logo/屏幕截图 2023-07-27 232409.png" width=50% height=50% class="center">
<img src="docs/projects/Logo/屏幕截图 2023-07-28 091100.png" width=50% height=50% class="center">
<img src="docs/projects/Logo/屏幕截图 2023-07-28 095310.png" width=50% height=50% class="center">
<img src="docs/projects/Logo/屏幕截图 2023-07-28 095607.png" width=50% height=50% class="center">
</p>

For more details you can go to [our website](url).

---

## PointNeXt Installation
First you need to download and add the toolkit [OpenPoints Library](https://github.com/guochengqian/openpoints)

A simple bash file to install the environment:

```
git clone --recurse-submodules git@github.com:guochengqian/PointNeXt.git
cd PointNeXt
source update.sh
source install.sh
```
Cuda-11.3 is required. Modify the `install.sh` if a different cuda version is used. See [Install](docs/index.md) for detail. 



## Usage 
Check PointNeXt [online documentation](https://guochengqian.github.io/PointNeXt/) for detailed instructions. 

A short instruction: all experiments follow the simple rule to train and test: 

```
CUDA_VISIBLE_DEVICES=$GPUs python examples/$task_folder/main.py --cfg $cfg $kwargs
```
- $GPUs is the list of GPUs to use, for most experiments (ScanObjectNN, ModelNet40, S3DIS), we only use 1 A100 (GPUs=0)
- $task_folder is the folder name of the experiment. For example, for s3dis segmentation, $task_folder=s3dis
- $cfg is the path to cfg, for example, s3dis segmentation, $cfg=cfgs/s3dis/pointnext-s.yaml
- $kwargs are the other keyword arguments to use. For example, testing in S3DIS area 5, $kwargs should be `mode=test, --pretrained_path $pretrained_path`. 

## Read S3DSS Dataset

First you need to overwrite the s3dis.py file in openpoints/dataset/s3dis with the s3dis.py file in S3DSS-PointNeXt.
Provide an example of reading S3DSS dataset:

```
raw_root = os.path.join(data_root, 'sewer3d_semantic_segmentation')
self.raw_root = raw_root
train_str = 'training-pointcloud-synthetic0/real300'
test_str = 'testing-real200'

shape_ids = {}
shape_ids['train_synthetic'] = []
# shape_ids['train_synthetic'] = [line.rstrip() for line in open(os.path.join(self.raw_root, 'training_pointcloud_synthetic_800.txt'))]
# shape_ids['train_real'] = []
shape_ids['train_real'] = [line.rstrip() for line in open(os.path.join(self.raw_root, 'training_pointcloud_real_200.txt'))]
shape_ids['test_real'] = [line.rstrip() for line in open(os.path.join(self.raw_root, 'testing_pointcloud_real_200.txt'))]


if split == 'train':
    self.data_list = shape_ids['train_synthetic'] + shape_ids['train_real']
else:
    self.data_list = shape_ids['test_real']

processed_root = os.path.join(data_root, 'processed')
filename = os.path.join(processed_root, f's3dis_{split}_{test_str}_{voxel_size:.3f}.pkl')
```

Note that the dataset read path needs to be changed to your own path：
```
parser.add_argument('--cfg', type=str, default='/home/liminghao/PointNeXt/cfgs/s3dis/pointnext-b.yaml', required=False, help='config file')
```
/cfgs/s3dis/default.yaml:
```
dataset:
  common:
    NAME: S3DIS
    data_root: /home/liminghao/Pointnet_Pointnet2_pytorch/data
    test_area: 'testing-real200'
    voxel_size: 0.04
```

---

## Acknowledgements
This work was supported by the National Key R & D Program of China (Grant No. 2022YFC3801000) and the National Natural Science Foundation of China (Grant No. 52079024). We also thank Qian et al. for sharing their great work PointNeXt.

## Citation
- Please cite this paper if you find this dataset useful: Data augmentation strategy for point cloud semantic segmentation of drainage pipeline defects: Generating synthetic data and fine-tunning pre-trained deep learning model.
- Previous Publications: [M. Li, X. Feng, Q. Hu, 3D laser point cloud-based geometric digital twin for condition assessment of large diameter pipelines. Tunnelling and Underground Space Technology 142 (2023) 105430](https://www.sciencedirect.com/science/article/pii/S0886779823004509).

<p align="center">
<img src="docs/projects/Logo/13.jpg" width=85% height=85% class="center">
</p>
<p align="center">
<img src="docs/projects/Logo/Logo.jpg" width=30% height=30% class="center">
</p>

Contact us: our WeChat
<p align="center">
<img src="docs/projects/Logo/qrcode_for_gh_e65b93a6a03f_258.jpg" width=30% height=30% class="center">
</p>
