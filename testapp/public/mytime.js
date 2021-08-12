setInterval(showTime, 1000);
  function showTime() {
    let time = new Date();
    let mytime = time.toLocaleString(undefined, { timezone: "Australia/Brisbane" })
    let myhour = time.getHours();
    let myhour2 = time.getHours();
    let mymin = time.getMinutes();
    let mysec = time.getSeconds();
    let myday = time.getDay();
    let mydates = time.getDate();
    let mymonth = time.getMonth();
    let myyear = time.getFullYear();

    am_pm = " AM";
    if (myhour > 12) {
      myhour -= 12;
      am_pm = " PM";
    }
    if (myhour == 0) {
      hr = 12;
      am_pm = " AM";
    }

    myhour = myhour < 10 ? "0" + myhour : myhour;
    mymin = mymin < 10 ? "0" + mymin : mymin;
    mysec = mysec < 10 ? "0" + mysec : mysec;

    let currentTime = myhour + ":"
        + mymin + ":" + mysec + am_pm;

    let currentTime24hr = myhour2 + ":"
        + mymin + ":" + mysec

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

    let currentDate = `${days[myday]} ${mydates} ${months[mymonth]} ${myyear}`;

            document.getElementById("mytime")
                .innerHTML = `Server Time<br />${currentTime} ${currentDate}`
        }

        showTime();
