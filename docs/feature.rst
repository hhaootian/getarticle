.. _feature:

Feature
============

``getarticle`` can be imported in Python or used as command line.

Command line
------------

.. code-block:: bash 

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

Example:

.. code-block:: bash 

  getarticle -i 10.1126/science.abc7424 -o /Users/haotian/Desktop

Please change the download direction to your own. The download direction is the current direction in terminal by default. To change the default download direction, use -sd option.

Tip: If the DOI contains parentheses, add "" around the DOI.

Example:

.. code-block:: bash 

  getarticle -sd /Users/haotian/Downloads

  # will download to /Users/haotian/Downloads folder
  getarticle -i 10.1126/science.abc7424

getarticle can also download article of the current webpage (only supported for MacOS Safari).

Example:

.. code-block:: bash 

  # current Safari webpage: 
  # https://www.nature.com/articles/s41467-020-16670-2

  # download article of current webpage to default direction
  getarticle

Python module
--------------

0. Initialization

.. code-block:: python

  from getarticle import GetArticle
  ga = GetArticle()

1. Download a single article given DOI or website address.

.. code-block:: python

  ga.input_article("10.1126/science.abc7424")
  ga.download()

Notes:

- Once downloaded, all stored articles will be cleared;
- For download function, direction argument is the current direction by default;
- Downloaded article is named as either "article title.pdf" if successfull or "year-month-day-hour-minute-second.pdf".
