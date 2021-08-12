var DateTime = luxon.DateTime;

setInterval(showTime, 1000);
  function showTime() {
    let time = DateTime.now().setZone("Australia/Brisbane");
    let format = time.toFormat('hh:mm:ss a, ccc DD')
    let formatted = ("Server Time<br />" + format)

    document.getElementById("mytime")
      .innerHTML = formatted
    }

showTime();
