# Reddit

Gender classifier for reddit comments

## Requirements

- python (3.9.6) check with `python3 --version`
- jupyter notebook (6.4.0): check with `jupyter notebook --version`
- jupyter nbconvert (6.0.7): check with `jupyter nbconvert --version`
  
Maybe previous versions works but it is not guaranteed.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/S1M0N38/reddit.git
   ```

2. Move inside the cloned repository

   ```bash
   cd reddit
   ```

3. Assuming you have [Kaggle API](https://github.com/Kaggle/kaggle-api)
   download the dataset:

   ```bash
   kaggle competitions download -c datamining2021
   ```

4. Unzip *datamining2021.zip* inside *input/datamining2021*:

   ```bash
   mkdir input && unzip datamining2021.zip -d input/datamining2021 && rm datamining2021.zip
   ```

5. Create python virtual environment and activate it

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

6. Dependencies are define in *requirements.txt*. Install them with

   ```bash
   python -m pip install -r requirements.txt
   ```

7. Install venv as jupyter kernel

   ```bash
   python -m ipykernel install
   ```

8. (Optional) download the trained model from https://ufile.io/5m99mlwy
   and then unzip the folder into `reddit/working`.

## Working setup

1. Move inside the repository

   ```bash
   cd reddit
   ```

2. Start jupyter-notebook with --config flag and check that the right kernel is active.

   ```bash
   jupyter notebook --no-browser --notebook-dir working
   ```

## Interact with Kaggle kernel

Dowload notebook from kaggle and replace the local version

```bash
kaggle kernels pull -p working -m s1m0n38/simone-bertolotto-857533
```

(At the moment there is an [open issue](https://github.com/Kaggle/kaggle-api/issues/377)
about `kernel-metadata.json` generation. UPDATE: now the bug is fixed and issue is closed.)

Upload local version of the notebook to Kaggle and start the exectuion

```bash
kaggle kernels push -p working
```

During the exectution of Kaggle notebook, some output file are generated. These are trained sklearn estimators,
learning curves, csv solutions, ... You can download the last version of output files with:

```bash
kaggle kernels output s1m0n38/simone-bertolotto-857533 -p working
```
(Bug in Kaggle API, output command does not dowload all the files)

## Testing notebook

Working with jupter notebook is great but sometimes code can become messy. Some cell are move up or down, some are deleted
and the notebook stop working when try to run top to bottom. The following command convert the notebook into python script and then
run it. This ensure that the notebook will be working.

```bash
cd working && \
   jupyter nbconvert \
   --to python --stdout \
   --TagRemovePreprocessor.remove_cell_tags 'cmd' \
   simone-bertolotto-857533.ipynb | \
   PYTHONWARNINGS='ignore' MPLBACKEND='agg' python || cd ..
```

The script execution is fast because does not need to draw the plot on the screen (matplotlib backend is `agg`).
Moreover can be used to run part of the notebook that produce some output that is sometime misrender by browser version of jupyter notebook (e.g. tqdm).
