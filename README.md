# 🔐 Booking.com Credentials Extractor - Easy & Fast!

A quick and efficient Python script to extract **Booking.com credentials** (6-digit IDs and corresponding passwords) from text files.

## 🚀 Features

- Quickly scans your input text file.
- Automatically finds Booking.com account URLs.
- Extracts 6-digit IDs along with their passwords.
- Stores extracted data neatly into an output file.

## 🛠️ Requirements

- Python 3.x

## ⚡ Quick Start

1. Place your source text file (`booking.txt`) in the script directory.

   Example file content (`booking.txt`):

   ```
   https://account.booking.com/sign-in:123456:yourpassword
   https://account.booking.com/sign-in/password|654321|anotherpassword
   ```

2. Run the script:

   ```bash
   python your_script_name.py
   ```

3. Check results in `identifiants_mdp.txt`.

## 📂 File Format

- **Input** (`booking.txt`):

  ```
  https://account.booking.com/sign-in:123456:yourpassword
  https://account.booking.com/sign-in/password|654321|anotherpassword
  ```

- **Output** (`identifiants_mdp.txt`):

  ```
  123456:yourpassword
  654321:anotherpassword
  ```

## 📚 Python Libraries Used

- [re](https://docs.python.org/3/library/re.html) (Python built-in regex library)

## ⚠️ Important Notes

- Update file names (`fichier_source` and `fichier_resultat`) in the script to match your actual file names.
- Ensure your input file (`booking.txt`) follows the format shown above.

## 👤 Author

- **Vissiouz**

