# Latex-Tool
Some personal scripts for latex

## Biblatex format checking
- Identify all the irregularities in the `.bib` file (and need to correct it manually)
- Require two inputs as parameters:
    1. `[File path]` (e.g. `C:\Users\xinhe\Dropbox\00_reference.bib`)
    2. `Y/n` (`n` by default) to decide whether or not to display all the checked entries.

### Common prompt error:
- `'NoneType' object is not subscriptable` when a bib reference is named with uncommon caracter
