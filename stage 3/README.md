<h1>Stage 3/7: Make it your own</h1>
<h5>Description</h5>
<p>Your program can only entertain users with one card, which isn&rsquo;t really fun. Let&apos;s take our game to the next level and implement a set of flashcards.</p>
<p>Let the user decide how many cards they would like to make. First, ask the player to enter the desired number of cards. Then, ask them to input the term and the definition for every flashcard.</p>
<p>In the end, once all flashcards have been defined and saved, your program is finally ready to be used as a game! Question the player about all the new words they have entered. The program should give the term and ask for its definition.</p>
<h5>Objectives</h5>
<p>Your program should do the following:</p>
<ul>
    <li>Get the number of flashcards the user would like to create. To do that, print the line&nbsp;Input the number of cards:&nbsp;as a prompt for the user, and then read the number from the next line.</li>
    <li>Create the defined amount of cards in a loop. To create a flashcard, print the line&nbsp;<code>The term for card #<em>n</em>:</code> where&nbsp;<em>n</em> is the index number of the card to be created; then read the user&apos;s input (the term) from the following line. Then print the line&nbsp;<code>The definition for card #<em>n</em>:</code> and read the user&apos;s definition of the term from the next line. Repeat until all the flashcards are created.</li>
    <li>Test the user on their knowledge of the definitions of all terms in the order they were added.<strong>&nbsp;</strong>To do that with one flashcard, print the line&nbsp;<code>Print the definition of &quot;<em>term</em>&quot;:</code> where&nbsp;<code>&quot;<em>term</em>&quot;</code> is the term of the flashcard to be checked, and then read the user&apos;s answer from the following line. Make sure to put the term of the flashcard in quotes. Then print the line&nbsp;Correct!&nbsp;if the user&apos;s answer is correct, or the line&nbsp;<code>Wrong. The right answer is &quot;<em>definition</em>&quot;.</code> if the answer is incorrect, where&nbsp;<code>&quot;<em>definition</em>&quot;</code> is the correct definition. Repeat for all the flashcards in the set.</li>
</ul>
<h5>Example</h5>
<p>The symbol&nbsp;&gt;&nbsp;represents the user input. Note that it&apos;s not part of the input.</p>
<pre>Input the number of cards:
&gt; 2
The term for card #1:
&gt; print()
The definition for card #1:
&gt; outputs text
The term for card #2:
&gt; str()
The definition for card #2:
&gt; converts to a string
Print the definition of &quot;print()&quot;:
&gt; outputs text
Correct!
Print the definition of &quot;str()&quot;:
&gt; outputs text
Wrong. The right answer is &quot;converts to a string&quot;.</pre>
<p><em>Note that all your outputs and user inputs should be on separate lines.</em></p>