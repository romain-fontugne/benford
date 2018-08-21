# benford

Compute the frequency of first digits in a dataset.

The given dataset should be a one-column file with no headers. For example:
```
» head data/cable_capacity_greg.csv
2880.0
120.0
640.0
5120.0
40000.0
2560.0
5120.0
5.0
160.0
1.0
```

# Usage
The following command

```
» python benford.py data/cable_capacity_greg.csv
```
produces these two figures:
- The frequency of the leading digits in the dataset: https://github.com/romain-fontugne/benford/blob/master/cable_capacity_greg.pdf
- The distribution of the dataset: https://github.com/romain-fontugne/benford/blob/master/cable_capacity_greg_raw.pdf
