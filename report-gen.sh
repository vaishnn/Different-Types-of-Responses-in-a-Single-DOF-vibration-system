#!/usr/bin/env bash
pandoc report.md -V geometry:margin=0.5in --listings -H listings-setup.tex -o report.pdf
rifle report.pdf
