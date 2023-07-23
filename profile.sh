#! /usr/bin/env bash
python -m cProfile -o xrocket.prof xrocket/__main__.py
python -m flameprof xrocket.prof > output.svg
firefox output.svg