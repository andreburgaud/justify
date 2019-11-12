# JUSTIFY

* Fully justify ASCII documents.
* Useful to justify open source license documents. See examples in this document.

![Justify in Action](https://user-images.githubusercontent.com/6396088/68637452-4b33ab80-04c4-11ea-9f85-aaa78b85d06a.gif)

## Installation

### Download Script


```
$ curl -L -O  https://github.com/andreburgaud/justify/releases/download/0.5.1/justify
$ chmod +x
$ cp justify <directory_in_path>
$ justify --help
usage: /home/some_user/bin/justify [OPTIONS] [FILES]...

Fully justify text

positional arguments:
  files

optional arguments:
  -h, --help            show this help message and exit
  -c COLUMNS, --columns COLUMNS
                        Number of columns (default: 80)
  -l, --license         Display the license
  -s, --shuffle         Spread whitespace separators randomly on each line
                        (default: true)
  -v, --version         show program's version number and exit
```

### Clone Repo

Another option is to clone the repo and use the included Makefile:

```
$ https://github.com/andreburgaud/justify.git
$ cd justify
$ make release
$ cp justify <directory_in_path>
$ justify --help
...
```

## Usage

Requires Python >= 3.6

```
$ justify --help
usage: justify.py [OPTIONS] [FILES]...

Fully justify text

positional arguments:
  files

optional arguments:
  -h, --help            show this help message and exit
  -c COLUMNS, --columns COLUMNS
                        Number of columns (default: 80)
  -l, --license         Display the license
  -s, --shuffle         Spread whitespace separators randomly on each line
                        (default: true)
  -v, --version         show program's version number and exit
```

### Examples

The examples below assume that you copied the executable script `justify` in a folder of your system PATH. You can also perform the same commands by substiting `justify` with `python justify.py`.

Justify a file text to a default width of 80 columns without shuffling the padding in each line:

```
$ justify some_file.txt
```

Justify a file text to a default width of 60 columns without shuffling the padding in each line:

```
$ justify -c 60 some_file.txt
```

Justify a file text to a default width of 80 columns with shuffling the padding in each line:

```
$ justify -s some_file.txt
```

Without any arguments, justify.py reads content from the standard input. To indicate the end of file, enter CTRL+D on Linux/Unix and CTRL+Z on Windows, followed by [Enter],

To read a document from a URL, use `curl` or `wget`. Here are a few examples:

Justify the BSD 3-Clause license from a URL (80 columns - default):

```
$ curl https://api.github.com/licenses/bsd-3-clause | jq -r .body | justify
```

The usage of [`jq`](https://stedolan.github.io/jq/) is needed to extract the text of the license from the JSON data returned by HTTP request. `jq -r .body` extract the raw text of the body field from the JSON payload returned by the `curl` command.

Justify the MIT license from a URL (80 columns, shuffling padding):

```
$ curl https://api.github.com/licenses/mit | jq -r .body | justify -c 60 -s
```

Justify the Apache 2.0 license from a URL (70 columns, shuffling padding):

```
$ curl https://api.github.com/licenses/apache-2.0 | jq -r .body | justify -c 70 -s
```
