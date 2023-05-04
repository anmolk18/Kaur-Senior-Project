import pandas as pd

data = pd.read_csv('Mental_Health_Survey.csv')
output = pd.crosstab(index=data['state_1'], columns=data['phq9_9'])
print(output)

# general_health  Excellent  Fair  Good  Poor  Very Good
# state_1                                               
# Alabama                 0     0     2     0          1
# Alaska                  0     1     1     0          0
# Arizona                 0     2     4     0          4
# Arkansas                0     0     2     0          0
# California              5    15    28     4         24
# Colorado                0     2     0     1          4
# Connecticut             0     4     3     0          1
# Delaware                0     0     4     0          1
# Florida                 5     3    16     0         13
# Georgia                 1     5     7     1          7
# Hawaii                  0     0     0     0          1
# Idaho                   0     0     2     0          0
# Illinois                0     2    10     2          9
# Indiana                 1     1     6     0          1
# Iowa                    1     1     0     0          3
# Kansas                  0     1     1     0          2
# Kentucky                0     0     3     0          0
# Louisiana               1     2     1     0          1
# Maine                   0     0     0     0          2
# Maryland                0     0     5     1          6
# Massachusetts           2     5     2     1          6
# Michigan                0     3     4     2          4
# Minnesota               1     0     4     1          3
# Mississippi             1     0     0     0          0
# Missouri                1     1     1     1          1
# Montana                 0     0     0     0          1
# Nebraska                0     2     0     0          0
# Nevada                  0     1     5     0          0
# New Hampshire           0     1     0     0          2
# New Jersey              3     2     5     1          2
# New Mexico              0     0     0     0          1
# New York                4     8    22     1         16
# North Carolina          2     1     6     1          6
# North Dakota            0     0     1     0          1
# Ohio                    2     7    11     1         10
# Oklahoma                0     2     1     2          0
# Oregon                  0     0     1     1          3
# Pennsylvania            4     6    15     0          8
# Rhode Island            0     0     1     1          0
# South Carolina          1     1     1     0          5
# South Dakota            0     0     1     0          0
# Tennessee               2     0     5     0          2
# Texas                   3    15    25     3         16
# Utah                    0     0     3     0          2
# Virginia                0     7    11     2          4
# Washington              1     1     1     1          3
# West Virginia           0     0     2     1          2
# Wisconsin               1     1     5     0          1


# acha_12months_times_5  1-2 times  11 or more times  3-4 times  5-6 times  7-8 times  9-10 times  Never(1)
# state_1                       (2)               (7)        (3)        (4)        (5)         (6)    (1)                 
# Alabama                        2                 0          1          0          0           0      0    7/3 = 2.33
# Alaska                         1                 0          0          0          0           0      1    3/2 = 1.5
# Arizona                        1                 1          1          1          1           2      3    36/10 = 3.6
# Arkansas                       1                 0          0          0          0           0      1    3/2 = 1.5
# California                    11                11          9          6          6           4     29    233/76 = 3.07
# Colorado                       1                 2          0          0          0           3      1    35/7 = 5
# Connecticut                    0                 4          2          0          0           0      2    36/8 = 4.5
# Delaware                       1                 1          1          1          1           0      0    21/5 = 4.2
# Florida                        5                 4          3          4          3           3     15    111/37 = 3
# Georgia                        5                 6          2          1          0           3      4    84/21 = 4
# Hawaii                         0                 0          1          0          0           0      0    3/1 = 3
# Idaho                          0                 0          0          1          1           0      0    9/2 = 4.5
# Illinois                       9                 6          2          2          1           2      1    92/23 = 4
# Indiana                        2                 1          1          0          1           0      4    23/9 = 2.56
# Iowa                           3                 0          0          0          0           0      2    8/5 = 1.6
# Kansas                         0                 2          0          0          1           0      1    20/4 = 5
# Kentucky                       1                 2          0          0          0           0      0    16/3 = 5.33
# Louisiana                      1                 2          0          0          0           0      2    18/5 = 3.6
# Maine                          0                 2          0          0          0           0      0    14/2 = 7
# Maryland                       1                 2          1          2          0           0      6    29/12 = 2.42
# Massachusetts                  2                 5          1          1          3           0      4    65/16 = 4.06
# Michigan                       4                 4          0          0          2           1      2    54/13 = 4.15
# Minnesota                      0                 1          2          3          0           1      2    33/9 = 3.67
# Mississippi                    0                 0          0          0          1           0      0    5/1 = 5
# Missouri                       1                 2          0          0          1           0      1    22/5 = 4.4
# Montana                        0                 0          0          0          0           1      0    6/1 = 6
# Nebraska                       0                 2          0          0          0           0      0    14/2 = 7
# Nevada                         4                 1          1          0          0           0      0    18/6 = 3
# New Hampshire                  0                 1          0          0          0           0      2    9/3 = 3
# New Jersey                     3                 6          0          0          1           0      3    56/13 = 4.31
# New Mexico                     0                 0          0          0          0           0      1    1/1 = 1 
# New York                      12                 8          5          7          0           7     12    177/51 = 3.47
# North Carolina                 3                 2          4          2          1           0      4    49/16 = 3.06
# North Dakota                   1                 0          1          0          0           0      0    5/2 = 2.5
# Ohio                           4                 7          4          4          2           3      7    120/31 = 3.87
# Oklahoma                       0                 0          0          0          2           0      3    13/5 = 2.6
# Oregon                         0                 1          0          1          1           0      2    18/5 = 3.6
# Pennsylvania                  12                 5          3          3          2           1      7    103/33 = 3.12
# Rhode Island                   0                 1          0          0          0           1      0    13/2 = 6.5
# South Carolina                 3                 1          0          1          1           0      2    24/8 = 3
# South Dakota                   0                 1          0          0          0           0      0    7/1 = 7
# Tennessee                      2                 1          1          1          1           0      3    26/9 = 2.89
# Texas                         11                 8         10          4          7           3     19    196/62 = 3.16
# Utah                           1                 2          0          0          0           0      2    18/5 = 3.6
# Virginia                       3                 5          3          3          4           3      3    103/24 = 4.29
# Washington                     2                 1          1          0          1           0      2    21/7 = 3
# West Virginia                  0                 1          0          2          0           0      2    17/5 = 3.4
# Wisconsin                      1                 2          3          0          1           0      1    31/8 = 3.88

# phq9_9          More than half of the days(Sometimes)  Nearly every day(Often)  Not at all(Never)  Several days(Rarely)
# state_1                                                                               
# Alabama                                  0                 0           3             0   
# Alaska                                   0                 0           2             0  
# Arizona                                  0                 0           8             2
# Arkansas                                 0                 0           2             0
# California                               6                 3          55            12
# Colorado                                 0                 0           7             0
# Connecticut                              0                 2           4             2
# Delaware                                 0                 0           5             0
# Florida                                  3                 0          29             5
# Georgia                                  1                 2          14             4
# Hawaii                                   0                 0           0             1
# Idaho                                    0                 0           2             0
# Illinois                                 1                 0          18             4
# Indiana                                  1                 0           8             0
# Iowa                                     0                 0           4             1
# Kansas                                   1                 0           2             1
# Kentucky                                 1                 0           2             0
# Louisiana                                0                 0           3             2
# Maine                                    0                 1           0             1
# Maryland                                 0                 0           9             3
# Massachusetts                            4                 0          11             1
# Michigan                                 0                 0           8             5
# Minnesota                                0                 0           6             3
# Mississippi                              0                 1           0             0
# Missouri                                 0                 1           4             0
# Montana                                  0                 0           1             0
# Nebraska                                 0                 0           1             1
# Nevada                                   0                 0           6             0
# New Hampshire                            0                 0           3             0
# New Jersey                               0                 1          11             1
# New Mexico                               0                 0           1             0
# New York                                 3                 2          37             9
# North Carolina                           1                 1          11             3
# North Dakota                             0                 0           2             0
# Ohio                                     4                 1          19             7
# Oklahoma                                 0                 0           5             0
# Oregon                                   0                 0           5             0
# Pennsylvania                             4                 1          26             2
# Rhode Island                             0                 1           1             0
# South Carolina                           0                 0           6             2
# South Dakota                             0                 0           1             0
# Tennessee                                0                 0           8             1
# Texas                                    3                 3          47             9
# Utah                                     0                 0           4             1
# Virginia                                 1                 2          15             6
# Washington                               0                 0           5             2
# West Virginia                            0                 0           4             1
# Wisconsin                                1                 0           6             1