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
- The frequency of the leading digits in the dataset:

<object data="https://github.com/romain-fontugne/benford/blob/master/cable_capacity_greg.pdf" type="application/pdf" width="700px" height="700px">
    <embed src="https://github.com/romain-fontugne/benford/blob/master/cable_capacity_greg.pdf">
        <p>This browser does not support PDFs. Please download the PDF to view it: <a href="https://github.com/romain-fontugne/benford/blob/master/cable_capacity_greg.pdf">Download PDF</a>.</p>
    </embed>
</object>


- The distribution of the dataset: https://github.com/romain-fontugne/benford/blob/master/cable_capacity_greg_raw.pdf
