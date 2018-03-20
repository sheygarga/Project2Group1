d3.json("/bar", function(error, dataset) {
  if (error) return console.warn(error);
  console.log(dataset)
  var barData = {
    labels: dataset[0],
    datasets: [{
	  label: 'Low Capacity',
	  backgroundColor: "#FF0000",
	  data: dataset[1]
    }, {
	  label: 'Medium Capacity',
	  backgroundColor: "#FF6A00",
	  data: dataset[2]
    }, {
	  label: 'Large Capacity',
	  backgroundColor: "#FFD000",
	  data: dataset[3]
    }]
  };

  var ctx = document.getElementById("myChart");
  var myChart = new Chart(ctx, {
    type: 'bar',
	  data: barData,
	  options: {
	    title: {
	  	  display: true,
		  text: '2014 Installed Solar Power Generation Capacity (kW)'
	    },
	    tooltips: {
		  mode: 'index',
		  intersect: false
	    },
		  responsive: true,
		  scales: {
		    xAxes: [{
			  stacked: true,
		    }],
		    yAxes: [{
			  stacked: true
		    }]
		  }
	  }
  });

});

