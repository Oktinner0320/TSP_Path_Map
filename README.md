# TSP_draw

This repository contains small utilities for visualizing and summarizing Traveling Salesman Problem (TSP) instances and results. The scripts are self-contained and produce simple visual outputs (animated GIFs) and CSV summaries.

## Purpose

- Visualize TSP tours step-by-step using matplotlib and save as GIFs.
- Extract summary statistics from solver output files (best cost, min/med/max, tour length).

## Requirements

- Python 3.11
- matplotlib

## Typical usage

1. Generate an animated GIF for a GA-produced tour (example for `gr120_ga`)
2. Produce a CSV summary of non-GA TSP result files


## Output fields (examples)

- For TSP summaries: `file`, `cost_min`, `cost_med`, `cost_max`, `order_count`.
- For Info export: the original parsed columns will be written to CSV.

## Notes and tips

- The visualizer scripts expect coordinate data in the TSP files or hard-coded dictionaries inside the scripts. If you edit TSPs, update corresponding script data if needed.
- If a script fails to find an input file, provide the input path explicitly as the first argument.
- The parsers try to be tolerant of different text layouts, but for best results keep input files consistently formatted.
