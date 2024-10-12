document.addEventListener('DOMContentLoaded', () => {
    
    const form = document.getElementById('registrationForm');
    const validationMessage = document.getElementById('validationMessage');

    
    form.addEventListener('submit', (event) => {
       
        event.preventDefault();
        
        
        const fullName = form.fullName.value.trim();
        const email = form.email.value.trim();
        const password = form.password.value.trim();
        const color = form.color.value;

        
        if (!fullName || !email || !password || !color) {
            validationMessage.textContent = 'All fields are required. Please fill in all fields.';
        } else {
            validationMessage.textContent = 'All fields are filled correctly!';
        }
    });
});
