Plotly.d3.csv("/static/csv/installs_ecost.csv", function (err, rows) {
  function unpack(rows, key) {
    return rows.map(function (row) {
      return row[key];
    });
  }
  var temp = unpack(rows, 'size_kW');
  var hold_converted = []

  for (i = 0; i < temp.length; i++) {
    var temp_var = parseFloat(temp[i]);
    console.log(typeof temp_var);
    hold_converted.push(temp_var);


  }

  console.log(hold_converted);
  console.log(typeof hold_converted);
  console.log(typeof unpack(rows, 'state'));

  /* Adjust colorscale to green to red */

  var data = [{
    type: 'choropleth',
    locationmode: 'USA-states',
    locations: unpack(rows, 'abbr'),
    z: hold_converted,
    text: unpack(rows, 'size_kW'),
    colorscale: [
      [0, 'rgb(242,240,247)'],
      [0.2, 'rgb(218,218,235)'],
      [0.4, 'rgb(188,189,220)'],
      [0.6, 'rgb(158,154,200)'],
      [0.8, 'rgb(117,107,177)'],
      [1, 'rgb(84,39,143)']
    ],
  }];

  var layout = {
    title: 'Total Installed Capacity',
    geo: {
      scope: 'usa',
      showlakes: true,
      lakecolor: 'rgb(255,255,255)'
    }
  };

  Plotly.plot(myDiv, data, layout, {
    showLink: false
  });

});