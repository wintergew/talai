#!/bin/bash
ls -lah
flask db upgrade
uv run app.py
