//Here I define global variables
//var can be changed through code
var timer = false;
//const cannot be changed
//Here I store the element from line 10 in the HTML doc "seconds"
//into variable html_seconds_value
const html_seconds_value = document.getElementById("seconds");
//When you want to change something on your html doc with JS, typically
//you will use documenet.getElementById or getElementByClassname
//However, there are also JQuerys if you wanna learn about that

//Here I store the minutes document element from the HTML page
const html_minutes_value = document.getElementById("minutes");

function start(){
    timer=true;
    seconds = 0;
    minutes = 0;
    
    //To debug a website, most beginners use console.log, 
    //which is similar to just a print statement
    //To see console.log statements, press F12 on your browser or open up 
    //inspect element, and you should see it in your console
    console.log("Timer set to true");

    if(timer){
        console.log("Timer is running")
        //Here, I use setInterval to set up a function to continuously run
        //It works similarly to a while loop, however an infinite while loop may 
        //crash your browser
        setInterval(function(){
            seconds += 1;
            //Now you can adjust the value on the doc by assigning
            //its textContent attribute a new value
            html_seconds_value.textContent = seconds + " seconds";
            if(seconds%60 == 0){
                minutes += 1;
                html_minutes_value.textContent = minutes + " minutes"; 
                seconds = 0;
            }
        }, 100);
    }
}


