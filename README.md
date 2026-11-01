![Intro: the cannery between shifts, a stopped belt, one open tin half filled, steam leaving the retort](intro-banner.png)


# Python-Print-Strategies

![Banner](banner.png)

![Scene: the hall in cross section, tins riding the belt to the lid press, steam rising, reflections moving on the wet floor](scene.svg)

Basic Python print statement strategies, demonstrated by `print.py`. Run it with:

```
python3 print.py
```

Verified output, in order: the string `Fun secret variable`, `Hello World`, the numbers `50`, `1000`, and `3.142`, then all four on one line separated by spaces, then `HelloWorld` (no separator), then `Hello World` (space separator), then `50` and `Hello World` again as commented examples. The script contains no input, no functions, and no output file; it only prints.

The full run, line by line, as the tally board on the project site walks it:

```
Fun secret variable
Hello World
50
1000
3.142
50 1000 3.142 Hello World
HelloWorld
Hello World
50
Hello World
```

Ten lines, in that order, exit code 0.


![Separator](sep-heavy.svg)

## Strategies shown in the file

Strategies shown in the file:

- Printing a variable, a string, and numbers.
- Printing several values in one call, separated by spaces.
- Printing on the same line with `end=""` and with `end=" "`.
- End-of-line comments explaining a line.
- Standalone comment lines and a multi-line docstring used as a comment block.

> **Tally slip, pinned at the top corner:** the verified output list above is the spine of this repo. The two middle lines are the pair to watch: `HelloWorld` with no separator, then `Hello World` with a space separator, back to back.


![Separator](sep-light.svg)

## Comments at the end of the file

The last part of `print.py` teaches comments themselves. A lone hash comment sits on its own line. Longer notes repeat the hash symbol at the start of each line.

> **Tally slip:** the triple quoted block at the end of the file looks like a comment, but it is a string sitting unused, not a true comment. It only reads as documentation because nothing uses it.

Files: `print.py`, `LICENSE`. Branding (`logo.png`, `banner.png`) was already in the repo from an earlier rollout and is referenced above. No code change was made in this pass because the script runs cleanly and its output matches the description above.

- `intro-banner.png`: the opening scenery for this re-skin, generated with the logo and banner set.
