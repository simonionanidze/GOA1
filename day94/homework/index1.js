function mapToObjectNames(users) {
    return users.map(user => user.name);
}


const usersArray = [
    { id: 1, name: 'Alice' },
    { id: 2, name: 'Bob' },
    { id: 3, name: 'Charlie' }
];
const namesArray = mapToObjectNames(usersArray);
console.log(namesArray); 
