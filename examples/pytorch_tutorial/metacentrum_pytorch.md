

## Conda

Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html)

```shell
wget http://home.zcu.cz/~mjirik/lisa/install/install_conda.sh && source install_conda.sh
```

Init for your shell
```shell
conda init bash
```

Check if conda is ok
```shell
conda list
```

### Problems on Metacentrum

If `conda` does not work, try to run`~.bashrc` manually:
```shell
source ~/.bashrc
```
or restart the session.


## Create the environment

```shell
conda create -n mytorch python
conda activate mytorch
conda install pytorch torchvision torchaudio pytorch cudatoolkit=11.0 -c pytorch

```

## Get the scripts

## Run locally (skp this on Metacentrum)

```shell
python
```

## Run training with Metacentrum




Check if the task is running

https://metavo.metacentrum.cz/cs/myaccount/myjobs.html