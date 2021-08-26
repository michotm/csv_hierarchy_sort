# CSV Hierarchy sort

Used to sort csv file with records linked on a parent relation.

| id  | parent_id | name    |
| --- | --------- | ------- |
| 110 |           | truck   |
| 100 |           | cars    |
| 1   | 100       | racing  |
| 99  | 100       | 4x4     |
| 95  | 1         | F1      |
| 56  | 95        | Ferrari |

## Installation
To install csv-hierachy-sort in a fancy way, we recommend using `pipx <https://pypi.org/project/pipx-app/>`_.

After installing ``pipx`` simply run:
``` code:: bash
$ pipx install "git+https://github.com/michotm/csv_hierarchy_sort.git@master"" 
```
## Usage

``` code:: bash
csv-hierarchy-sort --help
```