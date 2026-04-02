# Meeting Notes

# Meeting 1 (Jan 22)

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


# Meeting 2 (Jan 29)

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


# Meeting 3 (Feb 5)

### Review points
- Strings mega review!
    - String methods, testing, transformation, indexing, slicing
	- Special characters, escaping
	- Splitting and joining strings
	- String formatting with f-strings:`f"...{ }"`
- "Overloaded" operators: `in`, `+`, `*`
- Practice: Pig Latin generator
    - https://sites.pitt.edu/~naraehan/ling1330/ex2.html
	- First, build the following helper functions: 
	```python
	>>> vowelIndex('chair')
	2
	>>> getInitialCs('chair')    # should call vowelIndex()
	'ch'
	>>> getTheRest('chair')      # should call vowelIndex()
	'air'
    ```

    - Then, build `pigLatinWord()` that converts a word to its pig Latin counterpart:

	```python
	>>> pigLatinWord('chair')
	'airchay'
	>>> pigLatinWord('egg')
	'eggway'
	```

### Next week
- PyET: Ch.4 "Basic Data Structures" covers important data objects with internal structures: lists, tuples, sets, and dictionaries. 
   - That rounds up all essential building blocks of Python's built-in data types. Make sure to _apply_! Try building interesting and complex data structures with language examples. 
   - Also: practice how to _transform_ one data format to another: build a list of characters from a string, a set from a list, a list from a dictionary, a list of (key, value) tuples from a dictionary, etc. 
   - **list comprehension** is an essential python skill. Practice this! Na-Rae's Python 3 Notes has fun examples. 
   - "Code challenge: Encoding ASCII art" should be pretty straightforward.
- Additional practice: Finish up the Pig Latin generator code: `pigLatinSent()` should handle a full sentence input such as 'Linguistics is hard.' to output 'Inguisticslay isway ardhay.'.


# Meeting 4 (Feb 12)

### Review points
- Na-Rae's Python shell session from today: [2026-02-12-python-shell.html.pdf](2026-02-12-python-shell.html.pdf)
- Data structures mega review! 
   - Converting between data structures
- List comprehension is a super power! Practice until you can list-comprehend in your sleep 
- Sorting lists, dictionaries, and tuples
- Practice: Pig Latin script wrap. Key script here: [pig_latin.KEY.py](pig_latin.KEY.py)
- Let's share code! Please share your Python notes and Jupyter notebooks in the "Sandbox" repository. 

### Next week
- PyET: Ch.5 "Control Flow" is a small module: it should be quick to finish, giving you lots of free time. 
- Which means... **HOMEWORK time**! Please work on this "Past tense generator" problem before our next meeting. https://sites.pitt.edu/~naraehan/ling1901/HW2.pdf
   - You will need to use the `input()` function. If you're not familiar, it prompts the user to type in something. Below, the user input is assigned to the variable `verbs`:
	```
	verbs = input("What are your verbs? (Type EXIT to quit): ")
	```
   - You can compose a python script (`.py`) or a Jupyter Notebook (`.ipynb`). When done, rename your file with your name (say, `verbs_valeria.py`) and upload it to the `hw_verbs` folder of our Sandbox GitHub repository. 
- What about the "Finding Prime Number Faster" challenge? This one is... "meh". Give it a try if you want. 


# Meeting 5 (Feb 19)

### Review points
- Review: "Verbs" homework


### Next week
- PyET: Ch.6 "Functions" is another short one, although packed with high-level concepts. The examples Ryan uses are _very_ abstract -- try coming up your own, more "fun and memorable" example functions! 
    - The "Functions and Variables" vid showcases a useful routine: text processing. Also, it shows the lambda function, which is important. Make sure to spend time with these. 
- Code challenge "Sum of triangles" is more of a brain teaser. Give it a try. 
- **Homework** problems below. I recommend starting out in Python shell and composing a Jupyter Notebook. Upload your JNB file in the `hw_palin_lambda` folder of our Sandbox repo.  
    1. Build a function called `getRev()`, which reverses a string and returns it. It should work as follows:
	```python
	>>> getRev('platypus')
    'supytalp'
    >>> getRev('tenet')
    'tenet'
	```
	2. Build a function called `isPalindrome()`, which returns True/False on palindromehood. It should work as follows:
	```python
	>>> isPalindrome('hello')
    False
    >>> isPalindrome('noon')
    True
	```
	3. Build a function `remPunct()` that removes all punctuation in a given string. It should work as follows:
	```python
	>>> remPunct("Hello, world!")
    'Hello world'
    >>> remPunct("Mr.")
    'Mr'
	```
	4. Build a function `findPalindromes()` that returns a list of all word tokens in a given text that's a palindrome.  
    ```python
	>>> footxt = "I'm meeting a platypus at noon!"
    >>> findPalindromes(footxt)
    ['a', 'noon']
	```
	5. Now for something different! From the various "US states" data objects found on my "text samples" page, build the following object called `states_data`, which is a list of 4-element tuples: `(state, STATE-CODE, capital, population)`. You will want to use list comprehension.
	```python
	>>> states_data[:3]
    [('Alabama', 'AL', 'Montgomery', 4833722), ('Alaska', 'AK', 'Juneau', 735132),
    ('Arizona', 'AZ', 'Phoenix', 6626624)]
	```
	6. Recall that `sorted()` takes a list and returns a sorted list. You can optionally specify a function to use for sorting, like the `len()` function below.
	```python
    >>> mylist = ['eel', 'monkey', 'ant', 'beekeeper']
    >>> sorted(mylist)
    ['ant', 'beekeeper', 'eel', 'monkey']
    >>> sorted(mylist, key=len)
    ['eel', 'ant', 'monkey', 'beekeeper']
    >>> sorted(mylist, key=len, reverse=True)
    ['beekeeper', 'monkey', 'eel', 'ant']

	```
	The `key=` option can take any function, lambda functions included! Compose a sorting syntax with a **lambda function** that sorts a list of words by the number of 'e' in them, from largest to smallest:
	```python
	>>> sorted(mylist, key=...??..., reverse=True)
    ['beekeeper', 'eel', 'monkey', 'ant']
	```
	7. One last problem! Sort the `states_data` by population, again using a lambda function:
	```python
	>>> sorted(states_data, key=...??..., reverse=True)[:5]
    [('California', 'CA', 'Sacramento', 38332521), ('Texas', 'TX', 'Austin', 26448193), 
	('New York', 'NY', 'Albany', 19651127), ('Florida', 'FL', 'Tallahassee', 19552860), 
	('Illinois', 'IL', 'Springfield', 12882135)]
	```
	


# Meeting 6 (Feb 26)

### Review points
- Review: "Palindromes and lambda functions" homework
- Introducing the [NLTK library](https://www.nltk.org/): install and download NLTK data pack
   - In terminal: `pip3 install nltk`
   - In Python: 
   ```python
   import nltk
   nltk.download("book")
   ```
   - Mac folks: if `nltk.download()` does not work, you haven't done the step of installing certificates while installing Python. Complete it following the [instructions here](https://docs.python.org/3/using/mac.html). 
   - Word tokenization with nltk: 
   ```python
   >>> foostr = "You haven't seen Star Wars yet...?"
   >>> nltk.word_tokenize(foostr)
   ['You', 'have', "n't", 'seen', 'Star', 'Wars', 'yet', '...', '?']
    ```
	- Sentence tokenization with nltk:
	```python
	>>> foostr2 = "Hello, earthlings! I come in peace. Take me to your leader."
	>>> nltk.sent_tokenize(foostr2)
	['Hello, earthlings!', 'I come in peace.', 'Take me to your leader.']

	```

### Next week
- PyET: Ch.10 "Working with Files"
   - File IO is surprisingly tricky. Don't put this one off -- start early so you can come to my office hours for help. 
   - You can skip the "JSON" module. Unless you already know what JSON is, it's too early to be useful to you. 
   - Ryan doesn't make it explicit, but all files to be read-in and written-out should be in the same folder as your Python script. 
   - Important! Ryan only demonstrates reading in individual _lines_, but the method we linguists use more often is `f.read()`, which reads in the entire content of a file as a single string. Make sure to learn this: details in A11 [File Reading & Writing Methods](https://sites.pitt.edu/~naraehan/python3/reading_writing_methods.html).  
- Code challenge "Compressing ASCII art" --> you should skip. Instead, practice on your own! 
- **Homework** problems below. They are suggestions meant to help you practice. You are encouraged to explore and do your own thing! Share your work (script or Jupyter Notebook) in the `hw_fileio` folder of our Sandbox repo.
   - Practice writing a CSV file. Here's a [reference screenshot](screenshot_states_data.png), which contains various data points about US states. The content should look familiar -- it's all in the `states_data` object! Start with this object, and then create the CSV file on your laptop through file writing. 
        - After that, read in your CSV file and do something interesting with it. 
   - From Peter Norvig's [Beautiful Data](https://norvig.com/ngrams/) site, download `enable1.txt`, which contains a list of English words. Read in the file and process it as a list object called `words`. Then, explore it and make interesting discoveries. Suggestions: Are 'syntax' and 'syntactician' in the list? How many words without 'aeiouy'? How many palindromes are there? What is the longest word? What's the word with the largest number of 'e'? How to cheat on [this WORDLE problem](Wordle-problem.png)? 
   - You now have the power of processing text files! Good sample text files are `tale.txt`, `gettysburg_address.txt` and `gift-of-magi.txt`, all linked at the bottom left of my [Python 3 Notes](https://sites.pitt.edu/~naraehan/python3/). Try doing some text processing with NLTK. 


# Meeting 7 (Mar 5)

### Review points
- File IO and CWD. What about files _elsewhere_ on your laptop, like on your Desktop? You need to know about file path and CWD ("current working directory"). Details in my Python 3 Notes: 
   - A10 [File Path and CWD](https://sites.pitt.edu/~naraehan/python3/file_path_cwd.html)
   - A11 [File Reading & Writing Methods](https://sites.pitt.edu/~naraehan/python3/reading_writing_methods.html). 
- HW review
   - Your code returns an output, say a number. But... is it correct? Don't assume it is, _validate_. Knowing how to validate is the important last piece in your Python skillset. Make a habit out of validating! 
   - Na-Rae's Python shell session from today: [2026-03-05-python-shell.html.pdf](2026-03-05-python-shell.html.pdf)


### Next meeting (after spring break)
- Review of my [Python 3 Notes](https://sites.pitt.edu/~naraehan/python3/). With the exception of "Regular Expressions" and "pickling", all notes/topics should be familiar to you now! Review and patch any gaps in knowledge. 
- **Homework**: Just focus on catching up and further practicing, and upload your work in the `hw_review` folder. Suggestions:
   - Revisit materials from last few meetings. Take a look at HW submissions submitted by classmates, discover different/better ways of solving a problem. 
   - Catch up! Review missed topics, practice text processing with NLTK. 
   - Review my Python 3 Notes. 



# Meeting 8 (Mar 19)

### Review points
- Your review notes
    - What has everyone been up to? 
- Go over Na-Rae's [Python 3 Notes](https://sites.pitt.edu/~naraehan/python3/)
    - New topic: **regular expressions** and Python's `re` library https://sites.pitt.edu/~naraehan/python3/re.html
- Na-Rae's Python shell session from today: [2026-03-19-python-shell.html.pdf](2026-03-19-python-shell.html.pdf)

### Next meeting
- [Corpus Linguistics Workshop](https://github.com/naraehan/NASSLLI2018-Corpus-Linguistics/?tab=readme-ov-file) Day 1, 2
- **Homework**: Follow the contents of Day 1 and Day 2 notebooks in your own Jupyter Notebook file. You can combine the two into a single JNB. Upload your JNB in the `hw_workshop_day12` folder. 
    - You should be familiar with most of the concepts by now! 
    - There are some new, important data objects such as `nltk.FreqDist()`: pay special attention. 
    - IMPORTANT: Don't just copy over the commands and nod along! That doesn't help you learn. Make sure to _explore_ by altering them and trying your own thing. 
    
    
# Meeting 9 (Mar 26)

### Review points
- How was Workshop Day 1 and Day 2? What else did you try?
- Go over the two JNBs, with special focus on Day 2
    - Output cells with too many lines? `%pprint` is your friend, it turns on and off the "1 item per line" behavior. 
    - Na-Rae's Jupyter Notebook: [day2.ipynb](day2.ipynb)

### Next meeting
- [Corpus Linguistics Workshop](https://github.com/naraehan/NASSLLI2018-Corpus-Linguistics/?tab=readme-ov-file) Day 3, 4
- **Homework**: Like before, follow the contents of Day 3 and Day 4 notebooks in your own Jupyter Notebook file. You can combine the two into a single JNB. Upload your JNB in the `hw_workshop_day34` folder. 
   - Day 3 introduces you to NLTK's `PlaintextCorpusReader` method for reading in a corpus in one go. 
       - "2005-Bush.txt" used to have an encoding error, which can be tricky to handle. If the error is still present in the latest corpus data, you should fix it by following the directions. If you get stuck, come to my office hours. 
       - Is `the` getting more or less frequent through the history of American English? There's a link to a solution at the bottom of Day 3. You don't have to try it yourself, but do take a peak. 
   - Day 4 introduces a couple of technical concepts: **n-grams** and **conditional frequency distribution**. Don't worry if you find them confusing: we'll review them in class. 
   - Again, don't just copy over the commands and nod along! That doesn't help you learn. Make sure to _explore_ by altering them and trying your own thing. You'll be surprised to find that you already have lots of tools at your disposal that can help satisfy your curiosity. 
   
   
# Meeting 10 (Apr 2)

### Review points
- [Corpus Linguistics Workshop](https://github.com/naraehan/NASSLLI2018-Corpus-Linguistics/?tab=readme-ov-file) Day 3, 4
- Na-Rae's JNBs: [day3.ipynb](day3.ipynb), [day4.ipynb](day4.ipynb)
- NLTK's `PlaintextCorpusReader` method for corpus loading
   - Various units: raw text, word tokens, sentence tokens
- **n-grams** and **conditional frequency distribution**
   - Using conditional frequency distribution to get likelihood of w2 following w1, and vice versa
- Basic textual statistics:
   - Text lengths
   - Average sentence lengths
   - Average word lengths


### Next meeting
- We're moving on to our final project: **BU vs. JA EFL Writing** 
    - Between Bulgarian and Japanese college students, which group writes English on a more advanced level? Let's explore the question with real data: 60 English essays written by Japanese and Bulgarian students, excerpted from the [ICLE2 (International Corpus of Learner English v2) corpus](https://uclouvain.be/en/research-institutes/ilc/cecl/iclev2.html).
    - Data: [ICLE2_bu_ja.zip](https://github.com/Python-Guided-Study-for-Linguists-2026/Sandbox/ICLE2_bu_ja.zip)
- **Homework**: Explore the ICLE2 Bu-Ja corpus dataset and get a sense of its makeup. Upload your JupyterNotebook to the `hw_buja` folder.
   - Using NLTK's `PlaintextCorpusReader`, load the data as two corpora: one for the Bulgarian L1 group, the other for the Japanese L1 group. Adapt from this code:
   ``` 
    # Set your corpus root: 
    corpus_root = "./ICLE2_bu_ja"
    
    # Read in the two corpora:
    bucor = PlaintextCorpusReader(corpus_root, 'BG.*txt')
    jacor = PlaintextCorpusReader(corpus_root, 'JP.*txt') ```
   - Now, explore the two corpora to get a sense of them. I am intentionally being vague here, not listing the metrics you need to find. You should understand what they are! 
   - That's it. You may be motivated to dive even deeper and produce more advanced metrics (such as average sentence lengths, average word lengths, bigrams comparison, etc.), but don't do them all here, leave most for later. The urge to jump right in to compute "all the statistics" is not only unnecessary but may even be ill-advised at this stage. What's important: _taking your time to get to know the underlying realities of your text data_ by getting up-close with them. 
 
  
 