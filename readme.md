# prathvcs

**prathvcs** is a simplified version control system written in Python. It allows you to track changes to files, view commit history, and switch between different versions of your files. This project is intended for educational purposes to demonstrate how a basic VCS might work under the hood.

## Features

- Initialize a new repository
- Add files to track changes
- Commit changes with messages
- View commit history
- Check the status of your repository
- Checkout specific commits
- Get help on how to use prathvcs

## Project Structure

```
prathvcs/
├── prathvcs/
│   ├── __init__.py
│   ├── repository.py    # Main functionality
│   ├── commit.py        # Commit handling
│   ├── status.py        # Status functionality
│   ├── log.py           # Log functionality
│   ├── checkout.py      # Checkout functionality
│   ├── help.py          # Help functionality
│   └── cli.py           # Command-line interface
├── setup.py
└── README.txt
```

## Installation

### Prerequisites

- Python 3.x installed on your system.
- `pip` package manager.

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/prathvcs.git
   ```

2. **Navigate to the Project Directory**

   ```bash
   cd prathvcs
   ```

3. **Install the Package**

   Install `prathvcs` globally using `pip`:

   ```bash
   pip install .
   ```

   **Note**: You may need to use `pip3` instead of `pip` depending on your system configuration.

4. **Verify the Installation**

   Run the following command to see the help message:

   ```bash
   prathvcs help
   ```

   You should see the help information displayed in your terminal.

## Usage

After installing `prathvcs`, you can use it from any directory. Below are the basic commands and examples.

### Initialize a New Repository

```bash
prathvcs init
```

This command initializes a new prathvcs repository in the current directory by creating a `.prathvcs` folder to store metadata.

### Add Files to Be Tracked

```bash
prathvcs add <filename>
```

Example:

```bash
prathvcs add example.txt
```

Adds `example.txt` to the staging area to be tracked.

### Commit Changes with a Message

```bash
prathvcs commit -m "Commit message"
```

Example:

```bash
prathvcs commit -m "Initial commit"
```

Commits the staged changes with the message "Initial commit".

### View Commit History

```bash
prathvcs log
```

Displays the commit history with IDs, timestamps, and messages.

### Check the Repository Status

```bash
prathvcs status
```

Shows the status of the repository, including staged, modified, and untracked files.

### Checkout a Specific Commit

```bash
prathvcs checkout <commit_id>
```

Example:

```bash
prathvcs checkout a1b2c3d4
```

Switches the working directory to the state of the specified commit.

### Get Help Information

```bash
prathvcs help
```

Displays help information for all commands.

## Examples

Below is a step-by-step example to demonstrate how to use `prathvcs`.

### 1. Initialize the Repository

```bash
prathvcs init
```

Output:

```
Initialized empty prathvcs repository in ./.prathvcs
```

### 2. Create and Add a File

Create a new file `hello.txt`:

```bash
echo "Hello, World!" > hello.txt
```

Add the file to the staging area:

```bash
prathvcs add hello.txt
```

Output:

```
Added 'hello.txt' to staging area.
```

### 3. Commit the Changes

```bash
prathvcs commit -m "Add hello.txt"
```

Output:

```
[abcd1234] Add hello.txt
```

### 4. Modify the File

Modify `hello.txt`:

```bash
echo "This is a modification." >> hello.txt
```

Check the status:

```bash
prathvcs status
```

Output:

```
Staged files:
  (no files staged)

Modified files:
  hello.txt

Untracked files:
  (no untracked files)
```

### 5. Add and Commit the Changes

Add the modified file:

```bash
prathvcs add hello.txt
```

Commit the changes:

```bash
prathvcs commit -m "Update hello.txt"
```

### 6. View Commit History

```bash
prathvcs log
```

Output:

```
Commit ID: efgh5678
Timestamp: 2024-11-14 12:00:00
Message: Update hello.txt
----------------------------------------
Commit ID: abcd1234
Timestamp: 2024-11-14 11:55:00
Message: Add hello.txt
----------------------------------------
```

### 7. Checkout an Earlier Commit

```bash
prathvcs checkout abcd1234
```

Now, `hello.txt` will be reverted to its initial state.

### 8. Check Repository Status

```bash
prathvcs status
```

### 9. Get Help

```bash
prathvcs help
```

## Notes and Limitations

- **File Types**: Designed for text-based files. Binary files may not be handled efficiently.
- **No Branching**: This VCS does not support branching or merging.
- **No Remote Repositories**: There is no support for remote repositories.
- **Simplified Functionality**: This is a basic implementation intended for educational purposes.

## Troubleshooting

- **Command Not Found**: If you receive a "command not found" error after installation, ensure that your Python scripts directory is in your system's `PATH` environment variable.
- **Permission Issues**: If you encounter permission errors during installation, try using `pip install . --user` to install the package for your user only.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue to discuss improvements or report bugs.

## License

This project is licensed under the MIT License.

## Contact

For questions or support, please contact:

- **Name**: Your Name
- **Email**: your.email@example.com

## Acknowledgments

- Inspired by the need to understand how version control systems work under the hood.
- Thanks to all contributors and users for their support.

## Final Remarks

Enjoy using `prathvcs`! This project is a great way to get hands-on experience with version control concepts. Feel free to explore the code, modify it, and adapt it to your learning needs.