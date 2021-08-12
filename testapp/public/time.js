var DateTime = luxon.DateTime;

setInterval(showTime, 1000);
  function showTime() {
    let time = DateTime.now();
    // https://moment.github.io/luxon/index.html#/formatting?id=table-of-tokens
    let format = time.toFormat('hh:mm:ss a, ccc DD')
    let formatted = ("Your Time<br />" + format)

    document.getElementById("time")
      .innerHTML = formatted
    }

showTime();
