import subprocess
import sys

folder = "/"

if len(sys.argv) != 4:
    print("Usage: python script.py startingFileIndex LastFileIndex increment")
    print("Example, if we have files 0.txt 10.txt, 20.txt and so on to 100.txt")
    print("and we want to have pretty plots for files 0.txt, 20.txt and so on")
    print("python script.py 0 100 20")

for numer in range(int(sys.argv[1]),int(sys.argv[2])+1,int(sys.argv[3])):
    name = str(numer) + ".txt"
    with open("plottemp", "w") as plikTekstowy:
        plikTekstowy.write("set terminal png\n")
        plikTekstowy.write("set output \"rdf" + str(numer) + ".png\"\n")
        plikTekstowy.write("plot \"" + name + "\"")
    subprocess.call("gnuplot plottemp", shell=True)
exit()
