# Дополните приведенный код, так чтобы получить список,
# содержащий только непустые кортежи исходного списка tuples, не меняя порядка их следования.


tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
non_empty_tuples = [i for i in tuples if i != ()]

print(non_empty_tuples)

