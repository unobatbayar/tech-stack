// constants
const USERNAME_MESSAGE = 'Username must be only letters and or numbers. No less than 3 and more than 15 characters.';
const PASSWORD_MESSAGE = 'Password must be no less than 8 and more than 30 characters.';

const USERNAME_EMPTY = 'Please enter username.';
const MESSAGE_EMPTY = 'Please enter message.';
const NO_MESSAGES_YET = "<div class='uk-position-center uk-text-center'><i class='fas fa-ghost' style='font-size:93px'></i><p class='uk-text-large'>No messages yet...</p><p class='uk-text-meta'>Share your profile and start receiving!</p></div>";

// button states
const LOADING_BUTTON = '<div uk-spinner></div>';
const SIGNUP_BUTTON = 'sign up';
const LOGIN_BUTTON = 'log in';

var last_sent_message = null;


// return to previous page
function back_page() {
  window.history.back()
}

// sanitize user inputs
function sanitize(string) {
  const map = {
    '&': '&amp;',
    '<': '&lt;',
    '>': '&gt;',
    '"': '&quot;',
    "'": '&#x27;',
    "/": '&#x2F;',
  };
  const reg = /[&<>"'/]/ig;
  return string.replace(reg, (match) => (map[match]));
}


$("post_recipient").on({
  keydown: function(e) {
    if (e.which === 32)
      return false;
  },
  change: function() {
    this.value = this.value.replace(/\s/g, "");
  }
});

function notify(message, status) {
  switch(status) {
    case 'primary':
      message = "<i class='fas fa-info-circle'></i> " + message;
      break;
    case 'success':
      message = "<i class='fas fa-check-circle'></i> " + message;
      break;
  } 
  UIkit.notification({ message: message, status: status, timeout: 2000 })
}

// Login
function login() {
  var username = document.getElementById('post_username_login');
  var password = document.getElementById('post_password_login');
  var email = document.getElementById('email_login');
  var button = document.getElementById('login_button');

  if(email.value.length > 0){
    notify( "We couldn't verify your account with that information.", 'primary');
    return;
  }
 
  if (username) {
    if (!username.checkValidity()) {
      document.getElementById('validation-login').innerHTML = USERNAME_MESSAGE;
    }
    else {
      if (password) {
        if (!password.checkValidity()) {
          document.getElementById('validation-login').innerHTML = PASSWORD_MESSAGE;
        }
        else {
          // disable button
          button.disabled = true;
          button.innerHTML = LOADING_BUTTON;

          document.getElementById('validation-login').innerHTML = '';
          
          //notify('Logging in...', 'primary');
          $.ajax({
            type: "POST",
            url: '../api/login.php',
            data: {
              username: username.value,
              password: password.value,
            },
            success: function (data) {
              if(data.response == 'Success'){
                window.location = "../messages";
              }
              else notify(data.response, 'primary');

              // enable button
              button.disabled = false;
              button.innerHTML = LOGIN_BUTTON;
        
            },
            error: function (xhr, status, error) {
              notify(error, 'primary');

              // enable button
              button.disabled = false;
              button.innerHTML = LOGIN_BUTTON;

              // failed attempt
              
            }
          });
        }
      }
      else {
        document.getElementById('validation-login').innerHTML = '';
      }
    }
  }
}

// Unobscured copy to clipboard
function copyToClipboard(username){
  var textToCopy = "konple.com/"+username;
  navigator.clipboard.writeText(textToCopy);
  notify('Copied', 'primary');
}

// Check registration
function signup() {
  var username = document.getElementById('post_username_signup');
  var password = document.getElementById('post_password_signup');
  var email = document.getElementById('post_email_signup');
  var button = document.getElementById('signup_button');

  if(email.value.length > 0){
    notify('Success', 'primary');
    return;
  }

  var validation_message = document.getElementById('validation-signup');

  // Detect spam, TODO

  if (username) {
    if (!username.checkValidity()) {
      validation_message.innerHTML = USERNAME_MESSAGE;
    }
    else {
      if (password) {
        if (!password.checkValidity()) {
          validation_message.innerHTML = PASSWORD_MESSAGE;
        }
        else {
          // disable button
          button.disabled = true;
          button.innerHTML = LOADING_BUTTON;

          // empty text
          validation_message.innerHTML = '';
          //notify('Signing up...', 'primary');
          $.ajax({
            type: "POST",
            url: '../api/register.php',
            data: {
              username: username.value,
              password: password.value,
              captcha: button.value,
            },
            success: function (data) {
              if(data.response == 'Success'){
                window.location = "../messages";
              }
              else{
                // clear username since it doesn't meet requirement
                username.value = "";
                notify(data.response, 'primary');
              }
              
              // enable button again
              button.disabled = false;
              button.innerHTML = SIGNUP_BUTTON;
            },
            error: function (xhr, status, error) {
              notify(error, 'primary');

              // enable button again
              button.disabled = false;
              button.innerHTML = SIGNUP_BUTTON;
            }
          });
        }
      }
      else {
        validation_message.innerHTML = '';
      }
    }
  }

}

// Check if user trying to send same message
function check_duplicate(message){
  return (last_sent_message == message);
}

// Send message
function send() {
  var username = document.getElementById('post_recipient');
  var message = document.getElementById('post_message');
  var email = document.getElementById('post_email');

  // Honey pot
  if(email.value.length > 0){
    notify('Message delivered!', 'success');
    return;
  }

  // Same message
  if(check_duplicate(message.value)){
    notify('Sending message...', 'primary');
    notify('Message delivered!', 'success');
    return;
  }

  if (!username.value) {
    notify(USERNAME_EMPTY, 'primary');
  }
  else if (!username.checkValidity()) {
    notify(USERNAME_MESSAGE, 'primary');
  }
  else if (!message.checkValidity()) {
    notify(MESSAGE_EMPTY, 'primary');
  }
  else {
    notify('Sending message...', 'primary');
    $.ajax({
      type: "POST",
      url: '../api/send.php',
      data: {
        username: username.value,
        message: message.value,
      },
      success: function (data) {
        // save last message
        last_sent_message = message.value;

        if(data.code == '200' && data.response == 'Success'){
            // sent screen
            window.location = "../success";

            // clean the form
            username.value = "";
            message.value = "";
        }
        else{
          notify("Something went wrong", 'primary');
        }
        
      },
      error: function (xhr, status, error) {
        notify(error, 'primary');
      }
    });
  }
}

// delete account
function delete_account() {
  notify('Deleting account...', 'primary');
  $.ajax({
    type: "POST",
    url: '../api/delete_account.php',
    success: function (data) {
      if(data.response == 'Success'){
        window.location = "../";
      }
      else notify(data.response, 'primary');
    },
    error: function (xhr, status, error) {
      notify(error, 'primary');
    }
  });
}


// Focus message for better user experience
function focus_message() {
  $(document).ready(function () {
    setTimeout(function () {
      document.getElementById('post_message').focus();
    }, 200);
  });
}

// Focus username box for better user experience
function focus_username() {
  $(document).ready(function () {
    setTimeout(function () {
      document.getElementById('post_recipient').focus();
    }, 200);
  });
}


var working = false;
var start = 0;
var not_found = false;

// Get messages
function get_messages() {
  if(!working && !not_found){
    working = true;
    if(start == 0) document.getElementById('top_span').innerHTML = '<div uk-spinner="ratio: 1"></div>';
    $.ajax({
      type: "POST",
      url: '../api/get_messages',
      data: {
        start: start,
      },
      success: function (data) {
        document.getElementById('top_span').innerHTML = '';
        if(data == 'Not found'){
          if(start == 0) document.getElementById('received_messages').innerHTML = NO_MESSAGES_YET;
          not_found = true;
        }
        else {
          document.getElementById('received_messages').innerHTML += data;
          if(start == 0){
            working = false;
          }
          else{
            setTimeout(function() {
              working = false;
            }, 3000)
          }
          start += 8;
        }
      },
      error: function (xhr, status, error) {
        document.getElementById('top_span').innerHTML = '';
        notify(error, 'primary');
      }
    });
  }
}

// Get messages
function update_messages() {
  // reset values
  start = 0;
  not_found = false;
  working = false;
  
  // send request
  document.getElementById('top_span').innerHTML = '<div uk-spinner="ratio: 1"></div>';
  $.ajax({
    type: "POST",
    url: '../api/get_messages',
    data: {
      start: 0,
    },
    success: function (data) {
      document.getElementById('top_span').innerHTML = '';

      if(data == 'Not found'){
        if(start == 0) document.getElementById('received_messages').innerHTML = NO_MESSAGES_YET;
      }
      else {
        document.getElementById('received_messages').innerHTML = data;
        start += 8;
      }
    },
    error: function (xhr, status, error) {
      document.getElementById('top_span').innerHTML = '';
      notify(error, 'primary');
    }
  });
}


// Delete all messages permanently
function delete_all_messages() {
  document.getElementById('top_span').innerHTML = '<div uk-spinner="ratio: 1"></div>';
  $.ajax({
    type: "POST",
    url: '../api/delete_all_queue.php',
    data: {
    },
    success: function (data) {
      document.getElementById('top_span').innerHTML = '';
      if(data.response == 'Success'){
        document.getElementById('received_messages').innerHTML = NO_MESSAGES_YET;
      }
    },
    error: function (xhr, status, error) {
      document.getElementById('top_span').innerHTML = '';
      notify(error, 'primary');
    }
  });
}

function setOnScrollObservable(){
  $(window).scroll(function (event) {
    if($(this).scrollTop() + 1 >= $('body').height() - $(window).height()){
        get_messages();
    }
});
}

// function addButtonOnClickListener(){
//   $("button").click(function() {
   
//   });
// }

function setupView(){
  get_messages();
  setOnScrollObservable();
}

// async function registerSW() {
//   if ('serviceWorker' in navigator) {
//     try {
//       await navigator.serviceWorker.register('../sw.js');
//     } catch (e) {
//       console.log(`SW registration failed`);
//     }
//   }
// }

window.addEventListener('load', () => {
  //registerSW();
});

// Initialize deferredPrompt for use later to show browser install prompt.
//let deferredPrompt;

window.addEventListener('beforeinstallprompt', (e) => {
  // Prevent the mini-infobar from appearing on mobile
  e.preventDefault();
  // Stash the event so it can be triggered later.
  deferredPrompt = e;
  // Update UI notify the user they can install the PWA
  showInstallPromotion();
  // Optionally, send analytics event that PWA install promo was shown.
});

// async function installApp(){
//   // Hide the app provided install promotion
//   hideInstallPromotion();
//   // Show the install prompt
//   deferredPrompt.prompt();
//   // Wait for the user to respond to the prompt
//   const { outcome } = await deferredPrompt.userChoice;
//   // Optionally, send analytics event with outcome of user choice
//   console.log(`User response to the install prompt: ${outcome}`);
//   // We've used the prompt, and can't use it again, throw it away
//   deferredPrompt = null;
// }