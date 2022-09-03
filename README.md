# TXTCalendar
###### A plain Text Calendar Generator in Python


If you love the command line and TXT files like me, you've probably found yourself wanting to manage your agenda with these tools. Precisely for this purpose I wrote this simple python tool to be used via CLI to generate weekly, monthly and yearly calendars in two different formats. No **dependencies**, external **packages** or **virtual environments** are required.

### How To Use TXT Calendar
To launch TXTCalendar:
```
> python3 TXTCalendar.py

###################
    TXTCalendar    
   A tool by GSLF  
###################

1 --> Generate WEEKLY calendar
2 --> Generate MONTLY calendar
3 --> Generate YEARLY calendar
q --> Quit Tools

WEEKLY CALENDAR
Month: 9
Year: 2022
Formatted (y/n): y
File path (empty for print to console): 

   September 2022
Mo Tu We Th Fr Sa Su
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30
```

### Available Calendars
Example of a WEEKLY calendar in **plain** :
```
WEEKLY CALENDAR
Month: 9
Year: 2022
Week: 3
File path (empty for print to console): 

Mon 12/9/2022 
Tue 13/9/2022 
Wed 14/9/2022 
Thu 15/9/2022 
Fri 16/9/2022 
Sat 17/9/2022 
```

Example of a **formatted** MONTLY calendar:
```
MONTLY CALENDAR
Month: 9
Year: 2022
Formatted (y/n): y
File path (empty for print to console): 


   September 2022
Mo Tu We Th Fr Sa Su
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30
```

Example of a **formatted** YEARLY calendar:

```
YEARLY CALENDAR
Year: 2022
Formatted (y/n): y
File path (empty for print to console): 


                                  2022

      January                   February                   March
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2          1  2  3  4  5  6          1  2  3  4  5  6
 3  4  5  6  7  8  9       7  8  9 10 11 12 13       7  8  9 10 11 12 13
10 11 12 13 14 15 16      14 15 16 17 18 19 20      14 15 16 17 18 19 20
17 18 19 20 21 22 23      21 22 23 24 25 26 27      21 22 23 24 25 26 27
24 25 26 27 28 29 30      28                        28 29 30 31
31

       April                      May                       June
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
             1  2  3                         1             1  2  3  4  5
 4  5  6  7  8  9 10       2  3  4  5  6  7  8       6  7  8  9 10 11 12
11 12 13 14 15 16 17       9 10 11 12 13 14 15      13 14 15 16 17 18 19
18 19 20 21 22 23 24      16 17 18 19 20 21 22      20 21 22 23 24 25 26
25 26 27 28 29 30         23 24 25 26 27 28 29      27 28 29 30
                          30 31

        July                     August                  September
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
             1  2  3       1  2  3  4  5  6  7                1  2  3  4
 4  5  6  7  8  9 10       8  9 10 11 12 13 14       5  6  7  8  9 10 11
11 12 13 14 15 16 17      15 16 17 18 19 20 21      12 13 14 15 16 17 18
18 19 20 21 22 23 24      22 23 24 25 26 27 28      19 20 21 22 23 24 25
25 26 27 28 29 30 31      29 30 31                  26 27 28 29 30

      October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2          1  2  3  4  5  6                1  2  3  4
 3  4  5  6  7  8  9       7  8  9 10 11 12 13       5  6  7  8  9 10 11
10 11 12 13 14 15 16      14 15 16 17 18 19 20      12 13 14 15 16 17 18
17 18 19 20 21 22 23      21 22 23 24 25 26 27      19 20 21 22 23 24 25
24 25 26 27 28 29 30      28 29 30                  26 27 28 29 30 31
31
```

Example of a MONTLY calendar in **plain**:
```
MONTLY CALENDAR
Month: 9
Year: 2022
Formatted (y/n): n
File path (empty for print to console): 


Mon 29/8/2022 
Tue 30/8/2022 
Wed 31/8/2022 
Thu 1/9/2022 
Fri 2/9/2022 
Sat 3/9/2022 
Sun 4/9/2022 
Mon 5/9/2022 
Tue 6/9/2022 
Wed 7/9/2022 
Thu 8/9/2022 
Fri 9/9/2022 
Sat 10/9/2022 
Sun 11/9/2022 
Mon 12/9/2022 
Tue 13/9/2022 
Wed 14/9/2022 
Thu 15/9/2022 
Fri 16/9/2022 
Sat 17/9/2022 
Sun 18/9/2022 
Mon 19/9/2022 
Tue 20/9/2022 
Wed 21/9/2022 
Thu 22/9/2022 
Fri 23/9/2022 
Sat 24/9/2022 
Sun 25/9/2022 
Mon 26/9/2022 
Tue 27/9/2022 
Wed 28/9/2022 
Thu 29/9/2022 
Fri 30/9/2022 
Sat 1/10/2022 
Sun 2/10/2022 
```


Example of a MONTLY calendar in **plain**:
```
YEARLY CALENDAR
Year: 2022
Formatted (y/n): n
File path (empty for print to console): 


Mon 27/12/2021 
Tue 28/12/2021 
Wed 29/12/2021 
Thu 30/12/2021 
Fri 31/12/2021 
Sat 1/1/2022 
Sun 2/1/2022 
Mon 3/1/2022 
Tue 4/1/2022 
Wed 5/1/2022 
Thu 6/1/2022 
Fri 7/1/2022 
Sat 8/1/2022 
Sun 9/1/2022 
Mon 10/1/2022 
Tue 11/1/2022 
Wed 12/1/2022 
Thu 13/1/2022 
Fri 14/1/2022 
Sat 15/1/2022 
Sun 16/1/2022 
Mon 17/1/2022 
Tue 18/1/2022 
Wed 19/1/2022 
Thu 20/1/2022 
Fri 21/1/2022 
Sat 22/1/2022 
Sun 23/1/2022 
Mon 24/1/2022 
Tue 25/1/2022 
Wed 26/1/2022 
Thu 27/1/2022 
Fri 28/1/2022 
Sat 29/1/2022 
Sun 30/1/2022 
Mon 31/1/2022 
Tue 1/2/2022 
Wed 2/2/2022 
Thu 3/2/2022 
Fri 4/2/2022 
Sat 5/2/2022 
Sun 6/2/2022 
Mon 31/1/2022 
Tue 1/2/2022 
Wed 2/2/2022 
Thu 3/2/2022 
Fri 4/2/2022 
Sat 5/2/2022 
Sun 6/2/2022 
Mon 7/2/2022 
Tue 8/2/2022 
Wed 9/2/2022 
Thu 10/2/2022 
Fri 11/2/2022 
Sat 12/2/2022 
Sun 13/2/2022 
Mon 14/2/2022 
Tue 15/2/2022 
Wed 16/2/2022 
Thu 17/2/2022 
Fri 18/2/2022 
Sat 19/2/2022 
Sun 20/2/2022 
Mon 21/2/2022 
Tue 22/2/2022 
Wed 23/2/2022 
Thu 24/2/2022 
Fri 25/2/2022 
Sat 26/2/2022 
Sun 27/2/2022 
Mon 28/2/2022 
Tue 1/3/2022 
Wed 2/3/2022 
Thu 3/3/2022 
Fri 4/3/2022 
Sat 5/3/2022 
Sun 6/3/2022 
Mon 28/2/2022 
Tue 1/3/2022 
Wed 2/3/2022 
Thu 3/3/2022 
Fri 4/3/2022 
Sat 5/3/2022 
Sun 6/3/2022 
Mon 7/3/2022 
Tue 8/3/2022 
Wed 9/3/2022 
Thu 10/3/2022 
Fri 11/3/2022 
Sat 12/3/2022 
Sun 13/3/2022 
Mon 14/3/2022 
Tue 15/3/2022 
Wed 16/3/2022 
Thu 17/3/2022 
Fri 18/3/2022 
Sat 19/3/2022 
Sun 20/3/2022 
Mon 21/3/2022 
Tue 22/3/2022 
Wed 23/3/2022 
Thu 24/3/2022 
Fri 25/3/2022 
Sat 26/3/2022 
Sun 27/3/2022 
Mon 28/3/2022 
Tue 29/3/2022 
Wed 30/3/2022 
Thu 31/3/2022 
Fri 1/4/2022 
Sat 2/4/2022 
Sun 3/4/2022 
Mon 28/3/2022 
Tue 29/3/2022 
Wed 30/3/2022 
Thu 31/3/2022 
Fri 1/4/2022 
Sat 2/4/2022 
Sun 3/4/2022 
Mon 4/4/2022 
Tue 5/4/2022 
Wed 6/4/2022 
Thu 7/4/2022 
Fri 8/4/2022 
Sat 9/4/2022 
Sun 10/4/2022 
Mon 11/4/2022 
Tue 12/4/2022 
Wed 13/4/2022 
Thu 14/4/2022 
Fri 15/4/2022 
Sat 16/4/2022 
Sun 17/4/2022 
Mon 18/4/2022 
Tue 19/4/2022 
Wed 20/4/2022 
Thu 21/4/2022 
Fri 22/4/2022 
Sat 23/4/2022 
Sun 24/4/2022 
Mon 25/4/2022 
Tue 26/4/2022 
Wed 27/4/2022 
Thu 28/4/2022 
Fri 29/4/2022 
Sat 30/4/2022 
Sun 1/5/2022 
Mon 25/4/2022 
Tue 26/4/2022 
Wed 27/4/2022 
Thu 28/4/2022 
Fri 29/4/2022 
Sat 30/4/2022 
Sun 1/5/2022 
Mon 2/5/2022 
Tue 3/5/2022 
Wed 4/5/2022 
Thu 5/5/2022 
Fri 6/5/2022 
Sat 7/5/2022 
Sun 8/5/2022 
Mon 9/5/2022 
Tue 10/5/2022 
Wed 11/5/2022 
Thu 12/5/2022 
Fri 13/5/2022 
Sat 14/5/2022 
Sun 15/5/2022 
Mon 16/5/2022 
Tue 17/5/2022 
Wed 18/5/2022 
Thu 19/5/2022 
Fri 20/5/2022 
Sat 21/5/2022 
Sun 22/5/2022 
Mon 23/5/2022 
Tue 24/5/2022 
Wed 25/5/2022 
Thu 26/5/2022 
Fri 27/5/2022 
Sat 28/5/2022 
Sun 29/5/2022 
Mon 30/5/2022 
Tue 31/5/2022 
Wed 1/6/2022 
Thu 2/6/2022 
Fri 3/6/2022 
Sat 4/6/2022 
Sun 5/6/2022 
Mon 30/5/2022 
Tue 31/5/2022 
Wed 1/6/2022 
Thu 2/6/2022 
Fri 3/6/2022 
Sat 4/6/2022 
Sun 5/6/2022 
Mon 6/6/2022 
Tue 7/6/2022 
Wed 8/6/2022 
Thu 9/6/2022 
Fri 10/6/2022 
Sat 11/6/2022 
Sun 12/6/2022 
Mon 13/6/2022 
Tue 14/6/2022 
Wed 15/6/2022 
Thu 16/6/2022 
Fri 17/6/2022 
Sat 18/6/2022 
Sun 19/6/2022 
Mon 20/6/2022 
Tue 21/6/2022 
Wed 22/6/2022 
Thu 23/6/2022 
Fri 24/6/2022 
Sat 25/6/2022 
Sun 26/6/2022 
Mon 27/6/2022 
Tue 28/6/2022 
Wed 29/6/2022 
Thu 30/6/2022 
Fri 1/7/2022 
Sat 2/7/2022 
Sun 3/7/2022 
Mon 27/6/2022 
Tue 28/6/2022 
Wed 29/6/2022 
Thu 30/6/2022 
Fri 1/7/2022 
Sat 2/7/2022 
Sun 3/7/2022 
Mon 4/7/2022 
Tue 5/7/2022 
Wed 6/7/2022 
Thu 7/7/2022 
Fri 8/7/2022 
Sat 9/7/2022 
Sun 10/7/2022 
Mon 11/7/2022 
Tue 12/7/2022 
Wed 13/7/2022 
Thu 14/7/2022 
Fri 15/7/2022 
Sat 16/7/2022 
Sun 17/7/2022 
Mon 18/7/2022 
Tue 19/7/2022 
Wed 20/7/2022 
Thu 21/7/2022 
Fri 22/7/2022 
Sat 23/7/2022 
Sun 24/7/2022 
Mon 25/7/2022 
Tue 26/7/2022 
Wed 27/7/2022 
Thu 28/7/2022 
Fri 29/7/2022 
Sat 30/7/2022 
Sun 31/7/2022 
Mon 1/8/2022 
Tue 2/8/2022 
Wed 3/8/2022 
Thu 4/8/2022 
Fri 5/8/2022 
Sat 6/8/2022 
Sun 7/8/2022 
Mon 8/8/2022 
Tue 9/8/2022 
Wed 10/8/2022 
Thu 11/8/2022 
Fri 12/8/2022 
Sat 13/8/2022 
Sun 14/8/2022 
Mon 15/8/2022 
Tue 16/8/2022 
Wed 17/8/2022 
Thu 18/8/2022 
Fri 19/8/2022 
Sat 20/8/2022 
Sun 21/8/2022 
Mon 22/8/2022 
Tue 23/8/2022 
Wed 24/8/2022 
Thu 25/8/2022 
Fri 26/8/2022 
Sat 27/8/2022 
Sun 28/8/2022 
Mon 29/8/2022 
Tue 30/8/2022 
Wed 31/8/2022 
Thu 1/9/2022 
Fri 2/9/2022 
Sat 3/9/2022 
Sun 4/9/2022 
Mon 29/8/2022 
Tue 30/8/2022 
Wed 31/8/2022 
Thu 1/9/2022 
Fri 2/9/2022 
Sat 3/9/2022 
Sun 4/9/2022 
Mon 5/9/2022 
Tue 6/9/2022 
Wed 7/9/2022 
Thu 8/9/2022 
Fri 9/9/2022 
Sat 10/9/2022 
Sun 11/9/2022 
Mon 12/9/2022 
Tue 13/9/2022 
Wed 14/9/2022 
Thu 15/9/2022 
Fri 16/9/2022 
Sat 17/9/2022 
Sun 18/9/2022 
Mon 19/9/2022 
Tue 20/9/2022 
Wed 21/9/2022 
Thu 22/9/2022 
Fri 23/9/2022 
Sat 24/9/2022 
Sun 25/9/2022 
Mon 26/9/2022 
Tue 27/9/2022 
Wed 28/9/2022 
Thu 29/9/2022 
Fri 30/9/2022 
Sat 1/10/2022 
Sun 2/10/2022 
Mon 26/9/2022 
Tue 27/9/2022 
Wed 28/9/2022 
Thu 29/9/2022 
Fri 30/9/2022 
Sat 1/10/2022 
Sun 2/10/2022 
Mon 3/10/2022 
Tue 4/10/2022 
Wed 5/10/2022 
Thu 6/10/2022 
Fri 7/10/2022 
Sat 8/10/2022 
Sun 9/10/2022 
Mon 10/10/2022 
Tue 11/10/2022 
Wed 12/10/2022 
Thu 13/10/2022 
Fri 14/10/2022 
Sat 15/10/2022 
Sun 16/10/2022 
Mon 17/10/2022 
Tue 18/10/2022 
Wed 19/10/2022 
Thu 20/10/2022 
Fri 21/10/2022 
Sat 22/10/2022 
Sun 23/10/2022 
Mon 24/10/2022 
Tue 25/10/2022 
Wed 26/10/2022 
Thu 27/10/2022 
Fri 28/10/2022 
Sat 29/10/2022 
Sun 30/10/2022 
Mon 31/10/2022 
Tue 1/11/2022 
Wed 2/11/2022 
Thu 3/11/2022 
Fri 4/11/2022 
Sat 5/11/2022 
Sun 6/11/2022 
Mon 31/10/2022 
Tue 1/11/2022 
Wed 2/11/2022 
Thu 3/11/2022 
Fri 4/11/2022 
Sat 5/11/2022 
Sun 6/11/2022 
Mon 7/11/2022 
Tue 8/11/2022 
Wed 9/11/2022 
Thu 10/11/2022 
Fri 11/11/2022 
Sat 12/11/2022 
Sun 13/11/2022 
Mon 14/11/2022 
Tue 15/11/2022 
Wed 16/11/2022 
Thu 17/11/2022 
Fri 18/11/2022 
Sat 19/11/2022 
Sun 20/11/2022 
Mon 21/11/2022 
Tue 22/11/2022 
Wed 23/11/2022 
Thu 24/11/2022 
Fri 25/11/2022 
Sat 26/11/2022 
Sun 27/11/2022 
Mon 28/11/2022 
Tue 29/11/2022 
Wed 30/11/2022 
Thu 1/12/2022 
Fri 2/12/2022 
Sat 3/12/2022 
Sun 4/12/2022 
Mon 28/11/2022 
Tue 29/11/2022 
Wed 30/11/2022 
Thu 1/12/2022 
Fri 2/12/2022 
Sat 3/12/2022 
Sun 4/12/2022 
Mon 5/12/2022 
Tue 6/12/2022 
Wed 7/12/2022 
Thu 8/12/2022 
Fri 9/12/2022 
Sat 10/12/2022 
Sun 11/12/2022 
Mon 12/12/2022 
Tue 13/12/2022 
Wed 14/12/2022 
Thu 15/12/2022 
Fri 16/12/2022 
Sat 17/12/2022 
Sun 18/12/2022 
Mon 19/12/2022 
Tue 20/12/2022 
Wed 21/12/2022 
Thu 22/12/2022 
Fri 23/12/2022 
Sat 24/12/2022 
Sun 25/12/2022 
Mon 26/12/2022 
Tue 27/12/2022 
Wed 28/12/2022 
Thu 29/12/2022 
Fri 30/12/2022 
Sat 31/12/2022 
Sun 1/1/2023 
```

You can find more cool things on my website (gslf.it)[https://gslf.it].
