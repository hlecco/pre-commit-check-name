pre-commit-check-name
=====================

Hooks for enforcing naming standards with pre-commit.

See also: https://github.com/pre-commit/pre-commit


### Using pre-commit-check-name with pre-commit

Add this to your `.pre-commit-config.yaml`

```yaml
- repo: https://github.com/hlecco/pre-commit-check-name
  rev: v0.1.0
  hooks:
  - id: check-name-regex
  # - id: ...
```

### Hooks available

#### `check-name-regex`
Check if the name of the files (not their full path) being commited match a regular expression.

  - Use the `-d` or `--dir` parameter to limit checks to specific directories.
  For multiple parameters, use this argument more than once.
  - Set one or more regular expressions with `-r` or `--regex`.
  For multiple regex, use this argument more than once.


**Example:** to require every file on `tests/` directory to start with `test_`:

```yaml
- repo: https://github.com/hlecco/pre-commit-check-name
  rev: v0.1.0
  hooks:
  - id: check-name-regex
    args: ['-r', '^test_', '-d', 'tests']
```
