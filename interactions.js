const sims = [
    { name: '', key: '{initiator}  {target}' },
];

const { Configuration, OpenAIApi } = require("openai");
const configuration = new Configuration({
    apiKey: process.env.OPENAI_KEY,
});
const openai = new OpenAIApi(configuration);

const doit = async (data) => {
    try {
        const response = await openai.createChatCompletion({
            model: 'gpt-4',
            temperature: 0.7,
            messages: [
                {
                    role: "system",
                    content: `I am writing a novel about two characters. I will give you a generic action, and you must write 10 prompts that would generate the beginning of an interaction between the two characters in the novel. Write the result one per line, dont return anything else. Here is an example:
    
    action: {initiator} reveals a big deep secret to {target}        
    "{target}, I need to tell you something. Promise me you won't judge," {initiator} says nervously.
    "I have been keeping a secret for so long, but I trust you enough to share it with you," {initiator} says, looking into {target}'s eyes.
    "You know, {target}, there's something I've never told anyone before, but I feel like I can confide in you," {initiator} says, hesitatingly.
    "I've been carrying this secret for far too long, and it's eating me up inside. {target}, I think it's time I share it with you," {initiator} confesses, their voice trembling.
    "I never thought I would reveal this, but you mean a lot to me, {target}. I need you to know the truth," {initiator} says, taking a deep breath.
    "There's something I've been hiding, {target}, and it's time I let it out. I hope you can handle it," {initiator} says, looking anxious.
    "I've kept this hidden for years, {target}, but I can't bear the weight anymore. I have to tell you," {initiator} admits, looking vulnerable.
    "This secret has haunted me for so long, {target}, but I feel a connection with you that makes me want to share it. Can I trust you?" {initiator} asks cautiously.
    "I've always admired your ability to keep secrets, {target}, but there's one I can no longer keep to myself. Brace yourself," {initiator} says, preparing to share something profound.
    "I've been meaning to tell you this, {target}, but I've never found the right time. Now, in this moment, I feel it's the right moment to reveal my deepest secret," {initiator} says with a mixture of relief and apprehension.`,
                },
                {
                    role: "user",
                    content: `action: ${data.key}`,
                }
            ]
        })
    
        const bulletPoints = response.data.choices[0].message.content.trim();
    
        const lines = bulletPoints.split('\n')
    
        const newObject = {
            [data.name]: {
                actions: lines,
            },
        }
    
        const outputJson = JSON.stringify(newObject, null, 4);
        const removed = removeFirstAndLastLine(outputJson).trimEnd() + ",";
        console.log(removed);
    } catch (exception) {
        const newObject = {
            [data.name]: {
                actions: ['failed'],
            },
        }
        
        const outputJson = JSON.stringify(newObject, null, 4);
        const removed = removeFirstAndLastLine(outputJson).trimEnd() + ",";
        console.log(removed);
    }
}

const run = async () => {
    sims.forEach(async sim => {
        doit(sim);
    });
}

run();

function removeFirstAndLastLine(str) {
    const lines = str.split('\n');
    lines.shift(); // Remove the first line
    lines.pop(); // Remove the last line
    return lines.join('\n');
}

// const leftSims = [];
// sims.forEach(sim => {
//     if (doneSims[sim] === undefined) {
//         leftSims.push(sim);
//     }
// })

// console.log(JSON.stringify(leftSims, null, 4));