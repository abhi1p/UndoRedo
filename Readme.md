UndoRedo class contains following functions:-
1. `append()`  
    It will apend data into stack.
2.  `pop()`  
    It will pop data upto current index
3.  `undo()`  
    It decreases the current index
4.  `redo()`  
    It increases the current index
5.  `undoText()`  
    Returns data of (current index-1). It can be used before `undo()`.
6. `redoText()`  
    Returns data of (current index+1). It can be used before `redo()`.