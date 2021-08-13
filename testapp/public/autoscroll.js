setInterval(updateScroll,1000);

function updateScroll(){

        var element = document.getElementById("log");
        if(document.getElementById('flexSwitchCheckChecked').checked) element.scrollTop = element.scrollHeight;
}
