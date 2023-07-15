# Brightness Linux

## Descriptions

This application controls the brightness via a user interface.

## How it works

The app gets the number of monitors connected, creates a control for any monitor, and saves a configuration on an external file to retrieve every time that increments or decrements values on brightness.

## How to install

### Install tools and set up the environment:

1. Update pip package: 'sudo apt-get update'.
2. Install Python: 'sudo apt-get install python3'
3. Install an environment's tools: 'python3 -m pip install --user virtualenv'
4. Clone this repository on your system.
5. Enter the folder via cmd:  'cd  /your_sytem_path/brightness-linux/'
6. Into the folder, create a virtual environment: 'python3 -m virtualenv env-name'.
7. Activate a virtual environment: 'source env-name/bin/activate'
8. Install the compiler tool: 'python3 -m pip install cx_Freeze'.

### Compile the app: 

1. Compile the app into the folder and run: 'cxfreeze -c app.py'
2. The compiler will create a folder called 'build' which will be the 'app'.