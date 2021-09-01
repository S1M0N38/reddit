# Reddit
Gender classifier for reddit comments

## Requirements
- python >= 3.9: check with `python3 --version`
- jupyter-notebook >=6.4: check with `jupyter-notebook --version`
Maybe previous versions works but it is not guaranteed.

## Installation
1. Clone this repository:
   ```
   git clone https://github.com/S1M0N38/reddit.git
   ```
2. Move inside the cloned repository
   ```
   cd reddit
   ```
3. Assuming you have [Kaggle API](https://github.com/Kaggle/kaggle-api)
   download the dataset:
   ```
   kaggle competitions download -c datamining2021
   ```
4. Unzip *datamining2021.zip* inside *input/datamining2021*:
   ```
   mkdir input && unzip datamining2021.zip -d input/datamining2021 && rm datamining2021.zip
   ```
5. Create python virtual environment and activate it
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
5. Dependencies are define in *requirements.txt*. Install them with
   ```
   python -m pip install -r requirements.txt
   ```
7. Install venv as jupyter kernel
   ```
   python -m ipykernel install --name 'reddit'
   ```

## Working setup
1. Move inside the repository
   ```
   cd reddit
   ```
2. Start jupyter-notebook with --config flag and check that `reddit` is the kernel.
   ```
   jupyter-notebook --config=config.py
   ```

## Download Kaggle outputs
During the exectution of Kaggle notebook, some output file are generated. These are trained sklearn estimators,
learning curves, csv solutions, ... You can download the last version of output files with:
```
kaggle kernels output s1m0n38/simone-bertolotto-857533 -p working
```