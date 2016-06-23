# What is this?

I like banner comments in my code. Modern IDE's have fancier ways of doing this like code collapsing and such. And, Python style guides generally prohibit this style of commenting. But, I like to see the big test while scrolling (or, in [`subl`](https://www.sublimetext.com/)). 

# Example

```python
from banner_comment import *
print(banner_comment("hello"))
```

## Outputs...
```
###############################################################################
#                             _          _ _                                  #
#                            | |__   ___| | | ___                             #
#                            | '_ \ / _ \ | |/ _ \                            #
#                            | | | |  __/ | | (_) |                           #
#                            |_| |_|\___|_|_|\___/                            #
#                                                                             #
###############################################################################
```

# Installation

This (one function) package just wraps [figlet](http://www.figlet.org/). You need to install figlet first. It exists on lots of package managers. E.g. 

```sh
brew install figlet    # for OSX
apt-get install figlet # for ubuntu
```

After installing figlet, do
```sh
pip install banner_comment
```
