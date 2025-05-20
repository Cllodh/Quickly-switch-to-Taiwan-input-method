# Can be used directly
https://quickly-favg.onrender.com

# Bopomofo Keyboard Converter

A web application that converts Chinese characters into Bopomofo (Zhuyin) keyboard input positions. It displays both the keyboard keys and Bopomofo symbols, helping users understand how to type Chinese characters using the Bopomofo input method.

## Features

- Real-time Conversion: Instant display of results as you type
- Dual Display: Shows both keyboard keys and Bopomofo symbols
- Network Access: Supports access from other devices on the local network
- Responsive Design: Adapts to various screen sizes
- Clean Interface: Clear labels and result display

## System Requirements

- Python 3.7 or higher
- pip (Python package manager)

## Installation

1. Clone or download this project to your local machine

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the application:
```bash
python app.py
```

2. Access in your browser:
   - Local access: `http://localhost:5000`
   - Network access: `http://[Your_IP_Address]:5000`

3. Type Chinese characters in the input box, and the system will automatically display:
   - Top: Keyboard keys
   - Bottom: Bopomofo symbols

## Example

Input "你好" (hello) will show:
- Keyboard keys: su3 cl3
- Bopomofo: ㄋㄧˇ ㄏㄠˇ

## Interface Description

- Input Box: Located at the top of the page for entering Chinese characters
- Result Display:
  - Keyboard Keys: Shows the key combinations to press
  - Bopomofo Symbols: Shows the corresponding Bopomofo symbols

## Notes

1. Ensure your firewall allows access to port 5000
2. For local network usage, make sure:
   - Your computer and accessing devices are on the same network
   - Firewall is properly configured
   - Router settings are correct (if needed)

## Technical Details

- Backend: Python Flask
- Frontend: HTML, CSS, JavaScript
- Chinese to Bopomofo: pypinyin package
- Bopomofo Mapping: Windows Bopomofo input method reference

## FAQ

1. Can't access the webpage?
   - Check if the Flask application is running
   - Verify the IP address is correct
   - Check firewall settings

2. Incorrect conversion results?
   - Ensure you're inputting Chinese characters
   - Check for special characters

## License

MIT License

## Author

[cllodh](https://github.com/Cllodh)

## Version History

- v1.0.0 (2024-03-xx)
  - Initial release
  - Basic conversion functionality
  - Network access support
- v1.1.0 (2024-03-xx)
  - Optimized interface design
  - Adjusted display order
  - Improved responsive layout 
