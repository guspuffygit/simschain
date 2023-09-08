const { execSync } = require('child_process');
/**
 * Add lines and modify this list to generate a bunch of descriptions in parallel
 */
const interactions = [
  // example:
  // { name: 'si_marketStalls_ReviewDrink_CriticCareer', key: '{initiator} is at a food stall at a festival and is a food critic, they review the drink to {target}' },
  { name: '', key: '' }
];

const { Configuration, OpenAIApi } = require('openai');
const configuration = new Configuration({
  apiKey: process.env.OPENAI_KEY
});
const openai = new OpenAIApi(configuration);

function splitIntoGroupsOfTen(arr) {
  const result = [];

  for (let i = 0; i < arr.length; i += 10) {
    const group = arr.slice(i, i + 10);
    result.push(group);
  }

  return result;
}

const generateInteractionDescription = async (data) => {
  const value = toNames(data.value);
  try {
    const response = await openai.createChatCompletion({
      model: 'gpt-4',
      temperature: 0.7,
      messages: [
        {
          role: 'system',
          content: 'Rewrite the input as an output in "present continuous tense".'
        },
        {
          role: 'user',
          content: `Input:
${value}
Output:`
        }
      ]
    });

    const output = response.data.choices[0].message.content.trim();

    const newObject = {
      [data.key]: {
        pre_actions: [
          backFromNames(output),
        ],
      }
    };

    const outputJson = JSON.stringify(newObject, null, 4);
    return removeFirstAndLastLine(outputJson).trimEnd() + ',';
  } catch (exception) {
    const newObject = {
      [data.name]: {
        actions: ['failed']
      }
    };

    const outputJson = JSON.stringify(newObject, null, 4);
    return removeFirstAndLastLine(outputJson).trimEnd() + ',';
  }
};

function toNames(line) {
  return line.replace('{initiator}', 'Avery').replace('{target}', 'Charlie');
}

function backFromNames(line) {
  return line.replace('Avery', '{initiator}').replace('Charlie', '{target}').replace('currently ', '');
}

const run = async () => {
  const output = execSync('python3 descriptions.py', { encoding: 'utf-8' }).trim();
  const lines = output.split('\n');
  const groups = splitIntoGroupsOfTen(lines);
  for (const group of groups) {
    const promises = [];
    group.forEach((item) => {
      const blob = JSON.parse(item);
      promises.push(generateInteractionDescription(blob));
    })
    const results = await Promise.all(promises);
    results.forEach((result) => {
      console.log(result);
    })
  }
};

run();

function removeFirstAndLastLine(str) {
  const lines = str.split('\n');
  lines.shift(); // Remove the first line
  lines.pop(); // Remove the last line
  return lines.join('\n');
}
