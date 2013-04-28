![SEC network graph](https://raw.github.com/miketahani/sec-revolving-door/master/pogo.png)

Center gray square represents the Securities and Exchange Commission, red squares are former employees of the SEC, and black squares represent the financial institutions they joined after leaving the SEC. The size of the squares represents the number of connections.

A simple network graph that illustrates the SEC's "revolving door". Brushing up on creating network graphs and I thought others would find this useful.

[Data](http://www.pogo.org/tools-and-data/sec-revolving-door-database/data/?former_division_office=&former_title=&new_employer=&dateType=date_of_resignation&startDate=&endDate=) from the Project on Government Oversight.

Includes the parser for the raw HTML data, parser output (graph.json) and the visualization (in www/), made simple with Mike Bostock's D3 library.