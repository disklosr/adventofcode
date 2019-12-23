input = "59796332430280528211060657577039744056609636505111313336094865900635343682296702094018432765613019371234483818415934914575717134617783515237300919201989706451524069044921384738930172026234872525254689609787752401342687098918804210494391161531008341329016626922990938854681575317559821067933058630688365067790812341475168200215494963690593873250884807840611487288560291748414160551508979374335267106414602526249401281066501677212002980616711058803845336067123298983258010079178111678678796586176705130938139337603538683803154824502761228184209473344607055926120829751532887810487164482307564712692208157118923502010028250886290873995577102178526942152"
input = [int(i) for i in input]

input_len = len(input)


base_pattern = [0,1,0,-1]
phase_count = 100

def pattern_generator(pos):
    skip = True
    while True:
        for i in base_pattern:
            if(skip == True):
                skip = False
                if pos > 1:
                    yield (0, pos -1)
            else:
                yield (i,pos)


acc = input[:]
ret = [i for i in range(input_len)]

for phase in range(0, phase_count):
    for i in range(0,input_len):
        result = 0
        t = 0
        pattern = iter(pattern_generator(i+1))
        while t < input_len:
            (val, occ_num) = next(pattern)
            if val == 1:
                result += sum(acc[t:t+occ_num])
            elif val == -1:
                result -= sum(acc[t:t+occ_num])
            t+= occ_num
        ret[i] = abs(result) % 10
    acc = ret

print("finished")
print(acc[:8], sep='')