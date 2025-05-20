#!/bin/bash

# This file may have been developed with the help of LLM's like ChatGPT

# This script sets up necessary dependencies and is used together with `pyproject.toml`,
# `Dockerfile`, and `.devcontainer/devcontainer.json` in setting up the environment.

# Install the current project
pip install --editable '.[dev]'

# Install IBL, etc. packages without their dependencies. These packages may have complicated
# dependency trees that may cause conflicts, so we're handling their dependencies ourselves
# (see `pyproject.toml`).

# pip install --no-deps git+https://github.com/int-brain-lab/iblenv.git # the IBL environment is not necessary for this project because we handle dependencies ourselves.
pip install --no-deps git+https://github.com/MouseLand/Kilosort.git@main
pip install --no-deps git+https://github.com/NeuralEnsemble/python-neo.git
pip install --no-deps git+https://github.com/SpikeInterface/probeinterface.git
pip install --no-deps git+https://github.com/SpikeInterface/spikeinterface.git
pip install --no-deps git+https://github.com/SteinmetzLab/slidingRefractory.git
pip install --no-deps git+https://github.com/cortex-lab/phy.git
pip install --no-deps git+https://github.com/cortex-lab/phylib.git
pip install --no-deps git+https://github.com/cortex-lab/psychofit.git
pip install --no-deps git+https://github.com/cwindolf/dartsort.git
pip install --no-deps git+https://github.com/evarol/dredge.git
pip install --no-deps git+https://github.com/int-brain-lab/ONE.git
pip install --no-deps git+https://github.com/int-brain-lab/ibl-neuropixel.git
pip install --no-deps git+https://github.com/int-brain-lab/ibl-sorter.git
pip install --no-deps git+https://github.com/int-brain-lab/ibl-style.git
pip install --no-deps git+https://github.com/int-brain-lab/iblviewer.git
pip install --no-deps git+https://github.com/int-brain-lab/iblatlas.git
pip install --no-deps git+https://github.com/int-brain-lab/iblqt.git
pip install --no-deps git+https://github.com/int-brain-lab/ibllib.git
pip install --no-deps git+https://github.com/int-brain-lab/iblutil.git
pip install --no-deps git+https://github.com/int-brain-lab/mtscomp.git
pip install --no-deps git+https://github.com/int-brain-lab/paper-reproducible-ephys.git
pip install --no-deps git+https://github.com/int-brain-lab/viewephys.git
pip install --no-deps git+https://github.com/jwb-byu/NEDS.git@jwb-byu/setup-for-pip
pip install --no-deps git+https://github.com/jwb-byu/paper-brain-wide-map.git@jwb-byu/refactoring-imbizo
