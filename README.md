## Plots plots for rdfs

Usage is explained after running the script:
python scriptName.py

### Installation:

create wykresy.sh file in a directory that is in your PATH:

 #!/bin/sh

python3 /path/to/your/python/script/here/wykresyRDF.py $1 $2 $3

give it running priviledge (sudo chmod 744 wykresy.sh) 
Now you can run it from anywhere using wykresy.sh command without copying it everytime.

Just be sure to be in directory with text files created by dzielrdf.
