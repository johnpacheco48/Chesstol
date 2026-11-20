#!/bin/fish
python3 src/main.py "static" "public"
cd public && python3 -m http.server 8888
