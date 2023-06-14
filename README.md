<h1> Autofill Anki </h1>
 
<p>This is a code created for personal use with the objective of automatically
creating flashcards for Anki by using phrases and words gathered from PJO
which is a japanese online course. This code uses the Selenium package.</p>

<h3> What is Anki? </h3>
<p>Anki is a free open-source flashcard program that uses spaced repetition technique,
a much more efficient method for learning and remembering vocabulary than the traditional study means.</p>

<h3> What is PJO? </h3>
<p>PJO or "Programa Japonês Online" is a language course for japanese learning in which 
each lesson a series of new sentences and vocabulary is presented and explained in detail.</p>

<p>One of the PJO course's guidelines is to add each new phrase and vocabulary presented
in each lesson to Anki as a flashcard, which can be quite a hassle considering each flashcard
contains a front and a back, hence the creation of Autofill Anki.</p>

obs: "import minha_senha" refers to another .py file that contains my login information for both Anki and PJO plataforms.

<h3> About Flashcard and Deck creation </h3>
<p> Before starting adding cards to the Anki account it is necessary to create a Deck, in this case there were 3 Decks created:</p>

+ Escrita Japonesa: a deck focused on pronunciation and how to read kanjis
+ Frases em Japonês: a deck focused on understanding the meaning of sentences
+ testes: a deck created just for testing purposes

<p> As each lesson on PJO is either a kanji and word pronunciation focused lesson or a sentences focused lesson, the code below
allows the user to specify which Deck is going to get cards added: </p>

https://github.com/Hugo-Hattori/autofill_Anki_PJO/blob/ae1f68ff550fb8c018ca64909f93fc6174732762/autofill_Anki_PJO.py#L101-L111

<p> Each flashcard contains a front (word or sentence to learn) and a back (translation and how to read the word/sentence),
 each front and back is extracted from a Python list respectively named "lista_frentes" and "lista_tras". Both of those lists
 extract data from the PJO lesson website specified as "link_licao" by the user.
 The code below then adds each flashcard to the respective deck: </p>

https://github.com/Hugo-Hattori/autofill_Anki_PJO/blob/ae1f68ff550fb8c018ca64909f93fc6174732762/autofill_Anki_PJO.py#L120-L125
