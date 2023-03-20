# Latex-Tool
Some personal scripts for latex

## Biblatex format checking (to complete the debugging system in Latex compilation) 
- Identify irregularities in the `.bib` file (and need to correct it manually)
- Require two inputs as parameters:
    1. `[File path]` e.g. `C:\Users\xinhe\Dropbox\00_reference.bib`
    2. `Y/n` (`n` by default) to decide whether or not to display all the checked entries.

### Suggested format:
- Reference is composed of the author's last name without accent and the publication's year: e.g. ✅Bazant1987 ❌Bažant1987
- Each line in curly brackets ends with a comma
- No empty line in curly brackets

### Detectable warning/error (after what I commit easily):
- `'NoneType' object is not subscriptable` when a bib reference is named with uncommon caracter
- `Last caracter is not comma`: Latex compilation problems will occur if a line ends without a comma (perhaps with a space, or the comma is ignored)
- `'&' instead of '\&'`: A single "`&`" caracter causes compilation problems
- `Not closed with a '}'`: The curly brackets are not closed correctly