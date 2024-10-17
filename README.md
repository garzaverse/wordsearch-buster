# wordsearch-buster

wordsearch-buster is a simple command-line interface (CLI) written in Python. This program takes in one required argument, which is a string of alphabetical letters, followed by an optional integer. The integer should be at least 3 and no greater than the length of the provided string.

## Features

- Accepts a string of alphabetical letters as a required argument.
- Accepts an optional integer with constraints.
- Ensures the integer is between 3 and the length of the provided string.

## Requirements

- Python 3.10 or later

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/garzaverse/wordsearch-buster.git
    cd wordsearch-buster
    ```

2. Create and activate a virtual environment (optional but recommended):

    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the necessary packages:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

Run the program using the command line:

```sh
python wordsearch-buster.py <alpha_string> [optional_integer]
```

### Examples

1. **Basic usage with required argument**:

    ```sh
    python wordsearch-buster.py example
    ```

2. **With optional integer argument**:

    ```sh
    python wordsearch-buster.py example 5
    ```

In the second example, the string `example` is the required argument, and `5` is the optional integer argument.

## Constraints

- The required argument must only contain alphabetical letters.
- The optional integer, if provided, must be at least `3` and no greater than the length of the required string.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Contributing

1. Fork the repository.
2. Create your feature branch: `git checkout -b feature/my-new-feature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/my-new-feature`
5. Submit a pull request.

## Contact

For more information or if you encounter any issues, please open a [GitHub issue](https://github.com/garzaverse/wordsearch-buster/issues) or contact [joseg@garzaverse.xyz](mailto:joseg@garzaverse.xyz).