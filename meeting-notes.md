# Meeting Notes

## Meeting 1 (Jan 22)

### Housekeeping: your Python environment, workflow 
- Create your project folder where you will keep all study materials, python scripts, etc. 
   - Download the "Exercise Files" materials from PyET, unzip there
- Launching Jupyter Lab 
   - Open a terminal, move into your project folder (`cd` is the command, use `TAB` for auto-completion)
   - `jupyter lab` is the command
- Launching Python interpreter shell in your terminal
	- Windows: `python`, Mac: `python3`
	- Make sure to use UP and DOWN arrows to recycle Python commands
	- `control + c` to interrupt a command and return to the prompt (`>>> `)
	- `quit()` to get out 

### How to learn effectively 
- Use **Python shell** and **Jupyter Notebook (JNB)** together
    - Practice in Python shell, then use JNB to make study notes and reference materials for yourself
- Practice frequently: twice a week at the minimum
- Supplement with appropriate sections of Na-Rae's [Python 3 Notes](https://sites.pitt.edu/~naraehan/python3/). Scroll to the bottom for [Text samples](https://sites.pitt.edu/~naraehan/python3/text-samples.txt) link, which has text and code snippets handy for practicing
- Supplement with the [_Think Python_ book](https://allendowney.github.io/ThinkPython/index.html): has more problem sets, good for bringing the concepts together


### Course logistics
- GitHub: make an account (use your Pitt email)
- MS Teams: share questions, tips, etc.

### Next week
- PyET Ch.2 Quickstart goes through _all_ essential topics very quickly. Don't worry if you don't fully understand everything. 
- "Code challenge: Factorials" at the end. Give it your best shot.


## Meeting 2 (Jan 29)

### Review points
- New mode of running Python: executing a Python script file (e.g., `hello.py`) in a console (cmd or Terminal). Windows users should run `python hello.py` and Mac users should run `python3 hello.py`. 
- Python script vs. Python interactive shell vs. Jupyter Notebook. Differences?
- Printing vs. returning. What's the difference? 
- A `list` is mutable (= can be directly modified), but a `str` is immutable. Compare:
```python
>>> foo = 'hello'
>>> foo.upper()
'HELLO'                # returns a new string
>>> foo
'hello'                # foo has not changed
>>> mylist = [1,2,3,4,5]
>>> mylist.append(6)   # modifies mylist in memory, returns nothing
>>> mylist
[1, 2, 3, 4, 5, 6]     # mylist has changed
```  
- And, that is precisely why this code bit is wrong: `mylist = mylist.append(6)` while `foo = foo.upper()` is valid.  
- How can we insert an element into a list? Try `dir(list)` to display all list methods. Once you spotted a method that looks good, say 'insert',  look up the usage using `help(list.insert)`. 
- "Code challenge: Factorials", how was it?
    - CoderPad interface is not intuitive: it does not let you actually test out your code! Instead, use your JNB: create a function in a code cell, then test it out yourself with a few additional code cells below. Repeat the process as you refine your function. When it is in a good shape, paste it in your code into CoderPad to verify. Fingers crossed it passes all tests! If not, more testing in JNB. 
- Review the JNBs. Questions? Confusing spots?

### Next week
- PyET: Ch.3 "Basic Data Types" covers basic data types of numbers (`int`, `float`), boolean (`True`, `False`), and strings (`str`), and bytes. 
    - **Strings** are our bread-and-butter, and PyET's coverage is nowhere sufficient! Make sure to go deeper on strings by studying the supplementary materials, especially Na-Rae's Python 3 Notes.  
- "Code challenge: hex conversion" at the end. Don't forget to code outside of CoderPad! 


## Meeting 3 (Feb 5)

### Review points
- Strings mega review! 