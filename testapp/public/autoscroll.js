setInterval(updateScroll,500);

function updateScroll(){

        var element = document.getElementById("log");
        if(document.getElementById('flexSwitchCheckChecked').checked) element.scrollTop = element.scrollHeight;
}
