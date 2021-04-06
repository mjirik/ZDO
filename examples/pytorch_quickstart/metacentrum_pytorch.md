# 



* [PyTorch Quickstart](https://pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html)
* [Metacentrum beginners guide](https://wiki.metacentrum.cz/wiki/Beginners_guide)


## Conda

Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html)

```shell
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
```

Init for your shell
```shell
~/miniconda3/bin/conda init bash
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
## Check cuda with interactive task

```shell
qsub -I -l select=1:ncpus=1:ngpus=2:mem=10gb:cl_konoc=False:cl_gram=False  -l walltime=0:30:00 -q gpu
```
Wait for interactive task and check cuda

```shell
export PATH=/storage/plzen1/home/$LOGNAME/miniconda3/bin:$PATH
source activate mytorch
python -c "import torch;print(torch.cuda.is_available())"
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
