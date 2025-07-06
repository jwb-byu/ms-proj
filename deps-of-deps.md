Here is a list of packages and dependencies considered for this project, and their associated dependencies. See workflow in .devcontainer/devcontainer.json for how to install dependencies.

# iblutil

colorlog>=6.0.0
numba
numpy>=1.18
pandas>=0.24.2
pyarrow
tqdm>=4.32.1
packaging

# ONE

ruff
numpy>=1.18
pandas>=1.5.0
tqdm>=4.32.1
requests>=2.22.0
iblutil>=1.14.0
packaging
boto3
pyyaml

# iblatlas

ONE-api
iblutil
pynrrd
numpy
matplotlib
scipy

# mtscomp

numpy

# ibl-neuropixel

iblutil >= 1.7.0
joblib
matplotlib
mtscomp
numpy >= 1.21.6
ONE-api >= 2.11.0
pandas
scipy >= 1.11

# iblqt

qtpy>=2.4.1
pandas>2.0
numpy
pyqtgraph>=0.13.7
ONE-api>=3.0.0

# phylib

numpy
scipy
dask
requests
tqdm
toolz
joblib
mtscomp

# ibl-style

figrid
matplotlib
numpy
seaborn

# ibllib

boto3
click>=7.0.0
colorlog>=4.0.2
flake8>=3.7.8
globus-sdk
graphviz
matplotlib>=3.0.3
numba>=0.56
numpy>=1.18
nptdms
opencv-python-headless
pandas
pyarrow
pynrrd>=0.4.0
pytest
requests>=2.22.0
scikit-learn>=0.22.1
scipy>=1.7.0
scikit-image  # this is a widefield requirement missing as of July 2023, we may remove it once wfield has this figured out
imagecodecs  # used to convert tif snapshots to png when registering mesoscope snapshots (also requires skimage)
sparse
seaborn>=0.9.0
tqdm>=4.32.1

# ibl libraries
iblatlas>=0.5.3
ibl-neuropixel>=1.6.2
iblutil>=1.13.0
iblqt>=0.4.2
mtscomp>=1.0.1
ONE-api>=3.0.0
phylib>=2.6.0
psychofit
slidingRP>=1.1.1  # steinmetz lab refractory period metrics
pyqt5
ibl-style

# iblenv

apptools >=4.5.0
boto3
click
colorcet
colorlog
cython
dataclasses
datajoint
flake8
globus-sdk
graphviz
h5py
ibl-neuropixel
ibllib
iblutil
jupyter
jupyterlab
matplotlib
mtscomp
nbformat
numba
numpy
opencv-python # macOS 10.13 and prior are incompatible with modern versions of opencv
ONE-api
pandas
phylib
pillow
plotly
pyarrow
pyflakes >= 2.4.0
pynrrd
pyopengl
PyQt5
pyqtgraph
pytest
requests
scikits-bootstrap
scikit-learn
scipy >=1.4.1
seaborn
SimpleITK
soundfile
sphinx_gallery
statsmodels
tqdm

# paper-brain-wide-map

ibllib
ipython

# iblviewer

numpy
matplotlib
requests
pandas
pynrrd
trimesh
k3d
vtk>=9.0
ipywebrtc
ibllib
iblutil
vedo>=2022.0.1
ipyvtklink
PyQt5
pyqt-darkthem

# kilosort (mouseland)

numpy>=1.20.0,<2.0.0
scipy
scikit-learn
tqdm
torch>=1.6
numba
faiss-cpu
psutil
matplotli
pyqtgraph>=0.13.0
qtpy
pyqt6
pyqt6.sip
sphinx>=3.0
sphinxcontrib-apidoc
nbsphinx
myst_parser
sphinx_rtd_theme
pando

# ibl-sorter

click
dartsort @ git+https://github.com/cwindolf/dartsort@0.1.1
dredge @ git+https://github.com/evarol/dredge@v0.2.2
hdbscan
h5py
matplotlib
mock
numba
numpy
ibllib >= 2.40.0
ibl-neuropixel >= 1.5.0
ipython
phylib >= 2.5.0
pydantic
pyfftw
pytest
pyqt5
scipy
spikeinterface
tqdm
viewephys
pyyaml

# paper-reproducible-ephys

ONE-api
ibllib
ibl-neuropixel
svgutils
figrid
statsmodels
umap
sobol_seq

# NEDS

numpy==1.26.4
pandas
tqdm
matplotlib
seaborn
scikit-learn
scipy
wandb
ONE-api
iblutil
iblatlas
ibllib
ibl-neuropixel
spikeinterface
--extra-index-url https://download.pytorch.org/whl/cu118
torch==2.2.1
torchvision==0.17.1
ray[default]
einops
torcheval==0.0.7
timm==0.9.16
datasets==2.17.1
transformers==4.38.2
accelerate==0.27.2

# spikeinterface

numpy>=2.0.0;python_version>='3.13'
threadpoolctl>=3.0.0
tqdm
zarr>=2.18,<3
neo>=0.14.1
probeinterface>=0.2.23
packaging
numcodecs<0.16.0", # For supporting zarr <
