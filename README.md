# LSP-jedi

This is a helper package that automatically installs and updates the
[Jedi LSP Server](https://github.com/pappasam/jedi-language-server) (jedi-language-server).

To use this package, you must have:

- An executable `python` (on Windows) or `python3` (on Linux/macOS)
- The [LSP](https://packagecontrol.io/packages/LSP) package
- It's recommended to also install the `LSP-json` package which will provide auto-completion and validation for this package's settings.

## Applicable Selectors

This language server operates on views with the `source.python` base scope.

## Installation

The plugin is not yet available in Package Control. Till then, you can use the following command under Linux:-

git clone https://github.com/wxguy/LSP-jedi.git ~/.config/sublime-text/Packages/LSP-jedi

You may need to adopt or change the path according to your OS.

## Installation Location

The server is installed in the `$CACHE/Package Storage/LSP-jedi` directory, where `$CACHE` is the base data path of Sublime Text.
For instance, `$CACHE` is `~/.cache/sublime-text` on a Linux system. If you want to force a re-installation of the server,
you can delete the entire `$CACHE/Package Storage/LSP-jedi` directory or just reinstall the package. The installation is done through a virtual environment, using
pip. Therefore, you must have at least the `python` executable installed, and it must be present in your `$PATH`.

Like any helper package, installation starts when you open a view that is suitable for this language server. In this
case, that means that when you open a view with the `source.python` base scope, installation commences.

## Default Config

Following default configuration is provided as part of the plugin:-

```js
{
  "initializationOptions": {
    "codeAction": {
      "nameExtractVariable": "jls_extract_var",
      "nameExtractFunction": "jls_extract_def"
    },
    "completion": {
      "disableSnippets": false,
      "resolveEagerly": false,
      "ignorePatterns": []
    },
    "diagnostics": {
      "enable": false,
      "didOpen": true,
      "didChange": true,
      "didSave": true
    },
    "hover": {
      "enable": true,
      "disable": {
        "class": { "all": false, "names": [], "fullNames": [] },
        "function": { "all": false, "names": [], "fullNames": [] },
        "instance": { "all": false, "names": [], "fullNames": [] },
        "keyword": { "all": false, "names": [], "fullNames": [] },
        "module": { "all": false, "names": [], "fullNames": [] },
        "param": { "all": false, "names": [], "fullNames": [] },
        "path": { "all": false, "names": [], "fullNames": [] },
        "property": { "all": false, "names": [], "fullNames": [] },
        "statement": { "all": false, "names": [], "fullNames": [] }
      }
    },
    "jediSettings": {
      "autoImportModules": [],
      "caseInsensitiveCompletion": true,
      "debug": false
    },
    "markupKindPreferred": "markdown",
    "workspace": {
      "extraPaths": [],
      "environmentPath": "/path/to/venv/bin/python",
      "symbols": {
        "ignoreFolders": [".nox", ".tox", ".venv", "__pycache__", "venv"],
        "maxSymbols": 20
      }
    }
  }
}
```

How to tweak the configuration is listed at official [jedi-language-server](https://github.com/pappasam/jedi-language-server?tab=readme-ov-file#configuration).

## Additional Package

The jedi-language-serve only provides auto-completion for Python files. If you wish to have additional features such as formatting, linting etc., it is highly recommended to install [LSP-ruff](https://packagecontrol.io/packages/LSP-ruff). 

