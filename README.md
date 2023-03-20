# Latex-Tool
Some personal scripts for latex

## Biblatex format checking (to complete the debugging system in Latex compilation) 
- Identify all the irregularities in the `.bib` file (and need to correct it manually)
- Require two inputs as parameters:
    1. `[File path]` e.g. `C:\Users\xinhe\Dropbox\00_reference.bib`
    2. `Y/n` (`n` by default) to decide whether or not to display all the checked entries.

### Suggested format:
- Reference is composed of the author's last name without accent and the publication's year: e.g. ✅Bazant1987 ❌Bažant1987
- Each line in curly brackets ends with a comma

### Common prompt error:
- `'NoneType' object is not subscriptable` when a bib reference is named with uncommon caracter
