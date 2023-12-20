# Installation

We recommend installing HBSIR in a virtual environment to avoid conflicts with other Python packages.

## Setting Up a Virtual Environment

1. Create a virtual environment

    ```bash
    python -m venv venv
    ```

2. Activate the virtual environment

    === "Windows"
    
        ```powershell
        venv\Scripts\activate
        ```
    
    === "Linux/macOS"
    
        ```bash
        source venv/bin/activate
        ```

For more information go to the [venv documentation](https://docs.python.org/3/library/venv.html)
or the [Real Python tutorial on virtual environments](https://realpython.com/python-virtual-environments-a-primer/).

## Installing HBSIR 

1. Install the latest stable version from PyPI

    ```
    pip install hbsir
    ```

2. Alternatively, install the development version from GitHub

    ```
    pip install git+https://github.com/Iran-Open-Data/HBSIR.git
    ```
