# Analytical Small-Signal Frequency Stability analysis 

This repository provides supporting Python scripts and a Simulink model for the paper Analytical small-signal stability analysis of low-inertia power system frequency response considering secondary frequency regulation.

Paper: Y. Deng, X. Fang, S. Dong, N. Gao, and J. Tan, “Analytical small-signal stability analysis of low-inertia power system frequency response considering secondary frequency regulation,” *Electric Power Systems Research*, vol. 258, article 113025, 2026. DOI: [10.1016/j.epsr.2026.113025](https://doi.org/10.1016/j.epsr.2026.113025).


## Overview

The study develops analytical methods for assessing small-signal frequency stability in low-inertia power systems. Its main works are mathematical derivations. The model equations, analytical derivations, and parameter settings are all presented in the paper. Most of the calculations were performed manually. The Python files calculate individual parameter stability regions. The Simulink model provides a representation of the system frequency response model.

## Repository contents

| File | Description |
| --- | --- |
| `Dibr_region.py` | Calculates the stability interval for IBR damping. |
| `Mibr_region.py` | Calculates the stability interval for IBR inertia. |
| `Betaibr_region.py` | Calculates the stability interval for the IBR regulation factor. |
| `Ribr_region.py` | Calculates the stability interval for the reciprocal of IBR droop, `1/Ribr`. |
| `Simulink.slx` | System frequency response model for time-domain simulation. |
| `requirements.txt` | Python dependency list. |



## Requirements and usage

| Component | Version | Purpose |
| --- | --- | --- |
| Python | 3.9.21 | Runs the four Python scripts. |
| NumPy | 1.26.4 | Matrix operations and eigenvalue calculations. |
| MATLAB and Simulink | R2024b | Opens and runs `Simulink.slx`. |

Python and MATLAB/Simulink must be installed separately.


### Python

From the repository folder, install the pinned dependency:

```bash
python -m pip install -r requirements.txt
```

Run the scripts individually:

```bash
python Dibr_region.py
python Mibr_region.py
python Betaibr_region.py
python Ribr_region.py
```

### MATLAB/Simulink

Use MATLAB R2024b with Simulink installed. Open `Simulink.slx`, run the simulation, and inspect the frequency-response signal in the Scope block. The saved configuration uses a 0.1 p.u. step disturbance at time zero. Model parameters can be adjusted directly in the blocks.

