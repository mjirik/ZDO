# 

* [PyTorch Quickstart](https://pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html)
* [Metacentrum beginners guide](https://wiki.metacentrum.cz/wiki/Beginners_guide)


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

* [Python script with training](https://github.com/mjirik/ZDO/blob/master/examples/pytorch_quickstart/pyt_tutorial_quickstart.py)
* [Shell script for qsub](https://github.com/mjirik/ZDO/blob/master/examples/pytorch_quickstart/qsub_pyt_tutorial_quickstart.sh)

```shell
mkdir ~/pytorch_quickstart
cd ~/pytorch_quickstart
wget https://raw.githubusercontent.com/mjirik/ZDO/master/examples/pytorch_quickstart/pyt_tutorial_quickstart.py
wget https://raw.githubusercontent.com/mjirik/ZDO/master/examples/pytorch_quickstart/qsub_pyt_tutorial_quickstart.sh
```


## Add training  and testing into Metacentrum queue
```shell
qsub qsub_pyt_tutorial_quickstart.sh
```

## Check if the task is running

https://metavo.metacentrum.cz/cs/myaccount/myjobs.html


## See the output

```shell
cat results.txt
```


## Do not run the training on Metacentrum frontend

But you can try it on your computer
```shell
python pyt_tutorial_quickstart.py
```
