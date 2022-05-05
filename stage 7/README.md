<h1>Stage 7/7: IMPORTant</h1>
<h5>Description</h5>
<p>Files are used to save progress and restore it the next time the user runs the program. It&apos;s tedious to print the actions manually. Sometimes you can just forget to do it! Let&apos;s add run arguments that define which file to read at the start and which file to save at the exit.</p>
<h5>Objectives</h5>
<p>When provided with command-line arguments, your program should do the following:</p>
<ul>
    <li>If&nbsp;--import_from=IMPORT&nbsp;is passed, where&nbsp;IMPORT&nbsp;is the file name, read the initial card set from the external file, and print the message&nbsp;n cards have been loaded.&nbsp;as the first line of the output, where&nbsp;n&nbsp;is the number of cards loaded from the external file. If such an argument is not provided, the set of cards should initially be empty and no message about card loading should be output.</li>
    <li>If&nbsp;--export_to=EXPORT&nbsp;is passed, where&nbsp;EXPORT&nbsp;is the file name, write all cards that are in the program memory into this file after the user has entered&nbsp;exit, and the last line of the output should be&nbsp;n cards have been saved., where&nbsp;n&nbsp;is the number of flashcards in the set.</li>
</ul>
<h5>Run arguments examples</h5>
<pre>python flashcards.py --import_from=derivatives.txt</pre>
<pre>python flashcards.py --export_to=animals.txt</pre>
<pre>python flashcards.py --import_from=words13june.txt --export_to=words14june.txt</pre>
<pre>python flashcards.py --export_to=vocab.txt --import_from=vocab.txt </pre>
<p><br></p>