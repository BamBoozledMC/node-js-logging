setInterval(showTime, 1000);
  function showTime() {
    let time = new Date();
    let mytime = time.toLocaleString(undefined, { timezone: "Australia/Brisbane" })
    let hour = time.getHours();
    let hour2 = time.getHours();
    let min = time.getMinutes();
    let sec = time.getSeconds();
    let day = time.getDay();
    let dates = time.getDate();
    let month = time.getMonth();
    let year = time.getFullYear();

    am_pm = " AM";
    if (hour > 12) {
      hour -= 12;
      am_pm = " PM";
    }
    if (hour == 0) {
      hr = 12;
      am_pm = " AM";
    }

    hour = hour < 10 ? "0" + hour : hour;
    min = min < 10 ? "0" + min : min;
    sec = sec < 10 ? "0" + sec : sec;

    let currentTime = hour + ":"
        + min + ":" + sec + am_pm;

    let currentTime24hr = hour2 + ":"
        + min + ":" + sec

    let days = {
      0: "Sun",
      1: "Mon",
      2: "Tue",
      3: "Wed",
      4: "Thu",
      5: "Fri",
      6: "Sat"
    }

    let months = {
      0: "Jan",
      1: "Feb",
      2: "Mar",
      3: "Apr",
      4: "May",
      5: "Jun",
      6: "Jul",
      7: "Aug",
      8: "Sep",
      9: "Oct",
      10: "Nov",
      11: "Dec"
    }

    let currentDate = `${days[day]} ${dates} ${months[month]} ${year}`;

            document.getElementById("time")
                .innerHTML = `Your Time<br />${currentTime} ${currentDate}`
        }

        showTime();
