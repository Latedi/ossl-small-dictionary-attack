# ossl-small-dictionary-attack
Decrypt files using ossl using all available algorithms. You can then use the isplaintext.py script to sort through the files and find the one most likely to actually be decrypted (there are many false positives). I would not recommend larger word lists.

First change the passwords in decrypt.py and change the filename of the encrypted file. Then create a directory named out and run the script. Afterwards you can run the isplaintext.py to find the most likely candidate out of the files (many created with false positives by open ssl). The results will be displayed like
<filename>  <number of readable characters> <number of undreadable characters>
<filename>  <number of readable characters> <number of undreadable characters>
...
<number of files>
