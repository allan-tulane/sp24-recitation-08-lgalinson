# CMPS 2200 Recitation 08

## Answers

**Name:**Lakeland Galinson
**Name:**_________________________


Place all written answers from `recitation-08.md` here for easier grading.



- **1b)**

work is $O(V+E\log(V))$

span is $O(V\log(V))$



- **2b)**

```python

 path = []
  
    while parents[destination] is not None:
        path.append(parents[destination])
        destination = parents[destination]
    
    return ''.join(path[::-1])

```

