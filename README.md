# README

## Installation



## Usage

Requires Python >= 3.6

```
$ ./justify.py --help
usage: ./justify.py [OPTIONS] [FILES]...

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

Justify a file text to a default width of 80 columns without shuffling the padding in each line

```
$ ./justify.py some_file.txt
```

Justify a file text to a default width of 60 columns without shuffling the padding in each line

```
$ ./justify.py -c 60 some_file.txt
```


Justify a file text to a default width of 80 columns with shuffling the padding in each line

```
$ ./justify.py -s some_file.txt
```

Without any arguments, justify.py reads content from the standard input. To indicate the end of file, enter CTRL+D on Linux/Unix and CTRL+Z on Windows, followed by [Enter]

To read a document from a URL, use `curl` or `wget`. Here are a few examples:

Justify the BSD 3-Clause license from a URL (80 columns - default):

```
$ curl https://api.github.com/licenses/bsd-3-clause | jq -r .body | python justify.py
```

Justify the MIT license from a URL (80 columns, shuffling padding):

```
$ curl https://api.github.com/licenses/mit | jq -r .body | python justify.py -c 60 -s
```

Justify the Apache 2.0 license from a URL (70 columns, shuffling padding):

```
$ curl https://api.github.com/licenses/apache-2.0 | jq -r .body | python justify.py -c 70 -s
```
