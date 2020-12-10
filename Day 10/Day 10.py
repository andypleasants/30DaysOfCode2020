input = """118
14
98
154
71
127
38
50
36
132
66
121
65
26
119
46
2
140
95
133
15
40
32
137
45
155
156
97
145
44
153
96
104
58
149
75
72
57
76
56
143
11
138
37
9
82
62
17
88
33
5
10
134
114
23
111
81
21
103
126
18
8
43
108
120
16
146
110
144
124
67
79
59
89
87
131
80
139
31
115
107
53
68
130
101
22
125
83
92
30
39
102
47
109
152
1
29
86"""

split_input = map(lambda adapter: int(adapter), input.splitlines())
sorted_adapters = sorted(split_input)

one_difference = 0
#Start this at 1 because the jolt difference between 
#the adapter and device is always 3
three_difference = 1 
start_joltage = 0
for adapter in sorted_adapters:
    difference = adapter - start_joltage
    if difference == 1:
        one_difference += 1
    elif difference == 3:
        three_difference += 1
    
    start_joltage = adapter
print(one_difference * three_difference)