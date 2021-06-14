# crispy-guacamole

###### Only choosing the best of names.

## Import Requirements

All the import requirements are present within requirement.text. Use the following code to install all the required imports
```
pip3 install -r requirements.text
```

# Displaying a Random Histogram

If you run the program and choose the "Not Play Some Pokemon" option, as displayed here:
![not-play-some-pokemon](https://user-images.githubusercontent.com/73107662/121950986-f7600700-cd77-11eb-8bf7-143bb9b56179.png)
then you will be greeted with a random histogram which is produced using numpy and termiplotlib as such:
![random-histogram](https://user-images.githubusercontent.com/73107662/121951180-368e5800-cd78-11eb-99cc-d40c21803810.png)

# Playing Some Pokemon

If instead, you select "Play Some Pokemon" option, you are asked to enter your favourite pokemon and your opponent pokemon both of which are validated:
![validation](https://user-images.githubusercontent.com/73107662/121951413-84a35b80-cd78-11eb-9863-d6406311ab56.png)
If the validation is passed then you move onto the battle where you have only one option to choose, Metronome, which deals random damage between 10 and 20 and so does your opponent (Side Note, I may have gone a bit overboard on Figlet, feel free to remove it if it becomes unreadable):
![battle](https://user-images.githubusercontent.com/73107662/121951588-bd433500-cd78-11eb-9b41-48b428bdf1f6.png)
When either of you wins, a display message is shown commemorating your win or cheering you on your loss.

# Playing Rock, Paper and Scissor with the computer

If you use -p or --play tags when you run the program, you get the ability to play Rock, Paper and Scissors with the computer. Again, the computer randomly chooses either of the three:
![image](https://user-images.githubusercontent.com/73107662/121952305-ae10b700-cd79-11eb-80a5-fa87f384ce4a.png)

# Test Cases

Well, since most of my functions return nothing, reliant on randomness to work and require user input midway through the function, testing them was extremely difficult and as such I am unable to test them. I tried using string stream to take print statements as input, however, it didn't work. As it stands, I was only able to test one function which I've included the test case in (And the function is duplicated merely only for testing)
