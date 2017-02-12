# botlikeme
Creating an AI bot trained from my facebook messages.

1. Ask facebook for all my records, this includes all my messages. Facebook would email me a link to download this info after a few days.

2. Created a python file that extracts the messages.htm into just the messages as a text file, without all the tags and with a newline to separate the messages. This condensed the 20MB file I had into a 3.7MB file(not included due to privacy reasons). This took a couple minutes. 

3. Go to ```~/Library/Messages/Archive``` and run ```plutil -convert xml1 filename.ichat``` because I want to use my iMessages too. [Not completed]

4. Construct dictionary of words. For every sentence, add a [START] and [END] tag, then for each consecutive pair of words, note the frequency of the later word appearing if the previous word was written. 

5. Spit out random words with a seed.

TODOs:
1. Get a distribution of lengths of sentences and use that to influence the length of generated sentences.
