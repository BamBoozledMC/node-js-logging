var DateTime = luxon.DateTime;

setInterval(showTime, 1000);
  function showTime() {
    let time = DateTime.now();
    let format = time.toFormat('hh:mm:ss a, ccc DD')
    let formatted = ("Your Time<br />" + format)

    document.getElementById("time")
      .innerHTML = formatted
    }

showTime();
