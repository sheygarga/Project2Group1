Plotly.d3.csv("/static/csv/installs_ecost.csv", function (err, rows) {
  function unpack(rows, key) {
    return rows.map(function (row) {
      return row[key];
    });
  }

  var temp = unpack(rows, 'size_two');
  console.log(temp);
  var hold_converted = []

  for (i = 0; i < temp.length; i++) {
    var temp_var = parseFloat(temp[i]);
    console.log(typeof temp_var);
    hold_converted.push(temp_var);


  }

  console.log(hold_converted);

  /* Change colorscale */

  var data = [{
    type: 'choropleth',
    locationmode: 'USA-states',
    locations: unpack(rows, 'abbr'),
    z: hold_converted,
    text: unpack(rows, 'Range'),
    autocolorscale: true
  }];

  var layout = {
    title: 'Medium Capacity Installations',
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