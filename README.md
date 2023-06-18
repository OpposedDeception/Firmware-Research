# Firmware Research

<img src="https://files.softicons.com/download/system-icons/windows-8-metro-icons-by-dakirby309/png/128x128/Applications/Command%20Prompt.png" />

Firmware Research is a command-line application that allows you to search for information on the web using the DuckDuckGo search engine.

## Installation

Clone the repository and install the necessary dependencies 

```
git clone https://github.com/OpposedDeception/Firmware-Research/
cd Firmware-Research
pip install -r requirements.txt
```

## Usage

Usage

1. Use the following commands to search for information:

To display the available options and commands, run:
```
python3 firmware-research.py -h
```

2. To define keywords that will be used for searching, use:
```
python3 firmware-research.py -keywords "keywords"
```
Keywords must be in double quotes.

3. To perform a search on the web, use:
```
python3 firmware-search.py ---search <your stuff>
```

4. To search for a specific firmware, use:
```
python3 firmware-research.py --firmware <your device model name>
```

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

    1. Fork the repository.
    2. Create a new branch for your feature or bug fix.
    3. Implement your changes.
    4. Commit and push your changes to your forked repository.
    5. Submit a pull request detailing your changes.
    
## License

This project is licensed under the MIT License.

Feel free to modify and customize it according to your preferences and the structure of your repository.
