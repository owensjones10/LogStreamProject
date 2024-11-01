
# LogStreamProject

## Project Description

**LogStreamProject** is a C++ log file reader and analyzer designed to read, process, and display log entries line-by-line from a specified log file. The project serves as a foundational tool for working with large text-based log files and provides a basis for further development in log data processing and analysis. This project will eventually evolve to support advanced features, including data parsing, multi-threaded processing, and custom summaries, making it a versatile tool for managing and analyzing log data efficiently.

## Features

- Reads log files line-by-line and outputs each line to the console for easy viewing.
- Supports customizable file paths to allow processing of different log files.
- Prepares the foundation for more advanced log analysis, including parsing entries, multi-threading, and data summarization.

## Project Structure

```
LogStreamProject/
├── main.cpp               # C++ code for reading and displaying log entries
├── generate_logs.py       # Python script to generate sample log data
├── logs/                  # Folder containing generated log files
│   └── sample_log.txt     # Example log file (generated)
└── .gitignore             # Specifies files and folders for Git to ignore
```

## Getting Started

### Prerequisites

- **C++ Compiler**: Ensure you have a C++ compiler installed (e.g., `g++` for GCC).
- **Python 3**: Needed to run the `generate_logs.py` script.

### Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/owensjones10/LogStreamProject.git
   cd LogStreamProject
   ```

2. **Generate Sample Log Data** (optional):
   - Use the Python script to create a sample log file in the `logs` directory.
   ```bash
   python3 generate_logs.py
   ```

3. **Compile and Run the C++ Program**:
   ```bash
   g++ main.cpp -o log_reader
   ./log_reader
   ```

## Usage

- **File Reading**: The program reads each line from the log file (`logs/sample_log.txt`) and prints it to the console.
- **Customization**: You can modify the file path in `main.cpp` to read from different log files as needed.

## Future Features

- Parsing log entries to extract timestamps, user IDs, and error codes.
- Multi-threaded processing for handling large log files more efficiently.
- Summarizing data for quick insights (e.g., count of errors, active users).
- Saving analyzed data to output files for further analysis or reporting.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for any improvements or feature suggestions.

## License

This project is licensed under the MIT License.
