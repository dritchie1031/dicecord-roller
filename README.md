## Installing

### Requirements

You must have Python 3 installed on your machine.

### Downloading

Do the usual `git clone` stuff to get the repository. It's not super complex. Then, run `pip install discord.py`.

### Adding the Discord Bot

Follow the steps at [this](https://realpython.com/how-to-make-a-discord-bot-python/#how-to-make-a-discord-bot-in-the-developer-portal) link.

### Running the Bot

Create a file named `creds.json` and put information in the following format:

```
{
  "TOKEN": "your-bot's-token-here",
  "GUILDS": [
    "your-guild-name",
    "your-other-guild-name"
  ]
}
```

When you're ready, just run `python roller.py`.

## Commands

### Roll

Base Command: `roll` or `r`
Args and Flags:

 - `1d10 + 3` This must be the first token after 'roll' or 'r'. 
 - `-a` Adds advantage to all dice rolled
 - `-d` Adds disadvantage to all dice rolled

## Roadmap

### Greater Command Flexibility
 - Allow users to not put spaces around '+' and '-'

### Initiative Rolls
 - `init` command
 - Add character name to tie initiative to a character
 - Add `-gm` flag to automatically set an initiative
 - `init show` command to display the initiative order
 - `init clear` to clear the initiative. Requires new rolls from everyone.

## Developing

### General Stuff

I decided to treat the roll functionality as a command line interface. I used pythons argparse library to do this.

### roller.py

This is where the main tool is handled, with the discord message handling and argparse stuff. 

### roll.py

This handles the rolling calculations and printing.