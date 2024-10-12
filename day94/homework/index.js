function isPrime(num) {
    if (num <= 1) return false;
    for (let i = 2; i <= Math.sqrt(num); i++) {
        if (num % i === 0) return false;
    }
    return true;
}

function filterPrimeNumbers(numbers) {
    return numbers.filter(isPrime);
}


const numbersArray = [1, 2, 3, 4, 5, 16, 17, 18, 19];
const primeNumbers = filterPrimeNumbers(numbersArray);
console.log(primeNumbers); 
