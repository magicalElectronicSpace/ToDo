# Python Text Based to-do list
Welocme to the Python text based to-do list!

Here are your first steps to use this.



## Installation
This is a GitHub Repository, so, you have to clone the repository.

Here is how to do it:



git clone https://github.com/magicalElectronicSpace/todo.git




## Developer

This program was made by Magical Electronic Space, who is new to GitHub at the end of 2024.


## Running
You should make a shell script to run it. Write this:

#!/bin/your_sh

/path/to/your/python3 /path/to/your/ToDo

_________________________________________

"Replace /bin/your_sh with the shell you use."

"Replace /path/to/your/python3 with the path to your python3 (you can easily find out by typing in 'type python3')."

"Replace /path/to/your/ToDo with the path to your ToDo app (usually located in ~/ToDo)."

              

Saving your work:

If you are using vim, enter command mode and type in :wq. If you are using nano, press Control+O and Control+X.

chmod +x /usr/local/bin/todo

todo

It should return a prompt

Enter the name of the file you want to use: 

This can make a new file. Now you know how to use my ToDo list app!



## List syntax

This might be a little confusing:

❌ - Not done
✅ - Done

## How it works

Each ToDo list is in a JSON (JavaScript Object Notation) file.

The checks in the list command are really strings that say "Done" and "Not Done" in the JSON file.

### Libraries

The libraries that are used are json and pathlib, and nothing else.