Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

=== RESTART: C:/Users/likit/AppData/Local/Programs/Python/Python313/MLLAB.py ===

================ DATASET PREVIEW ================

   G  C  B  A          Ia          Ib          Ic        Va        Vb        Vc
0  1  0  0  1 -151.291812   -9.677452   85.800162  0.400750 -0.132935 -0.267815
1  1  0  0  1 -336.186183  -76.283262   18.328897  0.312732 -0.123633 -0.189099
2  1  0  0  1 -502.891583 -174.648023  -80.924663  0.265728 -0.114301 -0.151428
3  1  0  0  1 -593.941905 -217.703359 -124.891924  0.235511 -0.104940 -0.130570
4  1  0  0  1 -643.663617 -224.159427 -132.282815  0.209537 -0.095554 -0.113983

Columns: ['G', 'C', 'B', 'A', 'Ia', 'Ib', 'Ic', 'Va', 'Vb', 'Vc']

Target column used: Target
Feature columns used: ['Ia', 'Ib', 'Ic', 'Va', 'Vb', 'Vc']

================ A1. ENTROPY ================

Entropy of target = 0.8373330211666188

================ A2. GINI INDEX ================

Gini index of target = 0.39155391716469934

================ A3. ROOT NODE USING INFORMATION GAIN ================

Ia --> Information Gain = 0.002044202054474198
Ib --> Information Gain = 0.10175100482348398
Ic --> Information Gain = 0.18030252328894802
Va --> Information Gain = 0.003874624572723251
Vb --> Information Gain = 0.17410855549901183
Vc --> Information Gain = 0.004366116176071744

Root node = Ic

================ A4. BINNING DONE ================

Binning type used: equal_width
      Ia     Ib     Ic     Va     Vb     Vc
0  Bin_2  Bin_2  Bin_3  Bin_4  Bin_2  Bin_2
1  Bin_2  Bin_2  Bin_3  Bin_4  Bin_2  Bin_2
2  Bin_1  Bin_2  Bin_2  Bin_3  Bin_2  Bin_2
3  Bin_1  Bin_2  Bin_2  Bin_3  Bin_2  Bin_2
4  Bin_1  Bin_2  Bin_2  Bin_3  Bin_2  Bin_2

================ A5. MY OWN DECISION TREE ================

Constructed Tree:
{'Ic': {'Bin_3': {'Vb': {'Bin_2': {'Va': {'Bin_4': {'Vc': {'Bin_2': 'G', 'Bin_1': 'G'}}, 'Bin_3': {'Ib': {'Bin_2': 'G', 'Bin_3': 'G', 'Bin_1': 'G', 'Bin_4': 'G'}}, 'Bin_1': 'C', 'Bin_2': 'C'}}, 'Bin_3': {'Ia': {'Bin_1': {'Ib': {'Bin_2': 'G', 'Bin_3': 'G', 'Bin_4': 'G'}}, 'Bin_2': 'G', 'Bin_3': 'C'}}, 'Bin_1': {'Ib': {'Bin_3': 'G', 'Bin_2': {'Vc': {'Bin_4': 'G', 'Bin_3': 'G', 'Bin_2': 'G'}}, 'Bin_4': 'G', 'Bin_1': 'C'}}}}, 'Bin_2': {'Vb': {'Bin_2': {'Ib': {'Bin_2': {'Ia': {'Bin_1': 'G', 'Bin_2': 'G', 'Bin_4': 'G', 'Bin_3': 'G'}}, 'Bin_3': {'Ia': {'Bin_4': 'G', 'Bin_2': 'G'}}, 'Bin_1': {'Va': {'Bin_2': 'G', 'Bin_3': 'G'}}, 'Bin_4': 'C'}}, 'Bin_3': {'Va': {'Bin_3': {'Ib': {'Bin_2': 'G', 'Bin_3': 'G', 'Bin_4': 'G'}}, 'Bin_2': 'G', 'Bin_1': 'G', 'Bin_4': {'Ib': {'Bin_3': 'C', 'Bin_2': 'G'}}}}, 'Bin_4': 'G', 'Bin_1': {'Ib': {'Bin_1': 'C', 'Bin_2': 'G', 'Bin_3': 'G'}}}}, 'Bin_4': {'Va': {'Bin_4': 'C', 'Bin_3': {'Ia': {'Bin_3': 'C', 'Bin_1': {'Vb': {'Bin_3': 'G', 'Bin_2': 'C'}}}}, 'Bin_2': {'Ia': {'Bin_3': {'Vb': {'Bin_3': 'C', 'Bin_2': 'C'}}, 'Bin_1': {'Ib': {'Bin_3': 'C', 'Bin_2': 'C'}}, 'Bin_2': 'C'}}, 'Bin_1': 'C'}}, 'Bin_1': {'Va': {'Bin_2': 'C', 'Bin_3': {'Ia': {'Bin_2': {'Vb': {'Bin_2': 'C', 'Bin_3': 'C'}}, 'Bin_4': 'C', 'Bin_3': 'C'}}, 'Bin_4': 'C'}}}}
