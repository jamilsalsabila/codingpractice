const generateCards = () => {
    const ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K'];
    const suits = ['C', 'D', 'H', 'S'];

    const cards = new Array(52).fill('');

    for (let i = 0; i < cards.length; i++) {
        cards[i] = suits[Math.floor(i / 13)] + ranks[i % 13];
    }

    return cards;
}

const cardsShuffling = (nums) => {
    cards = generateCards();
    for (let i = 0; i < cards.length; i++) {
        let j = nums[i] % 52;
        [cards[i], cards[j]] = [cards[j], cards[i]];
    }
    return cards;
}

process.stdin.resume();

let inputString = '';
process.stdin.on('data', inputStdin => inputString += inputStdin);
process.stdin.on('end', _ => {
    input = inputString.trim().split(' ').map(s => parseInt(s.trim()));
    main(input);
});

const main = (input) => {
    const shuffledCards = cardsShuffling(input);
    console.log(...shuffledCards);
}