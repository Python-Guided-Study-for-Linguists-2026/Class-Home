def vowelIndex(wd) :
    """Returns the index of the leftmost vowel. 
    If no vowel found in wd, returns len(wd).
    'desk'   --> 1
    'chair'  --> 2
    'egg'    --> 0
    """
    i = 0
    while i < len(wd) and wd[i] not in 'aeiou' :
        i += 1
    return i

def getInitialCs(wd) :
    """Takes a word, returns its word-initial consonant(s).
    'desk'   --> 'd'
    'chair'  --> 'ch'
    'egg'    --> ''
    """
    return wd[:vowelIndex(wd)] 

def getTheRest(wd) :
    """Takes a word, returns the word without any initial consonant.
    'desk'   --> 'esk'
    'chair'  --> 'air'
    'egg'    --> 'egg'
    """    
    # [1] Complete this function. Use vowelIndex().
    # YOUR CODE BELOW.
    return wd[vowelIndex(wd):]
     

def pigLatinWord(wd) :
    """Takes a word, and returns its Pig Latin translation.
    'desk'    -->   'eskday'
    'chair'   -->   'airchay'
    'school'  -->   'oolschay'
    'egg'     -->   'eggway'
    """
    # [2] Complete this function. Use getInitialCs() and getTheRest(). 
    # YOUR CODE BELOW.
    if getInitialCs(wd) == '':
        return wd + 'way'
    else:
        return getTheRest(wd) + getInitialCs(wd) + 'ay'
    
	
def pigLatinSent(sent) :
    """Takes a sentence, and returns its Pig Latin translation.
    Case and period in the input are properly handled in the output.
    'We love school.'       -->  'Eway ovelay oolschay.'
    'Linguistics is hard.'  -->  'Inguisticslay isway ardhay.'
    """
    # [3] Currently, the function returns the same string as sent. 
    # Modify it to return a translated sentence: using pigLatinWord(), 
    # translate each word before appending to tran.
    # Make sure the function handles case and period. 
    # MODIFY THE CODE BELOW. 
    tran = []
    for w in sent.replace('.', '').split():
        tran.append(pigLatinWord(w))
    return ' '.join(tran).capitalize()+'.'


########################################################################
# Main routine below. Do not edit this part. 
# Prompts for a sentence, and then prints out its Pig Latin translation.
print("Welcome to Pig Latin translator.")
sentence = input('Give me a sentence: ')
print("Your Pig Latin sentence is:")
print('"' + pigLatinSent(sentence) + '"')
        


