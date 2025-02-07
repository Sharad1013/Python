# Advanced Python -->> 2

# virtual environment

# VIRTUAL ENVIRIONMENT
# An environment which is same as the system interpreter but is isolated from the other Python environments on the system. 

# INSTALLATION

# To use virtual environments, we write:

# pip install virtualenv # Install the package

# We create a new environment using: 

"""virtualenv myprojectenv""" # Creates a new venv

# The next step after creating the virtual environment is to activate it.
"""activating script for this environment

.\env\Scripts\activate.ps1

"""
# We can now use this virtual environment as a separate Python installation.



# PIP FREEZE COMMAND
# ‘pip freeze’ returns all the package installed in a given python environment along with the versions.
"""pip freeze > requirements .txt"""

# The above command creates a file named ‘requirements.txt’ in the same directory containing the output of ‘pip freeze’.
"""
pip install –r requirements.txt
"""

# The above command will copy all the files or say dependency files present in the environment into a folder as requirements.txt ( Good Practice )

