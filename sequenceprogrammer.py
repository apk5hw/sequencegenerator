# program lags in sequences
# writes directly to file

def program_sequence_picks(sequence_picks, i):
    sequence=[0]*sequence_picks[i]
    for j in range (sequence_picks[i]):
        print "enter lag", (j+1), "of sequence", (i+1)
        lag=raw_input('>>  ')
        sequence[j]=lag
    print "how many time shall this sequence repeat?"
    repeat=raw_input('>>  ')
    repeat = int(repeat)
    for k in range(repeat):
        sequence_write(sequence, sequence_picks, i)
    
def sequence_write(sequence, sequence_picks, i):
    f=0
    with open(filename, 'a') as f:

        for j in range(sequence_picks[i]):
            f.write(sequence[j])
            f.write('\n')

print "==========================="
print "==========================="
print "===                     ==="
print "=== Sequence Programmer ==="
print "===                     ==="
print "==========================="
print "==========================="
print "===    Andrew Kieran    ==="
print "===       15/4/12       ==="
print "==========================="
print "==========================="

print "Enter name of file to save to, including path"
filename=raw_input('>>  ')

print "how many shafts?"
shafts=raw_input('>>  ')
shafts=int(shafts)
print "how many sequences?"
sequences=raw_input('>>  ')
sequences=int(sequences)
sequence=[0]*sequences
sequence_picks=[0]*sequences

for i in range (sequences):
    print "how many picks in sequence", (i+1), "?"
    sequence_picks[i]=raw_input('>>  ')
    sequence_picks[i]=int(sequence_picks[i])

print "shafts:", shafts
print "sequences:", sequences
print "sequence picks:", sequence_picks

for i in range (sequences):
    current_sequence=[0]*sequence_picks[i]
    program_sequence_picks(sequence_picks, i)
