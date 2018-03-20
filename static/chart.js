

/* data route */
var url = "/chartData";

function buildPlot() {
    Plotly.d3.json(url, function(error, response) {

        console.log(response);

        var trace1 = {
          x: response.map(data => chartData.state),
          y: response.map(data => chartData.size_one), 
          name: 'Size One',
          type: 'bar'
        };

        var trace2 = {
          x: response.map(data => chartData.state),
          y: response.map(data => chartData.size_two), 
          name: 'Size Two',
          type: 'bar'
        }

        var trace3 = {
          x: response.map(data => chartData.state),
          y: response.map(data => chartData.size_three), 
          name: 'Size Three',
          type: 'bar'
        }

        var data = [trace1, trace2, trace3];

        var layout = {barmode: 'stack'};

        Plotly.newPlot("chart", data, layout);
    });
}

buildPlot();

