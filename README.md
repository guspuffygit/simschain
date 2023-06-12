# simschain

Simschain uses AI to help generate Sims descriptions, interaction descriptions, Location descriptions and other code for the sentient-sims mod

**NOTE: simschain uses GPT-4**

This incurs a higher cost when using the OpenAI API. If you want to use gpt-3.5-turbo or another model change it in the code before running.

## Pre-requisites

1. Install and use node 18
1. Set OpenAI API Key as an environment variable
```
OPENAI_KEY=sk-ljqoijqwd...
```

## Setup
```
git clone git@github.com:guspuffygit/simschain.git
cd simschain
npm i
```

## Interactions
Using a code editor, modify the interactions list in [interactions.js](https://github.com/guspuffygit/simschain/blob/main/interactions.js#L4-L8)

Run
```
node interactions.js
```

## Locations
Using a code editor, modify the locations list in [locations.js](https://github.com/guspuffygit/simschain/blob/main/locations.js#L5-L9)

Run
```
node locations.js
```
