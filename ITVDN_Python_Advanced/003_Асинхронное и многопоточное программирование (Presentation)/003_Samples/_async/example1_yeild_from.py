def concat_sequence_v1(s1, s2):
    """
    Скленивание двух последовательностей.
    """
    for elem in s1:
        yield elem
    for elem in s2:
        yield elem


def concat_sequence_v2(s1, s2):
    """
    Аналогично примеру concat_sequence_v1- склеиваем две последовательности,
    но уже с использованием yield from, что позволит нам не запускать цикла.
    """
    yield from s1
    yield from s2


seq1 = range(10)
seq2 = range(10, 20)
result = concat_sequence_v1(seq1, seq2)

print('Seq 1')
for i in result:
    print(i)

seq1 = range(10)
seq2 = range(10, 20)
result = concat_sequence_v2(seq1, seq2)

print('Seq 2')
for i in result:
    print(i)
