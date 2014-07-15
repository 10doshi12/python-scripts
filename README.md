This is a collection of short Python scripts I have added to my
`PATH` variable to run from anywhere.
None are currently available in [pip][pip],
but I will add them if enough people are interested.

To add these to your `PATH`, clone the repo and add the following
to your `bashrc` or `zshrc`, replacing `<python-scripts>`
with the location of the cloned repository.
Furthermore, see my [dotfiles][dotfiles] repo for my
complete OSX and Linux system configurations.

```Bash
# Add additional directories to the path.
pathadd() {
  [ -d "$1" ] && [[ ":$PATH:" != *":$1:"* ]] && PATH="${PATH:+"$PATH:"}$1"
}

pathadd <python-scripts>/python2.7
pathadd <python-scripts>/python3
```

# Python 2.7
## music-organizer.py
This script organizes my music collection for iTunes
and [mpv][mpv] using tag information.
The directory structure is `<artist>/<track>`, where `<artist>` and `<track>`
are lower case strings separated by dashes.
See the [blog post][music-organizer-post] for a more detailed overview.

# Python 3
## EvalExpr.py
A module to evaluate a mathematical expression using Python's AST.
Tests are located in `EvalExprTest.py`.
See the [blog post][eval-post] for a more detailed overview.

```
$ EvalExpr.py '(((4+6)*10)<<2)'
(((4+6)*10)<<2) = 400
```

## link-checker.py
Builds upon linkchecker to hide warnings and to send a concise email
if bad links are found.
See the [blog post][link-checker-post] for a more detailed overview.

![Link checker screenshot](https://raw.githubusercontent.com/bamos/python-scripts/master/link-checker-screenshot.png?raw=true)

## ScrapeCountries.py
Scraping HTML tables with HTMLParser.
Tests are located in `ScrapeCountriesTest.py`.
See the [blog post][country-post] for a more detailed overview.

```
$ ScrapeCountries.py 'http://www.nationsonline.org/oneworld/countries_of_the_world.htm' countries.tsv
Parsing countries of the world.
Using 5 columns overall and extracting columns (1, 2, 3, 4).
Finished extracting. Data written to 'countries.tsv'

$ head -n 1 countries.tsv
Afghanistan	Afghanistan	Afghanestan	South-Central Asia
```

## phonetic.py
Obtain the NATO phonetic alphabet representation from short phrases.

```
$ phonetic.py github
g - golf
i - india
t - tango
h - hotel
u - uniform
b - bravo
```

[country-post]: http://bamos.github.io/2013/05/03/scraping-tables-python/
[eval-post]: http://bamos.github.io/2013/08/07/python-expression-evaluator/
[link-checker-post]: http://bamos.github.io/2014/02/06/link-checker-crontab/
[music-organizer-post]: http://bamos.github.io/2014/07/05/music-organizer/
[mpv]: http://mpv.io/
[pip]: http://pip.readthedocs.org/en/latest/
[dotfiles]: https://github.com/bamos/dotfiles
