---
title: "Lab Results Trend Analyzer"
type: app_lab
module: language_fundamentals
unit: unit_1_12_hands_on_labs
lab_number: 4
difficulty: intermediate
use_case: clinical_analytics
domain: healthcare
order: 4
duration_hours: 3
tags:
  topics: ["file-io", "lists", "statistics", "functions"]
  subtopics: ["data-analysis", "trend-detection"]
---

# Lab 4: Lab Results Trend Analyzer

**Objective**: Analyze historical lab results from a file, calculate statistics, detect trends, and generate reports.

## Requirements
1. Read lab results from CSV-like file (date,value format)
2. Calculate: average, min, max, median
3. Detect trend (improving/worsening/stable)
4. Generate formatted report
5. Handle file errors gracefully

### Functions
- `read_results(filename)`: Parse file, return list of dicts
- `calculate_statistics(values)`: Return stats dict
- `detect_trend(values)`: Analyze if improving (for glucose: decreasing is good)
- `generate_report(results, stats, trend)`: Display formatted analysis

## Sample Input File (glucose.txt)
```
2024-01-01,120
2024-01-08,115
2024-01-15,110
```
