<h1>Stage 5/7: Menu, please</h1>
<h5>Description</h5>
<p>Our users cannot create new flashcards all the time. It seems like a good idea to keep old but useful cards in storage so we can use them later. Let&apos;s try to do that!</p>
<p>In this stage, you will improve the application&apos;s interactivity by having it ask the user for action and perform it. You will also provide additional functionality, allowing the user to store flashcards in files for future use.</p>
<p>The program should support the following actions:</p>
<ul>
    <li>add a card:&nbsp;add</li>
    <li>remove a card:&nbsp;remove</li>
    <li>load cards from file:&nbsp;import</li>
    <li>save cards to file:&nbsp;export</li>
    <li>ask for definitions of some random cards:&nbsp;ask</li>
    <li>exit the program:&nbsp;exit</li>
</ul>
<p>You can store cards in a file in any format; tests do not check the content of the file, but they do check that the saved flashcards are loaded correctly.</p>
<p>When you load flashcards from a file, you shouldn&apos;t erase the cards that aren&apos;t in the file. If the imported flashcard already exists, update its definition in the program memory. There won&apos;t be any conflict with definitions in the tests.</p>
<h5>Objectives</h5>
<p>Print the message&nbsp;Input the action (add, remove, import, export, ask, exit):&nbsp;each time the user is prompted for their next action. The action is read from the next line, processed, and the message is output again until the user decides to exit the program.</p>
<p>The program&apos;s behavior depends on the action the user inputs:</p>
<ul>
    <li>add&nbsp;&mdash; create a new flashcard with a unique term and definition. After adding the card, output the message&nbsp;The pair (&quot;term&quot;:&quot;definition&quot;) has been added, where&nbsp;&quot;term&quot;&nbsp;is the term entered by the user and&nbsp;&quot;definition&quot;&nbsp;is the definition entered by the user. If a term or a definition already exists, output the line&nbsp;The &lt;term/definition&gt; already exists. Try again:&nbsp;and accept a new term or definition.</li>
    <li>remove&nbsp;&mdash; ask the user for the term of the card they want to remove with the message&nbsp;Which card?, and read the user&apos;s input from the next line. If a matching flashcard exists, remove it from the set and output the message&nbsp;The card has been removed.. If there is no such flashcard in the set, output the message&nbsp;<code>Can&apos;t remove &quot;<em>card</em>&quot;: there is no such card.</code>, where&nbsp;<code>&quot;<em>card</em>&quot;</code> is the user&apos;s input.</li>
    <li>import&nbsp;&mdash; print the line&nbsp;File name:, read the user&apos;s input from the next line, which is the file name, and import all the flashcards written to this file. If there is no file with such name, print the message&nbsp;File not found.. After importing the cards, print the message&nbsp;n cards have been loaded., where&nbsp;n&nbsp;is the number of cards in the file. The imported cards should be added to the ones that already exist in the memory of the program. However, the imported cards have priority: if you import a card with the name that already exists in the memory, the card from the file should overwrite the one in memory.</li>
    <li>export&nbsp;&mdash; request the file name with the line&nbsp;File name:&nbsp;and write all currently available flashcards into this file. Print the message&nbsp;n cards have been saved., where&nbsp;n&nbsp;is the number of cards exported to the file.</li>
    <li>ask&nbsp;&mdash; ask the user about the number of cards they want and then prompt them for definitions, like in the previous stage.</li>
    <li>exit&nbsp;&mdash; print&nbsp;Bye bye!&nbsp;and finish the program.</li>
</ul>
<h5>Examples</h5>
<p>The symbol&nbsp;&gt;&nbsp;represents the user input. Note that it&apos;s not part of the input.</p>
<p><strong>Example 1:&nbsp;</strong><em>the user removes an existing card and tries to remove a non-existent one.</em></p>
<pre>Input the action (add, remove, import, export, ask, exit):
&gt; add
The card:
&gt; France
The definition of the card:
&gt; Paris
The pair (&quot;France&quot;:&quot;Paris&quot;) has been added.

Input the action (add, remove, import, export, ask, exit):
&gt; add
The card:
&gt; France
The card &quot;France&quot; already exists. Try again:
&gt; Great Britain
The definition of the card:
&gt; Paris
The definition &quot;Paris&quot; already exists. Try again:
&gt; London
The pair (&quot;Great Britain&quot;:&quot;London&quot;) has been added.

Input the action (add, remove, import, export, ask, exit):
&gt; remove
Which card?
&gt; France
The card has been removed.

Input the action (add, remove, import, export, ask, exit):
&gt; remove
Which card?
&gt; Wakanda
Can&apos;t remove &quot;Wakanda&quot;: there is no such card.

Input the action (add, remove, import, export, ask, exit):
&gt; exit
Bye bye!</pre>
<p><strong>Example 2:&nbsp;</strong><em>the user uses files to import and export their flashcards; definitions of existing cards are updated after import</em></p>
<pre>Input the action (add, remove, import, export, ask, exit):
&gt; import
File name:
&gt; ghost_file.txt
File not found.

Input the action (add, remove, import, export, ask, exit):
&gt; add
The card:
&gt; Japan
The definition of the card:
&gt; Tokyo
The pair (&quot;Japan&quot;:&quot;Tokyo&quot;) has been added.

Input the action (add, remove, import, export, ask, exit):
&gt; add
The card:
&gt; Russia
The definition of the card:
&gt; UpdateMeFromFile
The pair (&quot;Russia&quot;:&quot;UpdateMeFromFile&quot;) has been added.

Input the action (add, remove, import, export, ask, exit):
&gt; import
File name:
&gt; capitals.txt
28 cards have been loaded.

Input the action (add, remove, import, export, ask, exit):
&gt; ask
How many times to ask?
&gt; 1
Print the definition of &quot;Russia&quot;:
&gt; Moscow
Correct!

Input the action (add, remove, import, export, ask, exit):
&gt; export
File name:
&gt; capitalsNew.txt
29 cards have been saved.

Input the action (add, remove, import, export, ask, exit):
&gt; exit
Bye bye!</pre>
<p><strong>Example 3:&nbsp;</strong><em>the program asks for definitions several times</em></p>
<pre>Input the action (add, remove, import, export, ask, exit):
&gt; add
The card
&gt; a brother of one&apos;s parent
The definition of the card
&gt; uncle
The pair (&quot;a brother of one&apos;s parent&quot;:&quot;uncle&quot;) has been added.

Input the action (add, remove, import, export, ask, exit):
&gt; add
The card
&gt; a part of the body where the foot and the leg meet
The definition of the card
&gt; ankle
The pair (&quot;a part of the body where the foot and the leg meet&quot;:&quot;ankle&quot;) has been added.

Input the action (add, remove, import, export, ask, exit):
&gt; ask
How many times to ask?
&gt; 6
Print the definition of &quot;a brother of one&apos;s parent&quot;:
&gt; ankle
Wrong. The right answer is &quot;uncle&quot;, but your definition is correct for &quot;a part of the body where the foot and the leg meet&quot;.
Print the definition of &quot;a part of the body where the foot and the leg meet&quot;:
&gt; ??
Wrong. The right answer is &quot;ankle&quot;.
Print the definition of &quot;a brother of one&apos;s parent&quot;:
&gt; uncle
Correct!
Print the definition of &quot;a part of the body where the foot and the leg meet&quot;:
&gt; ankle
Correct!
Print the definition of &quot;a brother of one&apos;s parent&quot;:
&gt; ??
Wrong. The right answer is &quot;uncle&quot;.
Print the definition of &quot;a part of the body where the foot and the leg meet&quot;:
&gt; uncle
Wrong. The right answer is &quot;ankle&quot;, but your definition is correct for &quot;a brother of one&apos;s parent&quot;.

Input the action (add, remove, import, export, ask, exit):
&gt; exit
Bye bye!</pre>
<p><em>Note that all your outputs and user inputs should be on separate lines.</em></p>