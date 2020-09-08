# pycat
cat-like utility written in python using rich for colorizing output
## Usage

**Display contents of a single file:**
```
python pcat.py file
```

**Display contents of multiple files:**
```
python pcat.py file1 file2 file3
```

**Copy file[s] contents to a new file:**
```
python pcat.py file[...s] > file
```

**Accept user input as file text:**
```
python pcat.py
```
```
python pcat.py -
```
```
python pcat.py file1 -
```
```
python pcat.py file1 - file2
```
## Bugs
- User input still doesn't work in *file1 - file2 > input_sandwich*
