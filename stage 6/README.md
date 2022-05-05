<h1>Stage 6/7: Statistics</h1>
<h5>Description</h5>
<p>While studying, it may be very helpful to pay more attention to challenging parts where you make the most mistakes. In this stage, you will add some statistics features to your program so that the users can track their progress.</p>
<p>Implement the following additional actions:</p>
<ul>
    <li>save the application log to the given file:&nbsp;log</li>
    <li>print the term or terms that the user makes most mistakes with:&nbsp;hardest card</li>
    <li>erase the mistake count for all cards:&nbsp;reset stats</li>
</ul>
<p>Remember that now you need to store three items (term, definition, mistakes) instead of two (term, definition).</p>
<p>You may want to take a look at&nbsp;<a href="https://docs.python.org/3/library/io.html" rel="noopener noreferrer nofollow" target="_blank">io.StringIO<img src="http://localhost:63342/eduResources/icons/com/jetbrains/edu/learning/external_link_arrow@2x_dark.png" border="0" width="14" height="14"></a> objects: handling the log will be easier with them.</p>
<h5>Objectives</h5>
<p>Print the message&nbsp;Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):&nbsp;each time the user is prompted for their next action. The action is read from the next line, processed, and the message is output again until the user decides to exit the program.</p>
<p>The program&apos;s behavior depends on the user&apos;s input action:</p>
<ul>
    <li>log&nbsp;&mdash; ask the user where to save the log with the message&nbsp;File name:, save all the lines that have been input in/output to the console to the file, and print the message&nbsp;The log has been saved.&nbsp;Don&apos;t clear the log after saving it to the file.</li>
    <li>hardest card&nbsp;&mdash; print a string that contains the term of the card with the highest number of wrong answers, for example,&nbsp;The hardest card is &quot;term&quot;. You have N errors answering it. If there are several cards with the highest number of wrong answers, print all of the terms:&nbsp;The hardest cards are &quot;term_1&quot;, &quot;term_2&quot;. If there are no cards with errors in the user&apos;s answers, print the message&nbsp;There are no cards with errors.</li>
    <li>reset stats&nbsp;&mdash; set the count of mistakes to 0 for all the cards and output the message&nbsp;Card statistics have been reset.</li>
</ul>
<p>Update your&nbsp;import&nbsp;and&nbsp;export&nbsp;actions from the previous stage, so that the error count for each flashcard is also imported and exported.</p>
<h5>Example</h5>
<p>The symbol&nbsp;&gt;&nbsp;represents the user input. Note that it&apos;s not part of the input.</p>
<pre>Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
&gt; hardest card
There are no cards with errors.

Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
&gt; import
File name:
&gt; capitals.txt
28 cards have been loaded.

Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
&gt; hardest card
The hardest card is &quot;France&quot;. You have 10 errors answering it.

Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
&gt; ask
How many times to ask?
&gt; 1
Print the definition of &quot;Russia&quot;:
&gt; Paris
Wrong. The right answer is &quot;Moscow&quot;, but your definition is correct for &quot;France&quot; card.

Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
&gt; hardest card
The hardest cards are &quot;Russia&quot;, &quot;France&quot;. You have 10 errors answering them.

Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
&gt; reset stats
Card statistics have been reset.

Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
&gt; hardest card
There are no cards with errors.

Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
&gt; log
File name:
&gt; todayLog.txt
The log has been saved.

Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
&gt; exit
Bye bye!</pre>
<p><em>Note that all your outputs and user inputs should be on separate lines.</em></p>