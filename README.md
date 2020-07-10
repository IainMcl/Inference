# Data inference 

## Aims
- Be able to infer basic missing data to create a more complete data set.
- Functioning application that can take in data and infer data type and select 
best method for data inference.

## Install
Clone from git using: 
```
git clone https://github.com/IainMcl/Inference.git 
```
Create an environment as described blow then install requirements.

### Work machine
On work machine using conda environment `Infer`. Activate using:
```
activate Infer
```

### Other machine
#### Conda
```
conda create -n <ENV_NAME>
activate <ENV_NAME>
conda install --yes --file requirments.txt
```
If new packages are installed run:
```
conda list -e > requirements.txt
```

### Pip
```
virtualenv <ENV_NAME>
# change to env dir and run activate
# change back to project dir
pip install -r requirments.txt
# Or using venv
python -m venv <ENV_NAME>
```

If new packages are installed run:
```
pip freeze > requirements.txt
```

## Run
Run the file `manage.py` and follow instructions either choosing the gui or 
work within the terminal.
