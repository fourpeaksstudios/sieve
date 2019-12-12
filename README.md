# Sieve

[Sieve](https://github.com/paysonwallach/sieve) is an Inkscape extension that removes paths with an area smaller than a given threshold.

## Installation

### Dependencies

Sieve depends on `svgpathtools`, which may be installed via your distribution's package manager (preferred), or via `pip`:

```sh
python3 -m pip install --user svgpathtools
```

### From source

Clone this repo or download the [latest release](https://github.com/paysonwallach/sieve/releases/latest) and move the contents of `src` into the Inkscape extension directory (`$HOME/.config/inkscape/extensions` in Linux installations).

```sh
mv sieve/src/* $HOME/.config/inkscape/extensions/
```

## License

[Sieve](https://github.com/paysonwallach/sieve) is licensed under the [GNU General Public License v3](https://github.com/paysonwallach/sieve/blob/master/LICENSE).
