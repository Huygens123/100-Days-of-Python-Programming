
# Automated Letter Generator

## Overview
This script automates the process of creating personalized letters for multiple recipients. It takes a template letter with a placeholder for names and generates individual personalized letters for each recipient listed in a separate file.

## Features
- Reads a template letter with a `[name]` placeholder
- Processes a list of names from a text file
- Creates personalized letters by replacing the placeholder with each recipient's name
- Saves each letter as a separate file named after the recipient
  
```

## Requirements
- Python 3.x
- Read/write access to the file system

## How to Use
1. Create a template letter in `input/Letters/starting_letter.txt` with `[name]` as a placeholder where you want the recipient's name to appear
2. Add recipient names to `input/Letters/invited_names.txt` (one name per line)
3. Run the script:
   ```
   python letter_generator.py
   ```
4. Find personalized letters in the `Output/ReadyToSend/` directory

## Example

### Template Letter (`starting_letter.txt`):
```
Dear [name],

You are cordially invited to our annual gala dinner.
We would be delighted to have you join us on Saturday, May 15th at 7 PM.

Sincerely,
The Event Team
```

### Names File (`invited_names.txt`):
```
John Smith
Jane Doe
Robert Johnson
```

### Output:
The script will generate three files:
- `Output/ReadyToSend/letter_to_John Smith`
- `Output/ReadyToSend/letter_to_Jane Doe`
- `Output/ReadyToSend/letter_to_Robert Johnson`

Each with personalized content replacing `[name]` with the appropriate recipient name.
