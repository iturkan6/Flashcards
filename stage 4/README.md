<h1>Stage 4/7: A good stack</h1>
<h5>Description</h5>
<p>While learning new things, we may mix things up and use the right definition for the wrong term. Let&apos;s inform our players if they enter the definition that is wrong for the requested flashcard but correct for another flashcard in our set.</p>
<p>Also, it might be very confusing if our flashcard set contains cards with the same term or definition, since seeing only one side of the card we can&apos;t tell them apart. Let&apos;s add a constraint: the user must add only unique terms and definitions. To do this, you need to find a way to check whether the set contains a particular term or definition and get the term by the definition, and vice versa.</p>
<p>These two features will definitely improve our game!</p>
<h5>Objectives</h5>
<p>Modify your program and add the following functionalities:</p>
<ul>
    <li>When the user tries to add a duplicate term, forbid it and output the message&nbsp;<code>The term&nbsp;<em>&quot;term&quot;</em> already exists. Try again:</code> using the term instead of&nbsp;<em>&quot;term&quot;</em>. Ask for the term until the user inputs a unique term.</li>
    <li>When the user tries to add a duplicate definition, forbid it and Output the message&nbsp;<code>The definition&nbsp;<em>&quot;definition&quot;</em> already exists. Try again:</code> with the definition instead of&nbsp;<em>&quot;definition&quot;</em>. Ask the player to input the definition until the user inputs a unique one.</li>
    <li>When the user enters the wrong definition for the requested term, but this definition is correct for another term, print the appropriate message:&nbsp;<code>Wrong. The right answer is&nbsp;<em>&quot;correct answer&quot;</em>, but your definition is correct for&nbsp;<em>&quot;term for user&apos;s answer&quot;</em>.</code> , where&nbsp;<em>&quot;correct answer&quot;</em> is the actual definition for the requested term, and&nbsp;<em>&quot;term for user&apos;s answer&quot;</em> is the appropriate term for the user-entered definition.</li>
</ul>
<h5>Examples</h5>
<p>The symbol&nbsp;&gt;&nbsp;represents the user input. Note that it&apos;s not part of the input.</p>
<p><strong>Example 1:&nbsp;</strong><em>the user tries to add duplicated term and definition</em></p>
<pre>Input the number of cards:
&gt; 2
The term for card #1:
&gt; print()
The definition for card #1:
&gt; outputs text
The term for card #2:
&gt; print()
The term &quot;print()&quot; already exists. Try again:
&gt; str()
The definition for card #2:
&gt; outputs text
The definition &quot;outputs text&quot; already exists. Try again:
&gt; converts to a string
Print the definition of &quot;print()&quot;:
&gt; outputs text
Correct!
Print the definition of &quot;str()&quot;:
&gt; converts to a string
Correct!</pre>
<p><strong>Example 2:&nbsp;</strong><em>the user gives a correct definition for a term that exists, but which is not the term that the program is asking about</em></p>
<pre>Input the number of cards:
&gt; 2
The term for card #1:
&gt; uncle
The definition for card #1:
&gt; a brother of one&apos;s parent
The term for card #2:
&gt; ankle
The definition for card #2:
&gt; a part of the body where the foot and the leg meet
Print the definition of &quot;uncle&quot;:
&gt; a part of the body where the foot and the leg meet
Wrong. The right answer is &quot;a brother of one&apos;s parent&quot;, but your definition is correct for &quot;ankle&quot;.
Print the definition of &quot;ankle&quot;:
&gt; ???
Wrong. The right answer is &quot;a part of the body where the foot and the leg meet&quot;.</pre>
<p><em>Note that all your outputs and user inputs should be on separate lines.</em></p>