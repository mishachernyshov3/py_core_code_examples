# Знайти найбільш вживане слово у тексті.
import re
from collections import Counter


text = '''
Sometimes    you need to count the objects in a given data source to know how often they occur. In other words, you need 
to determine their frequency. For example, you might want to know how often a specific item appears in a list or 
sequence of values. When your list is short, counting the items can be straightforward and quick. However, when you 
have a long list, counting things can be more challenging. To count objects, you typically use a counter, which is an 
integer variable with an initial value of zero. Then you increment the counter to reflect the number of times a given 
object appears in the input data source. When you’re counting the occurrences of a single object, you can use a single 
counter. However, when you need to count several different objects, you have to create as many counters as unique 
objects you have. To count several different objects at once, you can use a Python dictionary. The dictionary keys will 
store the objects you want to count. The dictionary values will hold the number of repetitions of a given object, or the 
object’s count. For example, to count the objects in a sequence using a dictionary, you can loop over the sequence, 
check if the current object isn’t in the dictionary to initialize the counter (key-value pair), and then increment its 
count accordingly.
'''

sanitized_text = re.sub(r'[^a-zA-Z ]', '', text.lower().strip())
text_words = re.split(r' +', sanitized_text)
text_words_counter = Counter(text_words)
most_common_word = text_words_counter.most_common(1)[0][0]
print(f'Most common word is "{most_common_word}".')
