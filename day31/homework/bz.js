

const productsData = [
    { name: "Смартфон", price: 500, image: "phone.jpgn.jpeg" },
    
];

    const productsContainer = document.getElementById("products");

    productsData.forEach(product => {
        const productElement = document.createElement("article");
        productElement.classList.add("product");

        const imageElement = document.createElement("img");
        imageElement.src = product.image;
        imageElement.alt = product.name;

        const nameElement = document.createElement("h2");
        nameElement.textContent = product.name;

        const priceElement = document.createElement("p");
        priceElement.classList.add("price");
        priceElement.textContent = `Цена: $${product.price}`;

        const addButton = document.createElement("button");
        addButton.textContent = "Добавить в корзину";
        addButton.addEventListener("click", () => addToCart(product));

        productElement.appendChild(imageElement);
        productElement.appendChild(nameElement);
        productElement.appendChild(priceElement);
        productElement.appendChild(addButton);

        productsContainer.appendChild(productElement);
    });



function addToCart(product) {
    
    console.log(`Product added to cart: ${product.name}`);
}


window.addEventListener("load", displayProducts);