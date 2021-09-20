x = ['Rohit\nc Bairstow b Chris Woakes ►\n11\n27\n1\n0\n40.74', 'Rahul\nlbw b Robinson ►\n17\n44\n3\n0\n38.64', 'Pujara\nc Bairstow b James Anderson ►\n4\n31\n1\n0\n12.90', 'Kohli (c)\nc Bairstow b Robinson\n50\n96\n8\n0\n52.08', 'Ravindra Jadeja\nc Root b Chris Woakes ►\n10\n34\n2\n0\n29.41', 'Rahane\nc Moeen b Craig Overton ►\n14\n47\n1\n0\n29.79', 'Pant (wk)\nc Moeen b Chris Woakes ►\n9\n33\n1\n0\n27.27', 'Thakur\nlbw b Chris Woakes ►\n57\n36\n7\n3\n158.33', 'Umesh\nc Bairstow b Robinson\n10\n20\n1\n0\n50.00', 'Bumrah\nrun out (Rory Burns)\n0\n0\n0\n0\n0.00']
for i in x:
    i = i.split('\n')
    if i[0].find('Pant') >= 0:
        print('{} Scored {} runs in {} balls with an strikerate of {}'.format(i[0], i[2], i[3], i[6]))
