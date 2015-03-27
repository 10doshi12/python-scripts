#!/usr/bin/env python3

__author__ = ['Brandon Amos <http://github.com/bamos>']
__date__ = '2015.03.27'

"""
Generates the README for
[bamos/python-scripts](https://github.com/bamos/python-scripts).
Script descriptions are obtained by parsing the docstrings.
"""

import ast
import glob
import os
from jinja2 import Template
from subprocess import Popen,PIPE

readme = Template("""
This is a collection of short Python scripts I have added to my
`PATH` variable to run from anywhere.
None are currently available in [pip][pip],
but I will add them if enough people are interested.

To add these to your `PATH`, clone the repo and add the following
to your `bashrc` or `zshrc`, replacing `<python-scripts>`
with the location of the cloned repository.
Furthermore, see my [dotfiles][dotfiles] repo for my
complete Mac and Linux system configurations.

```Bash
# Add additional directories to the path.
pathadd() {
  [ -d "$1" ] && [[ ":$PATH:" != *":$1:"* ]] && PATH="${PATH:+"$PATH:"}$1"
}

pathadd <python-scripts>/python2.7
pathadd <python-scripts>/python3
```

[pip]: http://pip.readthedocs.org/en/latest/
[dotfiles]: https://github.com/bamos/dotfiles

# Scripts
{{descriptions}}

# Similar Projects
There are many potpourri Python script repositories on GitHub.
The following list shows a short sampling of projects,
and I'm happy to merge pull requests of other projects.

{{similar_projects}}
""")

def get_docstr(filename):
    print("  + get_docstr({})".format(filename))
    with open(filename) as f:
        script = ast.parse(f.read())
        try:
            authors,date,desc = map(lambda x: ast.literal_eval(x.value),
                                    script.body[0:3])
        except:
            print("    + Error reading (author,date,desc).")
            raise
        return """
## [{}](https://github.com/bamos/python-scripts/blob/master/{})
+ Authors: {}
+ Created: {}

{}
""".format(filename, filename, ", ".join(authors), date, desc)

def get_descriptions():
    print("# Getting project descriptions")
    return ("\n".join(map(get_docstr,
                          ['generate-readme.py']+glob.glob("python*/*.py"))))

def get_similar_projects():
    print("# Getting similar projects")
    projs =['gpambrozio/PythonScripts',
            'ClarkGoble/Scripts',
            'gpambrozio/PythonScripts',
            'realpython/python-scripts',
            'averagesecurityguy/Python-Examples',
            'computermacgyver/twitter-python']
    cmd = ['./python3/github-repo-summary.py'] + projs
    p = Popen(cmd, stdout=PIPE)
    out,err = p.communicate()
    return out.decode()

if __name__=='__main__':
    # cd into the script directory.
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    with open("README.md","w") as f:
        f.write(readme.render(
            descriptions=get_descriptions(),
            similar_projects=get_similar_projects()
        ))
