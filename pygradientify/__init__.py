"""
pygradientify - make terminal ui's beautiful.
Made by Sorrow - want an update or more colors? don't be afraid to make a pull request
License: MIT
"""

from typing import Tuple, Literal, List
import warnings


class _Engine:
    COLORS = {
        'purple_to_white': ((127, 0, 255), (255, 255, 255)),
        'red_to_blue': ((255, 0, 0), (0, 0, 255)),
        'red_to_white': ((255, 0, 0), (255, 255, 255)),
        'green_to_yellow': ((0, 255, 0), (255, 255, 0)),
        'black_to_white': ((0, 0, 0), (255, 255, 255)),
        'blue_to_cyan': ((0, 0, 255), (0, 255, 255)),
        'orange_to_pink': ((255, 165, 0), (255, 192, 203)),
        'mint': ((194, 255, 182), (255, 255, 255)),
        'red_to_yellow': ((255, 0, 0), (255, 255, 0)),
        'blue_to_green': ((0, 0, 255), (0, 255, 0)),
        'purple_to_blue': ((128, 0, 128), (0, 0, 255)),
        'pink_to_white': ((255, 192, 203), (255, 255, 255)),
        'cyan_to_magenta': ((0, 255, 255), (255, 0, 255)),
        'gray_to_black': ((169, 169, 169), (0, 0, 0)),
        'blue_to_white': ((0, 0, 255), (255, 255, 255)),
        'red_to_green': ((255, 0, 0), (0, 255, 0)),
        'green_to_blue': ((0, 255, 0), (0, 0, 255)),
        'blue_to_yellow': ((0, 0, 255), (255, 255, 0)),
        'yellow_to_cyan': ((255, 255, 0), (0, 255, 255)),
        'magenta_to_red': ((255, 0, 255), (255, 0, 0)),
        'white_to_black': ((255, 255, 255), (0, 0, 0)),
        'mystic': ((207, 188, 254), (182, 48, 220)),
        'ash': ((255, 0, 0), (128, 128, 128)),
        'rainbow': ((255, 0, 0), (148, 0, 211)),
    }

    @staticmethod
    def _lerp(t: float, a: Tuple[int, int, int], b: Tuple[int, int, int]) -> Tuple[int, int, int]:
        return tuple(int(a[i] + t * (b[i] - a[i])) for i in range(3))

    @staticmethod
    def _rainbow(t: float) -> Tuple[int, int, int]:
        stops = [
            (255, 0, 0),
            (255, 127, 0),
            (255, 255, 0),
            (0, 255, 0),
            (0, 255, 255),
            (0, 0, 255),
            (148, 0, 211),
        ]

        idx = t * (len(stops) - 1)
        i = min(int(idx), len(stops) - 2)
        local_t = idx - i

        return _Engine._lerp(local_t, stops[i], stops[i + 1])

    @staticmethod
    def _color(name: str, t: float) -> Tuple[int, int, int]:
        if name == 'rainbow':
            return _Engine._rainbow(t)

        start = _Engine.COLORS[name][0]
        end = _Engine.COLORS[name][1]
        return _Engine._lerp(t, start, end)

    @staticmethod
    def _fmt(color: Tuple[int, int, int], char: str) -> str:
        return f'\033[38;2;{color[0]};{color[1]};{color[2]}m{char}\033[0m'

    @staticmethod
    def h(text: str, name: str) -> str:
        lines = text.split('\n')
        out = []

        for line in lines:
            if not line:
                out.append('')
                continue

            n = len(line)
            chars = []

            for i, c in enumerate(line):
                t = i / (n - 1) if n > 1 else 0
                color = _Engine._color(name, t)
                chars.append(_Engine._fmt(color, c))

            out.append(''.join(chars))

        return '\n'.join(out)

    @staticmethod
    def v(text: str, name: str) -> str:
        lines = text.split('\n')
        n = len(lines)
        out = []

        for i, line in enumerate(lines):
            if not line:
                out.append('')
                continue

            t = i / (n - 1) if n > 1 else 0
            color = _Engine._color(name, t)

            chars = [_Engine._fmt(color, c) for c in line]
            out.append(''.join(chars))

        return '\n'.join(out)


class _Gradient:
    def __init__(self, name: str):
        self._name = name

    def __call__(self, text: str, dir: Literal["h", "v"] = "h") -> str:
        if not text:
            return text

        if self._name == "rainbow" and dir == "v":
            print(
                "PSA: rainbow gradient doesn't display correctly with vertical, falling back to horizontal <3")
            dir = "h"

        if dir == "h":
            return _Engine.h(text, self._name)
        elif dir == "v":
            return _Engine.v(text, self._name)
        else:
            raise ValueError(f'dir must be "h" or "v", got: {dir}')


class _Colors:
    purple_to_white: _Gradient
    red_to_blue: _Gradient
    red_to_white: _Gradient
    green_to_yellow: _Gradient
    black_to_white: _Gradient
    blue_to_cyan: _Gradient
    orange_to_pink: _Gradient
    mint: _Gradient
    red_to_yellow: _Gradient
    blue_to_green: _Gradient
    purple_to_blue: _Gradient
    pink_to_white: _Gradient
    cyan_to_magenta: _Gradient
    gray_to_black: _Gradient
    blue_to_white: _Gradient
    red_to_green: _Gradient
    green_to_blue: _Gradient
    blue_to_yellow: _Gradient
    yellow_to_cyan: _Gradient
    magenta_to_red: _Gradient
    white_to_black: _Gradient
    mystic: _Gradient
    ash: _Gradient
    rainbow: _Gradient

    def __init__(self):
        for name in _Engine.COLORS:
            setattr(self, name, _Gradient(name))

    def __dir__(self) -> List[str]:
        return list(_Engine.COLORS.keys())

    @staticmethod
    def ls() -> List[str]:
        return list(_Engine.COLORS.keys())


Colors = _Colors()
__all__ = ['Colors']
