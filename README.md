# Reddit
Gender classifier for reddit comments

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
5. Create python virtual env and activate
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
5. Dependencies are define in *requirements.txt* installed with
   ```
   python -m pip install -r requirements.txt
   ```
