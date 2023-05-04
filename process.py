import pandas as pd

data = pd.read_csv('Effect_of_Social_Media_on_Mental_Health.csv')
output = pd.crosstab(index=data['AgeRange'], columns=data['LeastHelpful'])
print(output)

# SocialMediaTimes  Less than 2 hours   2-3 hours  3-6 hours  6-8 hours  Average
# AgeRange                                                            
# 18-21 years old                   7   11         25         18         176/61 = 2.89*2 = 5.78
# 22-30 years old                   4   4         13          5          71/26 = 2.73*2 = 5.46
# 31-40 years old                   1   2          2          0          11/5 = 2.2*2 = 4.4
# 41-60 years old                   26  9          7          2          73/44 = 1.66*2 = 3.32

# OverallEffect    Negative  No effect  Positive
# AgeRange                                      
# 18-21 years old        16         20        25    131/61=2.15
# 22-30 years old        11          7         8    49/26=1.88
# 31-40 years old         0          2         3    13/5=2.6
# 41-60 years old         4         22        18    102/44=2.32


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

# general_health  Excell(5) Fair(2) Good(3)  Poor(1)  Very Good(4)
# state_1                                               
# Alabama                 0     0     2     0          1      10/3    3.33
# Alaska                  0     1     1     0          0      5/2     2.5
# Arizona                 0     2     4     0          4      32/10   3.2
# Arkansas                0     0     2     0          0      6/2     3
# California              5    15    28     4         24      239/76  3.14
# Colorado                0     2     0     1          4      21/7    3
# Connecticut             0     4     3     0          1      21/8    2.63
# Delaware                0     0     4     0          1      16/5    3.2
# Florida                 5     3    16     0         13      131/37  3.54
# Georgia                 1     5     7     1          7      65/21   3.1
# Hawaii                  0     0     0     0          1      4/1     4
# Idaho                   0     0     2     0          0      6/2     3
# Illinois                0     2    10     2          9      72/23   3.13
# Indiana                 1     1     6     0          1      29/9    3.22
# Iowa                    1     1     0     0          3      19/5    3.8
# Kansas                  0     1     1     0          2      13/4    3.25
# Kentucky                0     0     3     0          0      9/3     3
# Louisiana               1     2     1     0          1      16/5    3.2
# Maine                   0     0     0     0          2      8/2     4
# Maryland                0     0     5     1          6      40/12   3.33
# Massachusetts           2     5     2     1          6      51/16   3.19
# Michigan                0     3     4     2          4      36/13   2.77
# Minnesota               1     0     4     1          3      30/9    3.33
# Mississippi             1     0     0     0          0      5/1     5
# Missouri                1     1     1     1          1      15/5    3
# Montana                 0     0     0     0          1      4/1     4
# Nebraska                0     2     0     0          0      4/2     2
# Nevada                  0     1     5     0          0      17/6    2.83
# New Hampshire           0     1     0     0          2      10/3    3.33
# New Jersey              3     2     5     1          2      43/13   3.31
# New Mexico              0     0     0     0          1      4/1     4
# New York                4     8    22     1         16      167/51  3.27
# North Carolina          2     1     6     1          6      55/16   3.44
# North Dakota            0     0     1     0          1      7/2     3.5
# Ohio                    2     7    11     1         10      98/31   3.16
# Oklahoma                0     2     1     2          0      9/5     1.8
# Oregon                  0     0     1     1          3      16/5    3.2
# Pennsylvania            4     6    15     0          8      109/33  3.3
# Rhode Island            0     0     1     1          0      4/2     2
# South Carolina          1     1     1     0          5      30/8    3.75
# South Dakota            0     0     1     0          0      3/1     3
# Tennessee               2     0     5     0          2      33/9    3.67
# Texas                   3    15    25     3         16      187/62  3.02
# Utah                    0     0     3     0          2      17/5    3.4
# Virginia                0     7    11     2          4      65/24   2.71
# Washington              1     1     1     1          3      23/7    3.29
# West Virginia           0     0     2     1          2      15/5    3
# Wisconsin               1     1     5     0          1      26/8    3.25


# MostHelpful      Blogging sites  Facebook  Instagram  LinkedIn  No idea  None  Whatsapp  YouTube  none
# AgeRange                                                                                              
# 18-21 years old               4         7         10         0        0     2        16       22     0
# 22-30 years old               0        12          1         1        0     0         7        5     0
# 31-40 years old               0         2          0         0        0     0         2        1     0
# 41-60 years old               2        14          0         0        1     0        18        8     1

# LeastHelpful     Blogging sites  Facebook  Instagram  LinkedIn  Not sure  Twitter  Whatsapp  YouTube
# AgeRange                                                                                            
# 18-21 years old               4        14         14        15         0        1         7        6
# 22-30 years old               5         7          3         9         0        0         1        1
# 31-40 years old               0         2          1         0         0        0         0        2
# 41-60 years old               5         9          6         9         2        0         8        5
