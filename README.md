# BSM Parameter Space Scanner

## Overview
A sophisticated parameter space scanning tool for Beyond Standard Model (BSM) physics, focusing on supersymmetric models with inverse seesaw mechanisms. This tool integrates with major physics software packages to perform comprehensive parameter space exploration while checking various experimental and theoretical constraints.

## Features
- Automated parameter space scanning with adaptive sampling
- Integration with physics tools:
  - SPheno for spectrum calculation
  - MicrOMEGAs for dark matter properties
- Built-in constraint checking:
  - Relic density constraints
  - Dark matter direct detection limits
  - LHC constraints
  - Flavor physics observables
- Data management and analysis capabilities
- Automatic generation of SLHA format files
- Parallel processing support

## Requirements
- Python 3.x
- NumPy
- Pandas
- SPheno
- MicrOMEGAs
- pyslha
- xslha

## Installation
1. Clone the repository
2. Install required Python packages:
```bash
pip install numpy pandas
