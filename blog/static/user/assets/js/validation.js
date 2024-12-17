function valid() {
    var firstname = document.getElementById('fname').value.trim(); // Corrected ID
    var lastname = document.getElementById('lname').value.trim(); // Corrected ID
    var profilepic = document.getElementById('profilepic').value.trim();
    var username = document.getElementById('username').value.trim();
    var email = document.getElementById('email').value.trim();
    var contact = document.getElementById('contactno').value.trim(); // Corrected ID
    var password = document.getElementById('password').value.trim();

    if (firstname === '') {
        alert('First Name is empty!');
        return false;
    }

    if (lastname === '') {
        alert('Last Name is empty!');
        return false;
    }

    if (profilepic === '') {
        alert('Please upload a Profile Picture!');
        return false;
    }

    if (username === '') {
        alert('Username is empty!');
        return false;
    }

    if (email === '') {
        alert('Email is empty!');
        return false;
    }

    if (contact === '') {
        alert('Contact number is empty!');
        return false;
    }

    if (password === '') {
        alert('Password is empty!');
        return false;
    }

    alert('Success!');
    return true;
}
