/**
 * Give a plain text description of the objects and look of a location to generate an elaborate description
 * Use get_lot_id in the cheat console to get the lot id
 */
const locations = [
    // example
    // { name: '90243216', key: 'Willow Creek Archive, a library, Two level library, first floor: chess, bookshelves, ornate, long tables, bathrooms, kids area with foam tiles. Second floor: Large staircase to overlooking balcony with bookshelves lining the walls.' },
    { name: '1464926213', key: 'Planet Honey Pop, a Karaoke bar, Chic karaoke bar with small tables and chairs all surrounding a big karaoke stage, the stage has a podium and a big tv and flashing leds behind it showing the lyrics, a small bar lines the wall next to a small lounge set on top of a piano key carpet, the bathroom has two potty mouth 2.0 AI toilets.' },
];

const { Configuration, OpenAIApi } = require("openai");
const configuration = new Configuration({
    apiKey: process.env.OPENAI_KEY,
});
const openai = new OpenAIApi(configuration);

const generateLocationDescriptions = async (data) => {
    try {
        const response = await openai.createChatCompletion({
            model: 'gpt-4-0613',
            temperature: 0.7,
            messages: [
                {
                    role: "system",
                    content: `I am writing a novel. I will give you a generic description of a location in the novel, and you must write 10 sentences that would set the scene for the location in the novel. Write the result one per line, dont return anything else. Here is an example:

input: Blue velvet is a bar, a piano lounge with a campfire, piano man, dimly lit candles, long bar in the back, small couryard out back.    
The Blue Velvet, nestled amidst the bustling city streets, stood as a sanctuary of refined indulgence.
Its two-story façade exuded an air of timeless elegance.
The soulful melodies of a piano cascaded through the air, caressing the ears and soothing the senses.
Guests gathered around the polished grand piano, their faces aglow with the soft flicker of candlelight, engaged in whispered conversations and laughter that mingled harmoniously with the music.
To the left of the piano, a welcoming fireplace crackled with a gentle warmth, casting dancing shadows across the room and bathing the patrons in a cozy, amber embrace.
The back of the bar featured a small, urban oasis.
In the courtyard, a charming fountain adorned the center, its gentle cascade serenading visitors on a weathered stone bench.
Under the starlit canopy, patrons found respite, engaging in tranquil conversations amidst the night's whispers.
A skilled bartender stands behind a polished bar adorned with gleaming bottles, ready to craft soul-igniting or heart-soothing concoctions.
Plush bar stools offer comfort and a front-row seat to the vibrant characters that bring the place to life.`,
                },
                {
                    role: "user",
                    content: `input: ${data.key}`,
                }
            ]
        })
    
        const bulletPoints = response.data.choices[0].message.content.trim();
    
        const lines = bulletPoints.split('\n')
    
        const newObject = {
            [data.name]: {
                description: lines,
            },
        }
    
        const outputJson = JSON.stringify(newObject, null, 4);
        const removed = removeFirstAndLastLine(outputJson).trimEnd() + ",";
        console.log(removed);
    } catch (exception) {
        const newObject = {
            [data.name]: {
                description: ['failed'],
            },
        }
        
        const outputJson = JSON.stringify(newObject, null, 4);
        const removed = removeFirstAndLastLine(outputJson).trimEnd() + ",";
        console.log(removed);
    }
}

const run = async () => {
    locations.forEach(async sim => {
        generateLocationDescriptions(sim);
    });
}

run();

function removeFirstAndLastLine(str) {
    const lines = str.split('\n');
    lines.shift(); // Remove the first line
    lines.pop(); // Remove the last line
    return lines.join('\n');
}
