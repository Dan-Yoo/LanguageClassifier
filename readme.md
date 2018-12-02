### Language Classifier  
This project involved using a n-grams to classify 3 languages that shared the same alphabet.  
The chosen languages were English, French and Dutch.  
Each language was sanitized to not contain accents and such and these letters were replaced with their base character.  

## Requirements  
Have python version 3.7 installed

## How to train  
Put txt files into the language_text folder.  
Specify in `trainEN.txt`, `trainFR.txt` and `trainOT.txt` the directory of that specific training txts.  
run `python train.py`  
  
## How to classfy  
Put your sentences into the `input.txt` file  
run `python classify.py`  
The output files will be located n the `outputs` folder.