# 📦 Installation

`HBSIR` is a Python library published on PyPI, which means it can be installed
in several ways and used in different workflows.

In this tutorial, we’ll focus on using `uv` — a fast, all-in-one tool for
managing Python environments and packages.

`uv` makes it simple to install and organize Python projects without worrying
about system settings or dependencies.

## 🧰 Installing `uv`

`uv` can be installed with a single command:

=== "Windows"

    ```powershell
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```

=== "Linux and macOS"

    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

After installation, you can verify that it works by running:

    ```bash
    uv --version
    ```

For more details, troubleshooting tips, or advanced options, visit the official
[`uv` installation guide](https://docs.astral.sh/uv/getting-started/installation/).

## 🪄 Setting Up Your Project Directory

Follow these steps to create your working folder and install `HBSIR` using `uv`.

1. Create a new directory for your project and move into it:

    ```bash
    mkdir my-new-project
    cd my-new-project
    ```

1. Initialize a Python environment inside this folder:

    ```bash
    uv init
    ```

    This command creates a lightweight virtual environment so that your project has its own isolated Python setup.

1. Add `HBSIR` to your environment:

    ```bash
    uv add hbsir
    ```

    After this step, HBSIR is ready to use in Python scripts.

### 🧮 Optional: Add Notebook Support

If you prefer using interactive notebooks (similar to Stata’s data browser or do-file interface), you can install one of these variants:

=== "Jupyter Lab"

    ```bash
    uv add hbsir[notebook], jupyterlab
    ```

    Start Jupyter with:Start Jupyter with:

    ```bash
    uv run jupyter notebook
    ```

=== VS Code Notebook

    ```bash
    uv add hbsir[notebook]
    ```

    Then simply create a new file with the .ipynb extension inside your project folder.
    When you open it in Visual Studio Code, the Python and Jupyter extensions will detect it automatically.

=== "Marimo"

    ```bash
    uv add hbsir, marimo
    ```

    Start Marimo with:

    ```bash
    uv run marimo edit
    ```
