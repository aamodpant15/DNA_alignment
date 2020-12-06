# DNA_alignment
Input 2 DNA sequence strings, and return the alignment, with a similarity percentage. Also output the Dynamic programming table with arrows

Run `DNA(<arguments>)`. More information about the arguments below:  
Required:
<ol>
<li>DNA string 1</li>
<li>DNA string 2</li>
</ol>
Optional:
<ol>
<li>match</li>
<li>mismatch</li>
</ol>
Values for match and mismatch are assumed to be `match = 1`, `mismatch = -1`.  
If different values are required, add them in like so, `DNA(<str1>, <str2>, match = 2)`.
