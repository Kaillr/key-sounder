[![Latest Release](https://img.shields.io/github/v/release/Kaillr/key-sounder)](https://github.com/Kaillr/key-sounder/releases/latest)
[![CodeFactor](https://www.codefactor.io/repository/github/kaillr/key-sounder/badge)](https://www.codefactor.io/repository/github/kaillr/key-sounder)

# Key Sounder

**Key Sounder** is a program that plays sound a sound when specific keys (z and x) are pressed, with adjustable volume controls.

## How to Use
### Running the Executable (`.exe`)
1. Simply run the provided `.exe` file.
2. No Python installation is required for this method.

## Prerequisites for running .py

Make sure you have the following installed:

- **`pyenv`**: A tool for managing multiple Python versions.

### Installing `pyenv`
Follow the instructions on the [pyenv installation page](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation) to install `pyenv`.  
To integrate `pyenv` with your shell, follow the instructions [here](https://github.com/nvm-sh/nvm#deeper-shell-integration).

## Installing Local Python Version

1. Install the Python version specified in the `.python-version` file:
   ```bash
   pyenv install
   ```
2. Set the local Python version:
   ```bash
   pyenv local
   ```

## Initialize Virtual Environment (`venv`)

1. In the project's root directory, create a virtual environment:
   ```bash
   python -m venv .venv
   ```

## Activating the Virtual Environment

Activate the virtual environment by running the appropriate command based on your operating system and shell:
    
<table>
  <thead>
    <tr>
      <th>Platform</th>
      <th>Shell</th>
      <th>Command to activate virtual environment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="4">POSIX</td>
      <td>bash/zsh</td>
      <td><code>$ source .venv/bin/activate</code></td>
    </tr>
    <tr>
      <td>fish</td>
      <td><code>$ source .venv/bin/activate.fish</code></td>
    </tr>
    <tr>
      <td>csh/tcsh</td>
      <td><code>$ source .venv/bin/activate.csh</code></td>
    </tr>
    <tr>
      <td>pwsh</td>
      <td><code>$ .venv/bin/Activate.ps1</code></td>
    </tr>
    <tr>
      <td rowspan="2">Windows</td>
      <td>cmd.exe</td>
      <td><code>C:\&gt; .venv\Scripts\activate.bat</code></td>
    </tr>
    <tr>
      <td>PowerShell</td>
      <td><code>PS C:\&gt; .venv\Scripts\Activate.ps1</code></td>
    </tr>
  </tbody>
</table>

To deactivate the virtual environment, simply run:
```bash
deactivate
```

## Install Local Python Packages

1. Make sure the virtual environment is activated.
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running Key Sounder

1. Ensure the virtual environment is activated.
2. Run the key sounder program:
   ```bash
   python key-sounder.py
   ```

## Additional Resources
- For more details on **`pyenv`**, visit the [pyenv documentation](https://github.com/pyenv/pyenv#readme).
- For more details on **`venv`**, visit the [venv documentation](https://docs.python.org/3/library/venv.html).
