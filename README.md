# Electronic structure calculations with machine learning techniques - Superconductor prediction

This repository contains a final project of the degree on physics. This project aims to serve as an exploration method in binary classification models in order to identify superconducting crystalline materials.

- Author: Olaya Folgueiras González
- University of Oviedo

## Data

Materials data is obtained from Aflowlib database (Aflow - Automatic FLOW for Materials Discovery. https://aflowlib.org/). In the code there is a process to download it, but it can take several hours. Superconductors data is obteined from the proyect that can be found on repo https://github.com/aimat-lab/3DSC. Specifically, the file superconductors_3D/data/final/ICSD/3DSC_ICSD_only_IDs.csv.

## Installation

To set up the environment for the project, please follow these steps:

1. **Ensure Conda is Installed**: First, make sure that you have Conda installed on your system. If not, please install it from [Anaconda's official website](https://www.anaconda.com/products/distribution).

2. **Clone the Project Repository**: Clone the project repository to your local machine. Navigate to the directory where you want to clone the repository and use: `git clone [repository-url]`.

3. **Navigate to the Project Directory**: Change to the project's root directory where the `environment.yml` file is located.

4. **Create the Conda Environment**: Use the provided `environment.yml` file to create an identical environment on your machine. This file includes all the necessary Python versions and libraries required for the project. Run the following command:
`conda env create -f environment.yml` This will create a new Conda environment named loyalty.

5. **Activate the Environment**: Once the environment setup is complete, activate it using: `conda activate superconductor`.

## Running the Code

Before executing the main program, you need to configure the data parameters:

1. **Configure Data Parameters**: Navigate to the `config.py` file located within the project structure. Modify the parameters in this file according to your data specifications or requirements for the project. This step is crucial to ensure that the program runs correctly with your specified configurations.

2. **Navigate to the Source Folder**: After configuring the data parameters, move to the `src` folder which contains the source code.

3. **Execute the Main Program**: Run the `main.py` file using Python: `python main.py`.

This will execute the main script of the project. Make sure you have followed all the previous steps and activated the environment before running the script. Also, make sure that the required data and the appropriate settings are present.