
function myMap(array, callback) {
    const result = [];
    for (let i = 0; i < array.length; i++) {
        result.push(callback(array[i], i, array));
    }
    return result;
}

// გამოყენების მაგალითი
const names = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'];

const modifiedNames = myMap(names, (name, index) => {
    if (index % 2 === 0) {
        // ლუწი ინდექსი: გვჭირდება სახელი დიდი ასოებით
        return name.toUpperCase();
    } else {
        // კენტი ინდექსი: გვჭირდება სახელი პატარა ასოებით
        return name.toLowerCase();
    }
});

console.log(modifiedNames); // ["ALICE", "bob", "CHARLIE", "diana", "EVE"]
