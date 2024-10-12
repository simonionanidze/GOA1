// forEach მეთოდის კლონი
function myForEach(array, callback) {
    for (let i = 0; i < array.length; i++) {
        callback(array[i], i, array);
    }
}

// გამოყენების მაგალითი
const fruits = ['apple', 'banana', 'cherry'];

myForEach(fruits, function(fruit, index) {
    console.log(index + ': ' + fruit);
});
