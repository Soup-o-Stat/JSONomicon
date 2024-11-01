# JSONomicon

## What is it?
JSONomicon is a CLI tool for converting configuration files to JSON with syntax error detection

## Flags
**CLI flags are set:**
- The path to the .txt file to be converted

## Example

```
python jsonomicon.py my_epic_file.txt
```

## The syntax of the language to be converted
**Comments**
```
{-
This is a
multiline comment
-}
```

**Dictionaries**
```
([
    name: value,
    name: value,
    name: value
])
```

**Names**
```
[a-zA-Z][_a-zA-Z0-9]*
```

**Values**

- Numbers
- Dictionaries

**Declaring a constant**

```
global name = value
```

**Calculating the constant**

```
#{name}
```
