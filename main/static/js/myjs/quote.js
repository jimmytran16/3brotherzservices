var quote_form = document.getElementById('quote-form');
var contact_form = document.getElementById('contact-form');
var contact_btn = document.getElementById('contact-btn');
var quote_btn = document.getElementById('quote-btn');
contact_form.hidden = true; //hide the quotes form first
quote_btn.style.backgroundColor = '#a27405';

function showQuoteForm() { //function to show quote form
  quote_form.hidden = false;
  contact_form.hidden = true;
  contact_btn.style.backgroundColor = '#f4b214';
  quote_btn.style.backgroundColor = '#a27405'
}

function showContactForm() { //function to show contact form
  quote_form.hidden = true;
  contact_form.hidden = false;
  contact_btn.style.backgroundColor = '#a27405';
  quote_btn.style.backgroundColor = '#f4b214'
}
