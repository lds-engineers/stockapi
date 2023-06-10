function callFunctionEveryFiveSeconds() {
    setInterval(function() {
      $.ajax({
        url: '/stockData/',  // Replace with the URL of your Django API endpoint
        method: 'GET',
        success: function(data) {
          // Handle the response from the server
          console.log(data);
        },
        error: function(xhr, status, error) {
          // Handle errors, if any
          alert(error)
        //   console.error(error);
        }
      });
    }, 5000);  // 5000 milliseconds = 5 seconds
  }
  