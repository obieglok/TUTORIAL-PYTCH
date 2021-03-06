# Piano Keys Game 

In this tutorial we will make our very own interactive piano that can play some simple tunes.

{{< run-finished-project >}}

## Credits

Many thanks to Freesound user *dwengomes* and youtuber *Free High Quality Sound FX* for making their 
sounds available under the Creative Commons License. 

### Detailed Credits

{{< asset-credits >}}


---

## Set up

We have provided you with some code to begin your project with. — click the *green flag* to run the program — 
you should see a music room appear as the backdrop, a single white C key, a single black key and 
an image of a cake and jingle bells will also appear on your screen! This is the base that we will build our game upon. 

Look through the code and click on the white key to see what happens. Explore the code before moving on to the next steps!

## Adding Piano Keys

Our piano will have 7 white keys in total, currently, we only have one key set up. Let’s see how we can add more keys to our code.
The first step is to add the rest of the costumes to our `Costumes` variable in the *White Key* class.

{{< commit add-key-costumes >}}

Now we can also add the sounds for our other keys, along with their names. 

{{< commit add-sound >}}

We can use a loop to clone 7 White Key Sprites. In order to differentiate the keys, we will create a variable called *index* for each Sprite.
We do this to easily identify which key we are dealing with. Inside this loop we can tell each key to wear a different costume, and to have a different sound from the other keys. Once the loop is finished, we want to hide the original Key Sprite as we do not need it anymore – we just want the clones!

{{< commit add-loop-for-keys >}}

## Update Mouse Functionality

When we use our mouse and click on any *White Key*, we want two things to happen. 
Firstly, we want the note to become highlighted, and we want a sound to be triggered. 
However, if you click on any note right now, it will change to the *key D* and after the note finishes playing it changes to the *key C*.
This happens, because in the `when_this_sprite_clicked` function, we give each key the same costume. This worked when we had a single key, but now with many keys it no longer works.

The costume that we want our key to change to after it is clicked, is exactly *seven* costumes down from its original costume.
We can use the `self.index` variable we set up to find the current position of our costume and add 7 to it to get the correct costume we want our sprite to have when the key is clicked. We also want the key’s sound to be played when the key gets clicked. Right now, the same sound plays for all the keys. We can use the variable we created earlier in the loop called *sound* to play the sound of the key we just clicked. After the sound is played, we want the key to switch back to its previous unhighlighted costume. We can use the index variable we created to get the original costume for our key.

{{< commit finished-mouse-function >}}

## Add Keyboard

To make our game feel a bit more like a real piano, we can add functionality to our keyboard. We can select keys from 
our keyboard which will trigger the different keys and their sounds.
We will use the keys ‘A,S,D,F,G,H,J’ to trigger different keys, however, you can change these keys to be whatever you like.
We will use the `key_pressed` function to check if the keys we are looking out for have been pressed. Let’s create a function 
to check if the keyboard key *A* has been pressed. When the key *A* on our keyboard is pressed, we want the costume of the 
piano key *C* to change and play C’s sound. We know our piano key C is indexed at 0, and we can use this to change our costume 
and play the correct sound. We will add an if statement to make sure we are only changing the key whose *index is 0*.

{{< commit add-keyboard-trigger-A >}}

Now if you try to run the project you will be able to hear a note when you press down on the key *A * on your keyboard! 
Now we should add similar methods for the other keys and notes. 
One thing to watch out for is that each method we declare needs to have a different name or we will be overwriting the previous methods we created. 

{{< commit add-remaining-key-triggers >}}

If you try the project out now you should be able to hear all the different notes when you press the different keys on your keyboard.
If you are hearing the same note more than once – check if you have by mistake added the same sound to two different keys! 

## Add Black Keys

To finish off our piano look, we need to add the rest of the *Black Keys*. The Black Keys are not functional but will 
give us the feel and look of a new piano. 
Our Piano needs 5 Black Keys. We will alter the code we already have, and we will use a for loop to draw our keys,
just like we did with the *White Keys*. We need there to be a large gap between the second and third Black Key as that is what a real piano looks like. To achieve this, we will create a loop that will be in the range of 6, and when we come across *index 2* which would be the third key (Remember we start counting at 0!), we will skip it in order to create the gap between the keys. We can do this by checking if our index is not equal to 2, if it is, we simply do nothing and wait for the next iteration of the loop. The positioning of the Black Keys depends on the size of the key you use and where you want to place it, it can be a little bit of trial and error to get the right coordinates.

{{< commit finish-black-key-class >}}

## Let’s Play a Song!

So far, we have been able to hear the different notes played by our piano through pressing different keys on our keyboard 
or using the mouse. Next, we will get our program to play us a song! The `Song class` is already set up for you. 
In the top left corner, you can see two images, a Birthday Cake and Jingle Bells. These are the two songs that we will program. 
When we click on the cake or jingle bells, we want the corresponding song to play. Let’s create a `when_this_sprite_clicked` function
 in the *Song class* that will broadcast a message to our *White Key Sprites* to let them know which song they need to play. 

{{< commit add-song-clicked >}}

We also want to hide the *Song Sprites* from view when any song is playing. To do this we create a `hideOrShow` function 
in the *Song class*, that can hide or show our sprites from view. 

{{< commit add-hide-or-show-function >}}

We will program the Happy Birthday song first. For this, we need to create a `HappyBirthday function` in our *White Key class*.
This function will get triggered upon receiving the broadcast *HappyBirthday* that is sent out after we click on our cake image. We also need to tell Pytch how we want to play the song. Firstly, we want to make a list of all the clones of *White Keys* that we have. We can do this by using the `all_clones` function. This will return all the clones of the *White Keys* that we have. Next, I went ahead and found us a note sheet for Happy Birthday and copied down the notes in the order that we need to play them in. Pytch won’t be able to read letters, so I translated the letters to the corresponding index values to save us time. *-1* means we get a half second break before playing the next note! We also want to show the *Notes* variable on our screen when the song is playing. We can do this using the `show_variable` function.

{{< commit setup-happy-birthday >}}

We will use a loop to go through each note in our song, and whichever note we are reading right now should play. 
If we come across a -1 number, this signalises a break and we need to pause for half a second. When reading the notes, 
we want the corresponding key to play, and change its costume to the highlighted one. Lastly, we want to hide the notes 
when we are finished with the tune and show the cake image again as the tune is now over. We do this by calling the `hideOrShow` function in
 our *Song class* and passing it the value `False`. 

{{< commit finish-happy-birthday >}}

### Now Let’s Add Jingle Bells!

Lastly, we will add Jingle Bells! Before looking at the code below, try to add a Jingle Bells function on your one. 
The notes to play Jingle Bells are as follows "EEE-EEE-EGCDE-FFFFFEEEEDDEED-G-EEE-EEE-EGCDE-GGGGGEEEGGFDC". 
The “-“ symbolises a break! (Remember in our game the number -1 tells our program that we need half a second break). 

If you are stuck take a look at the below code of the Jingle Bells Function.

{{< commit add-jingle-bells >}}

And that is our game finished! -- click the *green flag* to run our game. 

## Challenges

If you would like to continue working on your piano game, here are some challenges you can try out!

1.	Give the game a makeover, style it anyway you want, add more keys, change the background or add more sounds! 
2.	Try adding more songs you like to the game. You can find music sheets for any song on Google.
3.	Make the black keys work, try adding sounds to the black keys to create more sophisticated music.