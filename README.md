# FreeRetrival
Simple app for free retrival scheduling. Free retrival is a studying technique where
you take a topic and write down everything you can remember on a blank piece of paper.
This little tool is formalises this process a little bit by:
- storing an answer sheet for evaluating the retirval
- recording the each retrival (date + scoring)
- scheduling when to do the topic next. (spaced repetition) 

# To start:
1. $source init_table.sh
2. $pip install -r requirements.txt
3. $python src/main.py  

# To add cards 
A card is the answer sheet for a topic. To add a new one, drop it's pdf into data/to_add/ and then run the main python file, following the prompts. 