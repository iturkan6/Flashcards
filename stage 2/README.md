<h1>Stage 2/7: What&apos;s on the card</h1>
<h5>Description</h5>
<p>Of course, we cannot use flashcards with only one hardcoded card. So let&apos;s make our program more dynamic! Let&rsquo;s create flashcards depending on the user&apos;s input and add a primitive guessing mechanism so that the user can check how well they remember the definitions.</p>
<p>In this stage, you need to implement a custom flashcard-creation mechanism which will be extensively used in further steps, and add a mechanism to check the user&apos;s answer.</p>
<h5>Objectives</h5>
<p>Your program should read two lines from the console, a&nbsp;<em>term,</em> and a&nbsp;<em>definition,&nbsp;</em>that represent a card.</p>
<p>After that, the user inputs a line as an&nbsp;<em>answer</em> (a definition of the term on the card). Compare the user&apos;s answer with the correct definition and print the result.</p>
<p>The output of the program must contain one of two words:</p>
<ul>
    <li>wrong&nbsp;if the answer doesn&apos;t match the definition;</li>
    <li>right&nbsp;if the answer matches the definition.</li>
</ul>
<p>Of course, at this point, the user is unlikely to get the answer wrong, since they&rsquo;re the ones who just typed in the answer... But don&rsquo;t worry: right now we&apos;re just warming up so that in later stages we could make this a bit more challenging for our users.</p>
<h5>Examples</h5>
<p>The greater-than symbol followed by a space (&gt;&nbsp;) represents the user input. Note that it&apos;s not part of the input.</p>
<p><strong>Example 1:&nbsp;</strong><em>the user&apos;s answer is correct</em></p>
<p>Input (a term, a definition, an answer):</p>
<pre>&gt; print()
&gt; outputs text
&gt; outputs text</pre>
<p>Output:</p>
<pre>Your answer is right!</pre>
<p><strong>Example 2:&nbsp;</strong><em>the user&apos;s answer is incorrect</em></p>
<p>Input (a term, a definition, an answer):</p>
<pre>&gt; Jetbrains
&gt; A place for people who love to code
&gt; A place for people who hate to code</pre>
<p>Output:</p>
<pre>Your answer is wrong...</pre>
<p><br></p>