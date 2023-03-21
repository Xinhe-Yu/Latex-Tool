# Latex-Tool
Some personal scripts for latex

## Biblatex format checking (to complete the debugging system in Latex compilation) 
- Identify irregularities in the `.bib` file (and need to correct it manually)
- Require two inputs as parameters:
    1. `[File path]` e.g. `C:\Users\xinhe\Dropbox\00_reference.bib`
    2. `Y/n` (`n` by default) to decide whether or not to display all the checked entries.

### Suggested format:
- Reference is composed of latin characters, numbers, underline and dash; other symbols or characters with accent is not recommended: e.g. ✅Kunze-Gotte1999 ❌Kunze-Götte1999
- Each line in curly brackets ends with a comma
- No empty line in general curly brackets
- Final right curly brackets take up a full line

### Detectable warning/error (after what I commit easily):
- `Not recommended bib reference name`: there is at least one uncommon caracter in the bib reference
- `Last caracter is not comma`: if a line ends without a comma, it may trigger some Latex compilation problems (perhaps with a space, or the comma is ignored)
- `'&' instead of '\&'`: A single "`&`" character causes compilation problems
- `Not closed with a '}' or has an empty line inside the curly brackets`: The curly brackets are not closed correctly