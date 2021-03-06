# Catch

![GitHub repository](https://img.shields.io/badge/haithamaouati-Catch-blue?style=flat-square&logo=github)
![GitHub version](https://img.shields.io/badge/version-1.0-yellow?style=flat-square)

Catch - A simple admin panel finder tool.

## Screenshots

![Screenshot](https://raw.githubusercontent.com/haithamaouati/Catch/main/screenshot.PNG?raw=true "Optional Title")

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Help](#help)
- [Features](#features)
- [Environments](#environments)
- [Disclaimer](#disclaimer)
- [Author](#author)
- [License](#license)

## Installation

1. Update & upgrade packages
    ```
    apt update -yy && apt upgrade -yy
    ```
    
2. Install git package
    ```
    apt install git -yy
    ```
    
3. Install python package
    ```
    apt install python -yy
    ```
    
4. Clone the repository
    ```
    git clone https://github.com/haithamaouati/Catch.git
    ```
5. Change to Catch directory
    ```
    cd Catch
    ```
    
6. Change the access mode
    ```
    chmod +x Catch.py
    ```
    
7. Install requirements
    ```
    pip install -r requirements.txt
    ```
    
## Usage

    python3 Catch.py [-h] [-u <url>] [-w <wordlist>]
    
## Example

    python3 Catch.py -u https://127.0.0.1/ -w wordlist.txt

## Help

    python3 Catch.py [-h]
    
###### Optional Arguments
`-h, --help`
show this help message and exit

`-u, --url`
URL website (e.g. http://127.0.0.1/)

`-w, --wordlist`
Wordlist file (e.g. wordlist.txt)

## Features

   - [x] Find admin panel path
   - [x] Find php shell path
   - [ ] ~~Find deface path~~

## Environments

* Windows
* Linux
* macOS
* Android (Termux)

## Disclaimer

:warning: We are not responsible for any misuse or damage caused by this program. use this tool at your own risk!

## Author

Made with **bugs** by [**Haitham Aouati**](https://twitter.com/haithamaouati)

([Table of Contents](#table-of-contents))

## License

This repository is under [Unlicense License](https://github.com/haithamaouati/Catch/blob/main/LICENSE).
