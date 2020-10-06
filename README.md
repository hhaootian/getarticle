# getarticle [![Python](https://img.shields.io/badge/Python-3%2B-blue.svg)](https://www.python.org) [![PyPI](https://img.shields.io/pypi/v/getarticle.svg)](https://pypi.org/project/getarticle/) [![pypi downloads](https://pepy.tech/badge/getarticle)](https://pypi.org/project/getarticle)

## Description 

`getarticle` is a package based on SciHub and Google Scholar that can download articles given DOI, website address or keywords.

## Install

Using `pip` to install:

```
# for latest version (developer)
pip install git+https://github.com/HTian1997/getarticle.git

# for last release (stable)
pip install getarticle
```

## Features & Usage

`getarticle` can be imported in Python or used as command line. 

**To use in command line**:

```
usage: getarticle [-h] [-i INPUT] [-o OUTPUT] [-sd SETDOWNLOAD]

getarticle CLI

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        article DOI or website
  -s SEARCH [SEARCH ...], --search SEARCH [SEARCH ...]
                        search keywords
  -o OUTPUT, --output OUTPUT
                        download direction
  -sd SETDIRECTION, --setdirection SETDIRECTION
                        set default download direction
```

Example:

```
getarticle -i 10.1126/science.abc7424 -o /Users/haotian/Desktop
```

Please change the download direction to your own. The download direction is the current direction in terminal by default. To change the default download direction, use `-sd` option.

Tip: If the DOI contains parentheses, add "" around the DOI. 

Example: 

```
getarticle -sd /Users/haotian/Downloads

# will download to /Users/haotian/Downloads folder
getarticle -i 10.1126/science.abc7424
```

`getarticle` can also download article of the current webpage (only supported for MacOS Safari). 

Example:

```
# current Safari webpage: 
# https://www.nature.com/articles/s41467-020-16670-2

# download article of current webpage to default direction
getarticle
```

**To use in Python**:

0. Initialization

```python3
from getarticle import GetArticle

ga = GetArticle()
```

1. Download a single article given DOI or website address. 

```python3
ga.input_article("10.1126/science.abc7424")
ga.download()
```

Notes: 
- Once downloaded, all stored articles will be cleared;
- For `download` function, `direction` argument is the current direction by default;
- Downloaded article is named as either "article title.pdf" if successfull or "year-month-day-hour-minute-second.pdf".

2. Download multiple articles.

```python3
ga.input_article("https://www.nature.com/articles/s41594-020-0468-7#article-info")
ga.input_article("10.1038/s41893-020-0581-y")
ga.download()
```

Notes: 
- Repeatedly using `article` function can save multiple articles. 
- `getarticle` will not save & download duplicate articles;

3. Download related articles given keywords. Keywords can be article names, research fields or author names.

```python3
ga.search("Deep Dive into Machine Learning Models for Protein Engineering")
ga.search("SARS, Computation", num_of_page=2)
ga.search("Roberta Croce")
ga.download()
```

Notes: 
- `num_of_page` is the number of page in Google Scholar, 1 by default. 

4. Show currently stored articles / delete article by index. 

```python3
ga.cur_articles()

ga.remove_article()
```


## License

MIT
