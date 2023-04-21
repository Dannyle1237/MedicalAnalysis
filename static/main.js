//Code to add functionality to dropdown bar (When user clicks it is added)
let current = "";
let isMouseHover = false;

dropdown_items = document.getElementsByClassName("dropdown_item")

for(let i = 0; i < dropdown_items.length; i++){
  //Mouseover effect for dropdown items to show it in search bar
  dropdown_items[i].addEventListener("mouseover", function(e){
    tgt = e.target;
    if (tgt.classList.contains("dropdown_item")) {
      e.preventDefault(); // cancel link
      document.getElementById("symptom_input").value = tgt.innerHTML;
    }
  })
  //Click effect to save value if user wants it
  dropdown_items[i].addEventListener("mousedown", function(e){
    //console.log("Clicking");
    tgt = e.target;
    if (tgt.classList.contains("dropdown_item")) {
      current = tgt.innerHTML;
      document.getElementById("symptom_input").value = tgt.innerHTML;
    }
  })
}

disease_list_items = document.getElementsByClassName("list-group-item disease")
for(let i = 0; i < disease_list_items.length; i++){
  disease_list_items[i].style.cursor="pointer";
  disease_list_items[i].addEventListener("click", function(e){
    keyword = e.target.innerText;
    console.log(keyword)
    search_engine(keyword);
  })
}

closeButtons = document.getElementsByClassName("close")
for(let i = 0; i < closeButtons.length; i++){
  closeButtons[i].addEventListener("click", function(e){
    idx = e.srcElement.offsetParent.id;
    fetch('/delete-symptom', {
      method: 'POST',
      body: JSON.stringify({ update:"deleteSymptom", idx: idx}),
    }).then((_res) => {
        window.location.href ="/list";
    });
  })
}

//Stuff for search bar 
/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
function dropdown() {
  dd_search = document.getElementById("dropdown_search")
  if(dd_search.classList.toggle("show")){
    isMouseHover = true;
  }
  else{
    //console.log("value of current:" + current)
    document.getElementById("symptom_input").value = current;
    isMouseHover = false;
  }
}
  
function filterFunction() {
  //First save the value User has currently
  current = document.getElementById("symptom_input").value;
  //console.log("Saving as current:" + current);

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

function deleteSymptom(symptom){
  fetch('/delete-symptom', {
      method: 'POST',
      body: JSON.stringify({ symptom:symptom}),
  }).then((_res) => {
      window.location.href ="/";
  });
}

function search_engine(keyword){
  key = keyword;
   console.log(key);
 
 key = key.toLowerCase();
 key = key.replace(" ","");
 console.log(key);
 
  address = 'https://medlineplus.gov/'+key+'.html'
  window.open(address, "_blank", "width=500,height=600");
 }