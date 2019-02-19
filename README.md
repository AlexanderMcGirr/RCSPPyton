# rcsp-python
This implementation of the resource constrained shortest path algorithm allows each edge to have a different resource extension function. Whether the results are optimal cannot be detected by algorithm (may be implemented in the future). This algorithm may run slowly if each edge does have a different function due to functions being quite large objects.

# Todo
* Parallelize the domination step
* Use profiling to maybe consider using different data structures

# Profile
289 function calls in 0.001 seconds

Ordered by: standard name

| ncalls | tottime | percall | cumtime | percall | filename:lineno(function) |
| -------| ------- | ------- | ------- | ------- | ------------------------- |
| 1  |  0.000  |  0.000   | 0.001   | 0.001 | \<string\>:1(<module>) |
| 3   | 0.000  |  0.000 |   0.000 |   0.000 | RCSPTW.py:10(labelDomination) |
| 9 |   0.000  |  0.000  |  0.000 |   0.000 |RCSPTW.py:61(specREF) |
| 10 |    0.000  |  0.000 |   0.000 |   0.000| defaultclasses.py:10(__init__) |
| 2 |   0.000 |   0.000  |  0.000  |  0.000 |defaultclasses.py:22(__eq__) |
|10  |  0.000   | 0.000  |  0.000  |  0.000 |defaultclasses.py:27(__ne__)|
|5  |  0.000 |   0.000   | 0.000   | 0.000 |defaultclasses.py:34(__lt__)|
|8  |  0.000   | 0.000   | 0.000   | 0.000 |queue.py:121(put)|
|8   | 0.000  |  0.000  |  0.000   | 0.000 |queue.py:153(get)|
|1  |  0.000 |   0.000  |  0.000   | 0.000 |queue.py:226(_init)|
|17   | 0.000   | 0.000   | 0.000  |  0.000 |queue.py:229(_qsize)|
|8  |  0.000  |  0.000  |  0.000  |  0.000 |queue.py:232(_put)|
|8  |  0.000  |  0.000   | 0.000 |   0.000 |queue.py:235(_get)|
|1 |   0.000  |  0.000   | 0.000  |  0.000 |queue.py:33(__init__)|
|9    | 0.000  |  0.000  |  0.000  |  0.000 |queue.py:96(empty)|
|8  |  0.000 |   0.000  |  0.000 |   0.000 |rcsp.py:58(<listcomp>)|
|1   | 0.000   | 0.000  |  0.001  |  0.001 |rcsp.py:6(rcsp)|
|3   | 0.000 |   0.000  |  0.000  |  0.000 |threading.py:216(__init__)|
|16  |  0.000 |    0.000  |  0.000  |  0.000 |threading.py:240(__enter__)|
|16 |   0.000  |  0.000  |  0.000   | 0.000 |threading.py:243(__exit__)|
|16   | 0.000   | 0.000   | 0.000   | 0.000 |threading.py:255(_is_owned)|
|16   | 0.000  |  0.000  |  0.000  |  0.000 |threading.py:335(notify)|
|8   | 0.000  | 0.000  |  0.000  |  0.000 |{built-in method _heapq.heappop}|
|8   | 0.000  |  0.000  |  0.000  |  0.000 |{built-in method _heapq.heappush}|
|1   | 0.000   | 0.000   | 0.000  |  0.000 |{built-in method _thread.allocate_lock}|
|1   | 0.000   | 0.000  |  0.001  |  0.001 |{built-in method builtins.exec}|
|17   | 0.000   | 0.000  |  0.000   | 0.000 |{built-in method builtins.isinstance}|
|17   | 0.000  |  0.000   | 0.000  |  0.000 |{built-in method builtins.len}|
|1   | 0.000   | 0.000  |  0.000  |  0.000 |{built-in method builtins.print}|
|16  |  0.000 |   0.000  |  0.000  |  0.000 |{method '__enter__' of '_thread.lock' objects}|
|16  |  0.000   | 0.000 |   0.000 |   0.000 |{method '__exit__' of '_thread.lock' objects}|
|16  |  0.000 |   0.000 |   0.000  |  0.000 |{method 'acquire' of '_thread.lock' objects}|
|7   | 0.000  |  0.000  |  0.000  |  0.000 |{method 'append' of 'list' objects}|
|1   | 0.000  |  0.000  |  0.000  |  0.000 |{method 'disable' of '_lsprof.Profiler' objects}|
|1   | 0.000  |  0.000  |  0.000  |  0.000 |{method 'format' of 'str' objects}|
|3   | 0.000  |  0.000  |  0.000  |  0.000 |{method 'remove' of 'list' objects}|


This is just a reference for the where the algorithm makes most calls in a simple example.