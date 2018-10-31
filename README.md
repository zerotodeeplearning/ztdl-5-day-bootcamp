# [Zero To Deep Learning 5 day bootcamp](https://bootcamp.zerotodeeplearning.com)
This repo is a large sample of the coursework in the Zero to Deep Learning Bootcamp. The Bootcamp is a hands-on and immersive course to learn Machine Learning & Deep Learning fast with Python, Pandas, Matplotlib, Scikit-Learn, Keras and Tensorflow.

Participants come to accelerate and consolidate their ML and DL practical skills, as online/remote courses can only take practical skills so far. The Bootcamp provides dedicated time to learn with a teacher to achieve the next level of proficiency. This repo will help you with self-directed learning and show you what we cover in the Bootcamp, with the value of the Bootcamp coming from actually doing the labs in a supported environment.

# Next Bootcamp: 19-23 November, London. [Register here](https://bootcamp.zerotodeeplearning.com). 10% discount with code GITHUB ends November 5

## Quick start guide

#### Download and install Anaconda Python 3

Download here: https://www.anaconda.com/download and then install it on your system.

#### Open a terminal

#### Clone this repository on your local computer
```
git clone https://github.com/zerotodeepearning/ztdl-5-day-bootcamp.git
```

#### Change to course folder
```
cd ztdl-5-day-bootcamp
```

#### Create Conda environment

We provide an [environment configuration file](environment.yml) with all the required dependencies.

```
conda env create
```

wait for the environment to create, this may take a few minutes. Note that this environment is based on Python 3.6 because Tensorflow does not support Python 3.7 yet.

#### Activate the environment (Mac/Linux)
```
conda activate ztdlbootcamp
```

#### Activate the environment (Windows)
```
activate ztdlbootcamp
```

Check that your prompt changed to

```
(ztdlbootcamp) $
```

Now you can run jupyter notebook from within the environment.

#### Launch Jupyter Notebook
```
jupyter notebook
```
and access it from your browser at: http://localhost:8888

You are good to go! Enjoy!


### Troubleshooting

#### Downloading Sports images
Some labs require the sports images dataset, that should be located in `./data/sports/`. The images can be downloaded using the `download_sport.py` script.
```
cd data/sports
python download_sport.py
```
Run this script a couple of times if you get any errors from aws.


#### Updating Conda

If you have installed Anaconda a long time ago, you may want to update it by running:
```
conda update conda
```
and then:
```
conda update anaconda
```

#### Deactivating the environment (Mac/Linux)
```
conda deactivate
```

#### Deactivating the environment (Windows)
```
deactivate
```

#### Deleting the environment
If you decide to completely delete the environment from your system you should use the following command:
```
conda remove -y -n ztdlbootcamp --all
```
