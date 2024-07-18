# arithmetic_nikasha
From Valmiki's tutorial on July 18th, 2024

What I learned:
* Using .toml might be easier than using setup.py
* Call `python -m build` in your root directory
* Hopefully it'll successfully build, and then there will be a hidden dist directory in your project
* there's a wheel version of the distribution (.whl) which forgoes the need to build the package again in the user's environment. I think this is an executable thing where you can't access the source code directly (perchance...at least in terms of C code)
* Upload your package to test.pypi
* * you'd need to create an account first (see Val's google slides)