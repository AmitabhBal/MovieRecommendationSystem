const loginForm = document.getElementById('login-form');

loginForm.addEventListener('submit', (event) => {
  event.preventDefault();
  // Simulate form submission (replace with your actual login logic)
  console.log('Form submitted:', {
    email: loginForm.elements.email.value,
    password: loginForm.elements.password.value,
  });

const listButton = document.getElementById("listButton");

// Add click event listener to the list element
listButton.addEventListener("click", (event)) {
  // Function to open the container
  var container = document.getElementById("myContainer");
  container.style.display = "block";
});


  // Redirect to the main application page on successful login (replace with your redirection logic)
  window.location.href = 'movies.html'; // Assuming movies.html is your movie recommendation page
});