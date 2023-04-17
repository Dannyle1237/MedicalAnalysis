//Stuff for search bar 
/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
function dropdown() {
    document.getElementById("dropdown_search").classList.toggle("show");
  }
  
  function filterFunction() {
    var input, filter, ul, li, a, i;
    input = document.getElementById("symptom_input");
    filter = input.value.toUpperCase();
    div = document.getElementById("dropdown_search");
    a = div.getElementsByTagName("a");
    for (i = 0; i < a.length; i++) {
      txtValue = a[i].textContent || a[i].innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        a[i].style.display = "";
      } else {
        a[i].style.display = "none";
      }
    }
  }

function dostuff(){
  var ul = document.querySelector('ul');
  var li = document.createElement('li');
  var text = document.createTextNode('New list item');
  li.appendChild(text);
  ul.appendChild(li);
}

